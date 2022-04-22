LANGUAGES = {'xlsum': {'hi': 'hindi', 'te': 'telugu', 'mr': 'marathi', 'gu': 'gujarati'}, 'tesum': {'te': 'telugu'}}
LANGUAGES.update({'massivesum': {'hi': 'hin', 'te': 'tel', 'mr': 'mar', 'gu': 'guj'}})


class Config:
    minSentCount = 4
    minArticleLength = 40
    minSummaryLength = 10
    minCompression = 50
    maxCompression = 80
    minAbstractivity = 10
    maxAbstractivity = 80

    file_exts = {'xlsum': "_total.jsonl", 'massivesum': ".all.jsonl", 'tesum': "_tesum_all.jsonl"}
    msfiles = {'hi': 'Hindi', 'te': 'Telugu', 'mr': 'Marathi', 'gu': 'Gujarati'}

    def __init__(self, source='./', dataset='xlsum', lang='te', filetype='.jsonl'):
        self.source = source
        self.dataset = dataset
        self.lang = lang
        self.filetype = filetype

        self.dataset_dir = {'massivesum': self.source + 'massivesum/', 'xlsum': self.source + 'xlsum/%s_XLSum_v2.0/'%LANGUAGES[self.dataset][self.lang]}
        self.dataset_dir.update({'tesum': self.source + 'tesum/'})

        if self.filetype == '.jsonl':
            self.datafile = self.dataset_dir[self.dataset] + LANGUAGES[self.dataset][self.lang] + self.file_exts[self.dataset]
        else:
            self.datafile = self.dataset_dir[self.dataset] + self.msfiles[self.lang] + "_filtered.jsonl.gz"

        self.save_dir = {'xlsum': './excluded_IDs/xlsum/%s_XLSum_v2.0/'%LANGUAGES[self.dataset][self.lang] + self.lang + "_", 'massivesum': './excluded_IDs/massivesum/' + self.lang + "_"}
        self.filter_dir = self.dataset_dir[self.dataset] + self.lang + "_"

    def set_dataset(self, dataset_name):
        self.dataset = dataset_name

    def set_language(self, lang):
        self.lang = lang
    
    def set_filetype(self, ftype):
        self.filetype = ftype
    
    def set_dataset_path(self, data_path):
        self.source = data_path
