# TeSum

This repository contains the code and data of the paper titled **"TeSum: Human-Generated Abstractive Summarization Corpus for Telugu"** published in the *13th Edition of Language Resources and Evaluation Conference of the European Language Resources Association: LREC 2022*

## Table of Contents

- [TeSum](#tesum)
  - [Table of Contents](#table-of-contents)
  - [Data](#data)
  - [Filtering Scripts](#filtering-scripts)
  - [Benchmarks](#benchmarks)
  - [License](#license)



## Data
  
  ***Disclaimer: You must agree to the [license](#license) and terms of use before using the dataset.***
  
  We are releasing the first version of our TeSum dataset, that is human-generated and has gone through an extensive filtering and sampling-based-human-evaluation process as reported in the paper. For advance usage and model training purposes, the data is being provided as carefully prepared and feature balanced splits of 80%-10%-10% for train-dev-test sets respectively.
  
  All dataset files in the given `data.tar.xz`, are in `.jsonl` format i.e. one JSON per line. One example from the dataset is given below in JSON format. Here, the *cleaned-text* field contains the processed text from the corresponding article link. Other fields are self-explanatory.  
  ```
  {
  	"id": "81822", 
  	"url": "https://www.vaartha.com/once-again-the-start-of-godari-boat-extraction-work/", 
  	"title": "లోకేష్ సతీమణి నారా బ్రాహ్మణి ఎన్నికల ప్రచారం…", 
  	"cleaned_text": "లోకేశ్ మద్దతుగా మంగళగిరిలో బ్రాహ్మణి ఎన్నికల ప్రచారం నిర్వహించారు. స్థానిక ఎమ్మెల్యే కాకపోయి నా ఇంత అభివృద్ధి చేస్తే..మంగళగిరి నుంచి ఎన్నికైతే ఇంకెంత చేస్తారో ఆలోచించాలని ప్రజల్ని కోరారు. రాబోయే ఐదేళ్లలో మరిన్ని సంస్థలు తీసుకొస్తామని చెప్పారు.మంత్రి నారా లోకేశ్ స్థానిక ఎమ్మెల్యే కానప్పటికీ మంగళగిరి నియోజకవర్గానికి ఇప్పటికే 42 సంస్థలను తీసుకొచ్చారని..వాటి ద్వారా 3500 మందికి ఉపాధి కలిగిందని ఆయన సతీమణి నారా బ్రాహ్మణి అన్నారు. నియోజకవర్గాన్ని అభివృద్ధి చేసేందుకు లోకేశ్ ప్రత్యేక మేనిఫెస్టోని ప్రకటించారని ఆమె చెప్పారు. స్థానిక సమస్యలను దృష్టిలో ఉంచుకుని దాన్ని రూపొందించారన్నారు. ముస్లిం మైనారిటీల స్వయం ఉపాధికి ప్రభుత్వమే నేరుగా రుణాలు ఇచ్చేలా చర్యలు తీసుకొంటామన్నారు. మేమంతా ఇక్కడే ఉంటున్నామని..మంగళగిరి నియోజకవర్గంలోనే ఇల్లు, ఓటు హక్కు ఉన్నాయని చెప్పారు. సమస్యలు చెప్పుకొనేందుకు కుప్పం ప్రజల్లాగే..మంగళగిరి ప్రజలకూ తమ ఇంటి తలుపులు ఎప్పుడూ తెరిచే ఉంటాయని బ్రాహ్మణి వ్యాఖ్యానించారు. లోకేశ్ను అత్యధిక మెజార్టీతో గెలిపించాలని ప్రజల్ని ఆమె కోరారు. ఎన్నికల ఖర్చుల నిమిత్తం ఓ వృద్ధురాలు బ్రాహ్మణికి రూ.500 విరాళంగా ఇచ్చారు. ఆ వృద్ధురాలికి బ్రాహ్మణి కృతజ్ఞతలు తెలిపారు.", 
  	"summary": "నారా లోకేష్ సతీమణి నారా బ్రాహ్మణి మంగళగిరిలో ఆయనకు మద్దతుగా ఎన్నికల ప్రచారం నిర్వహించారు. లోకేష్ స్థానిక ఎమ్మెల్యే కాకపోయినా మంగళగిరి నియోజకవర్గానికి 42 సంస్థలను తీసుకొచ్చి 3500 మందికి ఉపాధి కలిపించారు అని రాబోయే ఐదేళ్లలో మరిన్ని సంస్థలు తీసుకొస్తామని బ్రాహ్మణిచెప్పారు. ముస్లిం మైనారిటీలకు ప్రభుత్వమే నేరుగా రుణాలు ఇస్తుందని, లోకేష్ ను భారి మెజారిటీతో గెలిపించాలని ఆమె కోరారు.", 
  	"article_sentence_count": 13, 
  	"article_token_count": 144, 
  	"summary_token_count": 48, 
  	"title_token_count": 6, 
  	"compression": 66.67, 
  	"abstractivity": 29.17
  }
  
  ```

   * See [Data](data/tesum/)

  This dataset contains a total of **20329** article-summary pairs, making it the **largest** human-generated text summarization dataset publicly available.

## Filtering Scripts
  As mentioned in the paper, we have used multiple filters for Automatic Quality Control. Same filters were applied on existing datasets like XL-Sum and MassiveSum also. We are releasing the filteration scripts used by this work:
  * See [Filtering Scripts](filtering_scripts/)

## Benchmarks

Following are the Model Scores on TeSum test set, with the corresponding links for implementations used.

MODEL | CITATION | ROUGE-1 | ROUGE-2 | ROUGE-L | CODE
------|----------|---------|---------|---------|-------------
Pointer Generator | [See et al. 2017](https://nlp.stanford.edu/pubs/see2017get.pdf) | 39.37 | 22.72 | 32.15 | [Link](https://github.com/atulkum/pointer_summarizer)
MLE + RL-wo | [Paulus 2017](https://arxiv.org/pdf/1705.04304.pdf?ref=hackernoon.com) | 38.09 | 21.9 | 31.77 | [Link](https://github.com/rohithreddy024/Text-Summarizer-Pytorch) 
BertSumAbs | [Liu and Lapata 2019](https://arxiv.org/pdf/1908.08345.pdf?ref=hackernoon.com) | 26.49 | 12.55 | 19.6 | [Link](https://github.com/nlpyang/PreSumm)
mT5-small | [Xue et al. 2020](https://arxiv.org/pdf/2010.11934.pdf) | 37.42 | 20.82 | 30.88 | [Link](https://github.com/csebuetnlp/xl-sum)


Further, the parameter settings used is given below.

PARAMETERS | Pointer Generator | MLE+RL-wo | BertSumAbs | mT5
-----------|-------------------|-----------|------------|-------
Max source length | 400 | 400 | 512 | 512
Max target length | 100 | 100 | 200 | 256
Min target length | 35 | 35 | 50 | 30
Batch Size | 8 | 8 | 140 | 2
Epoch/Iterations | 100k iter | 100k iter | 50k iter | 10 epochs
Vocab Size | 50k | 50k | 28996 | 250112
Beam Size | 4 | 4 | 5 | 4
Learning Rate | 0.15 | 0.001 MLE <br> 0.0001 Others | lr_bert = 0.002 <br> lr_dec = 0.2 | 5e-4


## License
Contents of this repository are restricted to only non-commercial research purposes under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/). 
Copyright of the dataset contents belongs to the original copyright holders.


