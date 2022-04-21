# Filtering Scripts

  As mentioned in the paper, we are releasing the scripts of all the filters used for Automatic Quality Control.
    
## Existing dataset filteration

  Since the same filters were applied on 2 of the existing datasets, XL-Sum and MassiveSum, we are also releasing the `excluded_IDs` (i.e. the pair-ids or urls) of the article-summary pairs from these 2 datasets, which failed the basic filters of `Duplicate-Pair, Duplicate-Summary, Empty and Prefix` conditions.
  
  * See [XL-Sum Excluded IDs](excluded_IDs/xlsum/) and [MassiveSumm Excluded IDs](excluded_IDs/massivesumm)

### Running the scripts
  
  To run the filtering scripts, you would first need to download the (Telugu, Hindi, Marathi and Gujarati) datasets from [XL-Sum](https://github.com/csebuetnlp/xl-sum)
	(Note: MassiveSumm dataset was graciously provided to us by the authors and as per our best knowledge, the public link is unavailable so far)
  * Place them in the corresponding folders, `/data/xlsum/` or `/data/massivesumm/`
  * Make any necessary changes to the data paths in the `config.py` file
  * run the following:
  ```
  $ bash run.sh
  ```
  * Optionally, edit the `run.sh` file for your desired `--lang` and `--dataset_name` values
  
