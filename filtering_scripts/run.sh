#!/bin/sh

## Possible argument values
	# dataset_name options ['xlsum', 'massivesumm']
	# lang options ['te', 'hi', 'mr', 'gu']

python3 data_filters.py --lang='te' --dataset_name='xlsum'

## Use the following, if you have '.jsonl.gz' file format for MassiveSumm dataset.
# python data_filters.py --lang='te' --dataset_name='massivesumm' --filetype='.jsonl.gz'
