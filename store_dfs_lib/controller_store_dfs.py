from store_dfs_lib.display_store_df import DisplayStoreDF


class ControllerStoreDFs:

    def __init__(self, store_df):
        self.store_df = store_df
        self.display_store_df = DisplayStoreDF(store_df)

    def remove(self):
        self.store_df.remove()

    def add(self):
        self.store_df.add()

    def get_df_by_name(self, df_name):
        return self.store_df.get_df_by_name(df_name)

    def print_df_by_name(self, df_name, num_rows):
        self.display_store_df.print_df_by_name(df_name, num_rowsnum_rows)
