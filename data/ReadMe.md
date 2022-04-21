## TeSum Data
   
  This dataset contains a total of **20329** article-summary pairs, which are provided as carefully crafted train, dev and test splits of 16295(80%), 2017(10%) and 2017(10%) pairs resepectively. Extract the `tesum/data.tar.xz` to get the corresponding JSONL files of these splits.

   * See [Data](tesum/)
   
  Each JSON sample contains a `cleaned_text` field, that is the processed article text. The original articles are available only via the URLs provided with each JSON sample. 
  
#### Preparing article text 

  The script for extracting the corresponding article content, using the URL, is also provided and can be used as follows:
  
  ```
  $ python3 preparing_data.py
  
  ```



