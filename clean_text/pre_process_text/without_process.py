from unite_dfs_parts.unite_col import *
from clean_text.pre_process_text.abstract_pre_process_text import *


class NOPreProcess(PreProcessText):
    def __init__(self):
        super().__init__()

    def process_text(self):
        self.build_process_col()
        Unite.unite_cols_separate_by_comma(self.df, ["process"] + self.input_cols)
