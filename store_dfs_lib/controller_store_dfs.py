from store_dfs_lib.display_store_df import DisplayStoreDF
from store_dfs_lib.get_df_by_filter import FilterStoreDF


class ControllerStoreDFs:

    def __init__(self, dfs_store):
        self.store_df = dfs_store
        self.dfs = dfs_store.dfs
        self.dfs_names = dfs_store.dfs_names

        self.display_store_df = DisplayStoreDF(dfs_store)
        self.filter_store = FilterStoreDF(dfs_store)
        self.df_of_presence_col_within_df = self.filter_store.df_of_presence_col_within_df

    def remove(self, df_names):
        self.store_df.remove(df_names)

    def add(self, df_name, df):
        self.store_df.add(df_name, df)

    def get_df_by_name(self, df_name):
        return self.store_df.get_df_by_name(df_name)

    def add_col_to_dfs(self, ls_names_dfs, name_col, initial_value):
        self.store_df.add_col_to_dfs(ls_names_dfs, name_col, initial_value)

    # filter
    def get_dfs_names_if_contain_col(self, col):
        return self.filter_store.get_dfs_names_if_contain_col(col)

    def get_dict_keys_names_dfs_values_cols_contain_x(self, x):
        return self.filter_store.get_dict_keys_names_dfs_values_cols_contain_x(x)

    # display
    def print_df_by_name(self, df_name, num_rows):
        self.display_store_df.print_df_by_name(df_name, num_rows)

    def print_shape_dfs(self):
        self.display_store_df.print_shape_dfs()

    def print_cols_by_df(self):
        self.display_store_df.print_cols_by_df()

    def print_col_values_by_dfs(self, col):
        self.display_store_df.print_col_values_by_dfs(col)

    def print_cols_values_by_dfs(self):
        self.display_store_df.print_cols_values_by_dfs()

    # filter + store
    def get_ls_of_dfs_that_contain_col(self, col):
        names = self.get_dfs_names_if_contain_col(col)
        return [self.get_df_by_name(name) for name in names]


