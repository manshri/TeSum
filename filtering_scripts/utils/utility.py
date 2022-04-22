import pandas as pd
import json
import gzip

## Given selected list-of-pairs, Save the id/index/urls for 
def saveIDs(pairs, fname):
    pair_ids = []

    for each in pairs:
        if 'index' in each.keys():
            id_url = each['index']
        elif 'id' in each.keys():
            id_url = each['id']
        elif 'url' in each.keys():
            id_url = each['url']
        else:
            # id_url = '' # removed because this doesn't help with maintaining duplicate id dict
            # raise valueError for some id/index or url
            raise ValueError("No indexing found. \nAdd some id/index attribute.")

        pair_ids.append(id_url)

    with open(fname, 'w') as fout:
        for idx in pair_ids:
            fout.write("\nID: " + idx)


# Read main data file (jsonl format)
def read_data(filename):
    pairs = []
    for line in open(filename, 'r', encoding='utf-8'):
        if line.strip():
            pairs.append(json.loads(line))
    if len(pairs) == 1:
        pairs = pairs[0]
    print("\n# Samples: ", len(pairs))
    print("# Keys: ", pairs[0].keys())
    return pairs


# Read json.gz file as list-of-dictionaries
def read_gz_data(filename):
    sampleList = []
    with gzip.open(filename, 'rt', encoding='utf-8') as fin:
        for idx, line in enumerate(fin):
            sampleList.append(json.loads(line))
    print("\nNumber of samples : ", len(sampleList))
    print("Keys: ", sampleList[0].keys())
    return sampleList


# # Save output/final pairs (list-of-dicts saved as jsonl)
# def write_finalPairs(out_filename, final_pairs):
#     with open(out_filename, 'w', encoding='utf-8') as outfile:
#         for each_pair in final_pairs:
#             json.dump(each_pair, outfile, ensure_ascii=False)
#             outfile.write('\n')


# # Save output/final pair as json
# def write_toJSON(out_filename, pair_dict):
#     with open(out_filename, 'w', encoding='utf-8') as outfile:
#         json.dump(pair_dict, outfile, ensure_ascii=False)


# def display_nOfList(pairList, n=5):
#     for each in pairList[:n]:
#         for k,v in each.items():
#             print(k, ' : ', v)
#         print()


# Write pandas dataframe to JSONL file
def writeDF_to_jsonl(df, outfile):
    df.to_json(outfile, orient = 'records', lines=True, force_ascii=False, compression = 'infer', default_handler=str)


# # Read JSONL file
# def read_jsonl_to_dataframe(infile):
#     df = pd.read_json(infile, lines=True, compression = 'infer')
#     return df


