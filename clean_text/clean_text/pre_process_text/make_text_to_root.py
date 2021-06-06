import nltk
from clean_data.unite_col import *
from python_expansion import *
from clean_text.pre_process_text.pre_process_text import *


class ToRoot(PreProcessText):
    def __init__(self):
        super().__init__()

    def _make_text_to_root(self, col):
        ps = nltk.stem.SnowballStemmer('english')
        Clean.change_words_col_to_ls_word_col(self.df, col)
        self.df[col] = self.df[col].apply(lambda x:
                                                    Pexpansion.from_word_ls_to_roots_str(x, ps) if x == x else "")

    def process_text(self):
        self.build_process_col()
        Unite.unite_cols_separate_by_comma(self.df, ["process"] + self.input_cols , delete=False)
        Clean.clean_text_col_from_punctuation(self.df, "process")
        self._make_text_to_root("process")
