## TeSum Data
   
  This dataset contains a total of **20329** article-summary pairs, which are provided as carefully crafted train, dev and test splits of 16295(80%), 2017(10%) and 2017(10%) pairs resepectively. Extract the `tesum/data.tar.xz` to get the corresponding JSONL files of these splits.

### Preparing article text 

  The JSON samples contain `cleaned_text`, that is the processed article text. 
  The original articles are available only via the URLs provided with each JSON sample. The script for extracting the corresponding article content is provided and can be used as follows:
  
  ```
  $python preparing_data.py
  
  ```

   * See [Data](data/tesum/)




