from pipeline.pipeline_value.value_for_change_cols_in_dfs import change_cols_names_by_df, drop_cols_by_df


class Prepare:
    def __init__(self, dfs_store):
        self.dfs_store = dfs_store

    def change_name_cols(self, change_cols_names_by_df):
        for k in change_cols_names_by_df:
            self.dfs_store.get_df_by_name(k).rename(columns=change_cols_names_by_df[k], inplace=True)

    def drop_unnecessary_cols(self, drop_cols_by_df):
        for k in drop_cols_by_df:
            self.dfs_store.get_df_by_name(k).drop(drop_cols_by_df[k], axis=1, inplace=True)

    def add_origin(self):
        names_cols_add_origin = ["treatment", "symptoms", "severity_illness", "infection_place",
                                 "background_diseases", "infected_by"]
        cols = []
        for col in self.dfs_store.df_of_presence_col_within_df.columns:
            for name in names_cols_add_origin:
                if name in col:
                    cols.append(col)

        d = dict(zip(cols, ["origin_" + i for i in cols]))
        for df in self.dfs_store.dfs:
            df.rename(columns=d, inplace=True)

    def organize_cols(self):
        self.change_name_cols(change_cols_names_by_df)
        self.drop_unnecessary_cols(drop_cols_by_df)