from pipeline.pipeline_value.value_for_change_cols_in_dfs import change_cols_names_by_df, drop_cols_by_df


class Prepare:

    @staticmethod
    def add_origin(dfs_store):
        names_cols_add_origin = ["symptoms", 'treatment',  "severity_illness", "infection_place",
                                 "background_diseases", "infected_by"]
        dfs_store.print_cols_by_df()
        for col in names_cols_add_origin:
            rename_dict = dfs_store.get_dict_keys_names_dfs_values_cols_contain_x(col)
            for name_df in rename_dict:
                rename_dict[name_df] = dict(zip(rename_dict[name_df], ["origin_" + i for i in rename_dict[name_df]]))
            dfs_store.rename_dfs_cols(rename_dict)
        return dfs_store

    @staticmethod
    def organize_cols(dfs_store):
        dfs_store.rename_dfs_cols(change_cols_names_by_df)
        dfs_store.drop_cols_from_dfs(drop_cols_by_df)
        Prepare.add_origin(dfs_store)

