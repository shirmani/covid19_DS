from clean_lib.clean import Clean
from clean_lib.clean_date import CDate
from pipeline.pipeline_lib.clean_feature.abstract_clean_feature import CleanJAbstract
from python_expansion_lib.python_expansion import Pexpansion


class CleanDateJ(CleanJAbstract):
    def __init__(self, dfs_store):
        super().__init__(dfs_store)
        for name in dfs_store.dfs_names:
            setattr(self, name, dfs_store.get_df_by_name(name))

    def prepare_vars(self, type_date_by_df):
        col_of_date = self.dfs_store.get_dict_keys_names_dfs_values_cols_contain_x("date")
        type_date_by_df = Pexpansion.upside_down_dictionary(type_date_by_df)
        return col_of_date, type_date_by_df

    def check_different_type_date(self, type_date_by_df, different_type_date_dict, df_name, col):
        if df_name in different_type_date_dict.keys():
            if col in different_type_date_dict[df_name].keys():
                return different_type_date_dict[df_name][col]
        return type_date_by_df[df_name][0]

    def handel_vietnam_return_date(self):
        def find_date(x):
            x = [i for i in x if "/" in i]
            return "-".join(x)

        Clean.replace_tags_in_value(self.vietnam, "return_date", {" ": ["(", ")"]})
        self.vietnam["return_date"] = self.vietnam["return_date"].str.split(pat=" ")
        self.vietnam["return_date"] = self.vietnam["return_date"].apply(lambda x: find_date(x) if x == x else x)

    def clean_date_cols(self, type_date_by_df, different_type_date_by_col):
        col_of_date, type_date_by_df = self.prepare_vars(type_date_by_df)
        for df_name in col_of_date.keys():
            for col in col_of_date[df_name]:
                format = self.check_different_type_date(type_date_by_df, different_type_date_by_col, df_name, col)
                CDate.clean_date_col(self.dfs_store.get_df_by_name(df_name), col,
                                     format=format)
