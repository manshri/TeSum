#!/bin/bash

## Possible argument values
	# dataset_name options ['xlsum', 'massivesum']
	# lang options ['te', 'hi', 'mr', 'gu']

python evaluation.py --lang='te' --dataset_name='xlsum'

## Use the following, if you have '.jsonl.gz' file format for MassiveSum dataset.
# python data_evaluation.py --lang='te' --dataset_name='massivesum' --filetype='.jsonl.gz'
