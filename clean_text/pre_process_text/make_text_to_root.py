import nltk
from clean_lib.clean import Clean
from unite_dfs_parts.unite_col import Unite
from clean_text.pre_process_text.abstract_pre_process_text import PreProcessText
from python_expansion_lib.python_expansion import Pexpansion


class ToRoot(PreProcessText):
    def __init__(self):
        super().__init__()

    def _make_text_to_root(self, col):
        ps = nltk.stem.SnowballStemmer('english')
        Clean.change_text_col_to_ls_words_col(self.df, col)
        self.df[col] = self.df[col].apply(lambda x:
                                                    Pexpansion.from_word_ls_to_roots_str(x, ps) if x == x else "")

    def process_text(self):
        self.build_process_col()
        Unite.unite_cols_separate_by_comma(self.df, ["process"] + self.input_cols)
        Clean.clean_text_col_from_punctuation(self.df, "process")
        self._make_text_to_root("process")
