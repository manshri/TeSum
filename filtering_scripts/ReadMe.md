# Filtering Scripts

  As mentioned in the paper, we are releasing the scripts of all the filters used for Automatic Quality Control.
    
## Existing dataset filteration

  Since the same filters were applied on 2 of the existing datasets, XL-Sum and MassiveSum, we are also releasing the `excluded_IDs` (i.e. the pair-ids or urls) of the article-summary pairs from these 2 datasets, which failed the basic filters of `Duplicate-Pair, Duplicate-Summary, Empty and Prefix` conditions.
  
  * See [XL-Sum Excluded IDs](excluded_IDs/xlsum/) and [MassiveSumm Excluded IDs](excluded_IDs/massivesumm)

  To run the filtering scripts yourself, you would first need to download the (Telugu, Hindi, Marathi and Gujarati) datasets from [XL-Sum git](https://github.com/csebuetnlp/xl-sum) and follow the instructions given below:
	
(Note: MassiveSumm dataset was graciously provided to us by the authors and as per our best knowledge, the public link for the dataset is unavailable so far, 23rd Apr 2022)

### Running the scripts
  
  * Download and place the data files in the corresponding folders, `./xlsum/` or `./massivesumm/`
  * Prepare the XL-Sum data input file, by running the following:
  ```
  $ sh prepare_xlsum_data.sh
  ```
  * Make any necessary path/filename changes to the data paths in the `config.py` file
  * Finally, to apply the filters, run the following:
  ```
  $ python3 evaluation.py --lang='te' --dataset_name='xlsum'
  ```
  * MassiveSumm data input file (whenever it becomes publicly available), can be directly ingested by the filtering scripts with `--filetype=".jsonl.gz"`
  ```
  $ python3 evaluation.py --lang='te' --dataset_name='massivesumm' --filetype=".jsonl.gz"
  ```

  * Optionally, you can use the `run.sh` file for your desired `--lang` and `--dataset_name` values
  
