from store_dfs_lib.display_store_df import DisplayStoreDF
from store_dfs_lib.get_df_by_filter import FilterStoreDF


class ControllerStoreDFs:

    def __init__(self, store_df):
        self.store_df = store_df
        self.display_store_df = DisplayStoreDF(store_df)
        self.filter_store = FilterStoreDF(store_df)

    def remove(self):
        self.store_df.remove()

    def add(self):
        self.store_df.add()

    def get_df_by_name(self, df_name):
        return self.store_df.get_df_by_name(df_name)

    # filter
    def get_dfs_names_if_contain_col(self, col):
        return self.filter_store.get_dfs_names_if_contain_col(col)

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
        dfs_names = self.get_dfs_names_if_contain_col(col)
        return [self.get_df_by_name(i) for i in dfs_names]


