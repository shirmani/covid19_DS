import pandas as pd
from disply_code_clear.display import Display


class DisplayStoreDF:
    def __init__(self, dfs_store):
        self.dfs_store = dfs_store

    def print_df_by_name(self, df_name, num_rows=5):
        df = self.dfs_store.get_df_by_name(df_name)
        pd.set_option('expand_frame_repr', True,
                      "display.max_rows", num_rows,
                      "display.max_columns", len(df),
                      'display.width', len(df) * 50)
        print(df)
        pd.reset_option("display.max_rows")
        pd.reset_option("display.max_columns")
        pd.reset_option('display.width')

    def print_all_dfs(self):
        for df_name in self.dfs_store.dfs_names:
            print(df_name)
            self.print_df_by_name(df_name)
            print("-------------------------------")

    def print_col_values_by_dfs(self, col):
        Display.buffer_with_num_of_line()
        print("--" + col + "--")
        for i in range(len(self.dfs_store.dfs)):
            print("\n" + self.dfs_store.dfs_names[i])
            if col in self.dfs_store.dfs[i].columns:
                print(self.dfs_store.dfs[i][col].value_counts())

    def print_shape_dfs(self):
        Display.buffer_with_num_of_line()
        print("Shape of Dfs")
        shapes = []
        for i in range(len(self.dfs_store.dfs_names)):
            print(self.dfs_store.dfs_names[i], self.dfs_store.dfs[i].shape)
            shapes.append(self.dfs_store.dfs[i].shape[0])
        print("\nsum " + str(sum(shapes)))

    def print_cols_by_df(self):
        Display.buffer_with_num_of_line()
        for i in range(len(self.dfs_store.dfs_names)):
            print(self.dfs_store.dfs_names[i] + " " + str(self.dfs_store.dfs[i].columns))
            print()

    def print_cols_values_by_dfs(self):
        Display.buffer_with_num_of_line()
        for i in range(len(self.dfs_store.dfs_names)):
            for col in self.dfs_store.dfs[i].columns:
                print(self.dfs_store.dfs_names[i] + " " + col)
                print(self.dfs_store.dfs[i][col].value_counts())
                print()
