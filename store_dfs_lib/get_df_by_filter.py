import numpy as np
import pandas as pd


class FilterStoreDF:
    def __init__(self, store_dfs):
        self.dfs = store_dfs.dfs
        self.dfs_names = store_dfs.dfs_names
        self.df_of_presence_col_within_df = self.make_df_of_presence_col_within_df()

    def make_df_of_presence_col_within_df(self):
        cols_in_dfs = set(np.array([df.columns for df in self.dfs]).flatten())
        list_zero_size_num_dfs = np.zeros((len(self.dfs_names), len(cols_in_dfs)), dtype=np.int64)
        df_of_presence_col_within_df = pd.DataFrame(list_zero_size_num_dfs, columns=cols_in_dfs)

        for i in range(len(self.dfs_names)):
            df_of_presence_col_within_df.loc[i, list(self.dfs[i].columns)] = 1
        df_of_presence_col_within_df.index = self.dfs_names
        return df_of_presence_col_within_df

    def get_dfs_names_if_contain_col(self, col):
        try:
            ls_dfs = self.df_of_presence_col_within_df.index[self.df_of_presence_col_within_df[col] == 1]
            ls_dfs = list(ls_dfs)
        except KeyError:
            ls_dfs = []
        return ls_dfs

