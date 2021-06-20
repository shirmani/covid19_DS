import numpy as np
import pandas as pd
import itertools

from python_expansion_lib.python_expansion import Pexpansion


class FilterStoreDF:
    def __init__(self, dfs_store):
        self.dfs_store = dfs_store
        self.df_of_presence_col_within_df = self.make_df_of_presence_col_within_df()

    def make_df_of_presence_col_within_df(self):
        cols_in_dfs = Pexpansion.flatten_ls([list(df.columns) for df in self.dfs_store.dfs])
        cols_in_dfs = set(cols_in_dfs)
        list_zero_size_num_dfs = np.zeros((len(self.dfs_store.dfs_names), len(cols_in_dfs)), dtype=np.int64)
        df_of_presence_col_within_df = pd.DataFrame(list_zero_size_num_dfs, columns=list(cols_in_dfs))

        for i in range(len(self.dfs_store.dfs_names)):
            df_of_presence_col_within_df.loc[i, list(self.dfs_store.dfs[i].columns)] = 1
        df_of_presence_col_within_df.index = self.dfs_store.dfs_names
        return df_of_presence_col_within_df

    def get_dfs_names_if_contain_col(self, col):
        try:
            ls_dfs = self.df_of_presence_col_within_df.index[self.df_of_presence_col_within_df[col] == 1]
            ls_dfs = list(ls_dfs)
        except KeyError:
            ls_dfs = []
        return ls_dfs

