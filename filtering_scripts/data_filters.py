# # -*- coding: utf-8 -*-

### basic libraries
import os
import sys
import math
import random
import csv
import torch
import argparse
from itertools import permutations

from utils import prep, utility as ut, filters as fltr
from config import Config, LANGUAGES


def evaluate(config):

    ## Reading datsets
    print("reading ", config.datafile)
    if config.filetype == ".jsonl.gz":
        pairs = ut.read_gz_data(config.datafile)
    else:
        pairs = ut.read_data(config.datafile)

    # check if GPU is available
    mydevice = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # clean the data for removing noise, english tokens and timestamps
        # save=True --> save the cleaned pairs in a separate jsonl
    cleaned_pairs = prep.clean_text(pairs, config)  # , save=True)

    # Remove empty or duplicates and then remove prefixed pairs
    filtered_pairs = prep.apply_basic_filters(cleaned_pairs, config, save=True)
    
    # add all metric scores to each pair and convert to dataframe
    df = fltr.add_Metrics(filtered_pairs, lang=config.lang)
    print("Converted to dataframe.")

    '''
    # Optional Save
    
    # Saving the dataframe columns in a csv(excluding text and summary)
    metrics_csv_file = config.filter_dir + "metrics_%s.csv"%config.dataset
    df2 = df.loc[:, ~df.columns.isin(['url', 'text', 'summary'])]
    df2.to_csv(metrics_csv_file)  # optional, if needed
    print('metrics csv saved.')
    
    ## Save pairs with metrics
    # metrics_file = config.filter_dir + "metrics_%s.jsonl"%config.dataset
    # ut.writeDF_to_jsonl(df, metrics_file)  # optional, if needed
    '''

    ## filter by minimum numbers-of-sentences
    minSent_pair_df = fltr.filter_frameCol(df, "article_sentence_count", ">=", config.minSentCount)

    # filter by minimum numbers-of-tokens in article and summary
    minTokens_pair_df = fltr.rangeFilter_frameCol(minSent_pair_df, ["article_token_count", "summary_token_count"], [">=", ">="], [config.minArticleLength, config.minSummaryLength])

    # filter by minimum compression%
    minCompression_pair_df = fltr.filter_frameCol(minTokens_pair_df, "compression", ">=", config.minCompression)

    # Filter out pairs with compression% > 80
    validCompression_pair_df = fltr.filter_frameCol(minCompression_pair_df, "compression", "<=", config.maxCompression)

    # Filter out pairs with lower abstractivity
    minAbstractivity_pair_df = fltr.filter_frameCol(validCompression_pair_df, "abstractivity", ">=", config.minAbstractivity)

    # Filter out pairs with lower abstractivity
    validAbstractivity_pair_df = fltr.filter_frameCol(minAbstractivity_pair_df, "abstractivity", "<=", config.maxAbstractivity)


    # Save final remaining valid pairs
    filter_file = config.filter_dir + "filtered_%s.jsonl"%config.dataset
    ut.writeDF_to_jsonl(validAbstractivity_pair_df, filter_file)

    ## Optional # Saving the dataframe columns in a csv(excluding text and summary)
    # metrics_csv_file = config.filter_dir + "filtered_metrics_%s.csv"%config.dataset
    # df3 = validAbstractivity_pair_df.loc[:, ~validAbstractivity_pair_df.columns.isin(['url', 'cleaned_text', 'summary'])]
    # df3.to_csv(metrics_csv_file)  # optional, if needed
    # print('metrics csv saved.')


def main():
    parser = argparse.ArgumentParser(description='Process datset & language parameters.')
    parser.add_argument('--lang', type=str, default='te', help='working language')
    parser.add_argument('--datapath', default='./', help='data path') # , type=dir_path
    parser.add_argument('--filetype', type=str, default='.jsonl', choices=['.jsonl', '.jsonl.gz'], help='file compression type')
    parser.add_argument('--dataset_name', type=str, required=True, choices=['tesum', 'xlsum', 'massivesumm'], help='specify dataset name/category')
    args = parser.parse_args()

    if args.filetype == ".jsonl.gz" and not args.dataset_name == "massivesumm":
        raise TypeError("Only massivesumm dataset has .jsonl.gz filetype.")
    elif not args.filetype == ".jsonl.gz" and args.dataset_name == "massivesumm":
        raise TypeError("Massivesumm dataset has only .jsonl.gz filetype.")

    config = Config(args.datapath, args.dataset_name, args.lang, args.filetype)
    evaluate(config)


if __name__ == "__main__":
    main()
