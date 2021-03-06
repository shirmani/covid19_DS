from python_expansion_lib.python_expansion import Pexpansion


class StoreDF:
    def __init__(self, dfs, dfs_names):
        self.dfs = dfs
        self.dfs_names = dfs_names
    
    def remove(self, df_names):
        df_names = Pexpansion.if_x_not_ls_make_x_ls(df_names)
        for df_name in df_names:
            index_df = self.dfs_names.index(df_name)
            del self.dfs_names[index_df]
            del self.dfs[index_df]

    def add(self, df_name, df):
        self.dfs_names.append(df_name)
        self.dfs.append(df)

    def get_df_by_name(self, df_name):
        index_df = self.dfs_names.index(df_name)
        return self.dfs[index_df]

    def add_col_to_dfs(self, ls_names_dfs, name_col, initial_value):
        for name in ls_names_dfs:
            self.get_df_by_name(name)[name_col] = initial_value

    def rename_dfs_cols(self, change_name_dict):
        for df_name in change_name_dict:
            self.get_df_by_name(df_name).rename(columns=change_name_dict[df_name], inplace=True)

    def drop_cols_from_dfs(self, drop_cols_dict):
        try:
            for df_name in drop_cols_dict:
                self.get_df_by_name(df_name).drop(drop_cols_dict[df_name], axis=1, inplace=True)
        except KeyError as e: print("KeyError:drop_cols_from_dfs: " + df_name + str(e).strip('"'))
