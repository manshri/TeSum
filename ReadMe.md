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
     "id": "1713",
     "url": "https://www.prajasakti.com/WEBSECTION/International/page55/rendo-roju-mutapadd-bali-airport",
     "title": "ముఖ్యమంత్రి కరువును పట్టించుకోవడం లేదు\n", 
     "cleaned_text": "మాజీ ముఖ్యమంత్రి వైఎస్ రాజశేఖర్రెడ్డిపై అసెంబ్లీలో ముఖ్యమంత్రి కేసీఆర్ చేసిన వ్యాఖ్యలను కాంగ్రెస్ ఎమ్మెల్సీ పొంగులేటి సుధాకర్రెడ్డి తప్పుపట్టారు. శుక్రవారం సీఎల్పీ కార్యాలయంలో మీడియాతో మాట్లాడిన ఆయన సీఎం కేసీఆర్ గురువారం అసెంబ్లీలో చెప్పిన ప్రాజెక్టులన్నీ కాంగ్రెస్ హయాంలో ప్రారంభించినవేనని స్పష్టం చేశారు. కోటి ఎకరాలలో నీరు అందించడం కాంగ్రెస్ చేపట్టిన 60 లక్షల ఎకరాల ప్రాజెక్టుల వల్లే అని చెప్పారు. పట్టిసీమ ఎలా కడతారని గతంలో ఆరోపించిన కేసీఆర్ ఇప్పుడు ఆ ప్రాజెక్టు సరైన నిర్ణయం అని అనడం వెనక మతలబు ఏంటోనని అనుమానం వ్యక్తం చేశారు. ఓటుకు కోట్లు కేసులో చంద్రబాబు నాయుడును ఎవరు కాపాడలేరని వ్యాఖ్యానించిన ముఖ్యమంత్రి ఇప్పుడు ఆకేసు గురించి ఎందుకు మాట్లాడటం లేదని ప్రశ్నించారు. రాష్ట్రంలో తీవ్ర కరువు పరిస్థితులు తీవ్రంగా ఉన్నాయని, ముఖ్యమంత్రి మాత్రం దానిపై అసలు స్పందించడం లేదని విమర్శించారు. కరువు పరిస్థితిపై ప్రభుత్వ చర్యలపై హైకోర్టు ఇచ్చిన ఆదేశాలను సైతం దిక్కరిస్తున్నారని మండిపడ్డారు.",
     "summary": "పొంగులేటి సుధాకర్రెడ్డి కార్యాలయంలో మాట్లాడుతూ, కేసీఆర్ అసెంబ్లీలో చెప్పిన ప్రాజెక్టులన్నీ కాంగ్రెస్ హయాంలో ప్రారంభించినవేనని, కోటి ఎకరాలలో నీరు అందించడం కాంగ్రెస్ చేపట్టిన 60 లక్షల ఎకరాల ప్రాజెక్టుల వలనేనని, పట్టిసీమ వెనక మతలబు ఏదో ఉందని అన్నారు. కరువు పరిస్థితిపై ప్రభుత్వ చర్యలపై హైకోర్టు ఇచ్చిన ఆదేశాలను సైతం దిక్కరిస్తున్నారని మండిపడ్డారు.", 
     "sent_count": 7, 
     "article_len": 110, 
     "summary_len": 43, 
     "title_len": 4, 
     "compression": 60.91, 
     "abstractivity": 16.28
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
Pointer Generator | [See et al. 2017](https://nlp.stanford.edu/pubs/see2017get.pdf) | 29.39 | 10.48 | 29.02 | [Link](https://github.com/atulkum/pointer_summarizer)
MLE + RL-wo | [Paulus 2017](https://arxiv.org/pdf/1705.04304.pdf?ref=hackernoon.com) | 39.64 | 24.13 | 39.37 | [Link](https://github.com/rohithreddy024/Text-Summarizer-Pytorch) 
BertSumAbs | [Liu and Lapata 2019](https://arxiv.org/pdf/1908.08345.pdf?ref=hackernoon.com) | 31.31 | 18.49 | 25.05 | [Link](https://github.com/nlpyang/PreSumm)
mT5-small | [Xue et al. 2020](https://arxiv.org/pdf/2010.11934.pdf) | 40.53 | 24.61 | 33.79 | [Link](https://github.com/csebuetnlp/xl-sum)


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


