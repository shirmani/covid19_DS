import numpy as np
import pandas as pd
from clean.clean import Clean
from disply_code_clear.display import Display
from pipeline.pipeline_lib.clean_feature.abstract_clean_feature import CleanJAbstract


class InferJ(CleanJAbstract):
    def __init__(self, dfs_store):
        super().__init__(dfs_store)
        for name in dfs_store.dfs_names:
            setattr(self, name, dfs_store.get_df_by_name(name))

    def ever_icu_by_treatment(self):
        names_dfs = self.dfs_store.get_dfs_names_if_contain_col("treatment")
        for name_df in names_dfs:
            Clean.replace_value_by_comparison(self.dfs_store.get_df_by_name(name_df), "treatment",
                                              {0: ["home isolation", "clinic"]}, name_output_col="ever_icu")

    def treatment_by_ever_icu_and_intubated(self):
        for col in ["ever_intubated", "ever_icu"]:
            dfs_ever_intubated = self.dfs_store.get_dfs_names_if_contain_col(col)
            for name_df in dfs_ever_intubated:
                Clean.replace_value_by_comparison(self.dfs_store.get_df_by_name(name_df),
                                                  col, {"hospitalized": [1]},
                                                  name_output_col="treatment")

    def severity_illness_by_deceased_or_released_date(self):
        ls_deceased_date = self.dfs_store.get_dfs_names_if_contain_col("deceased_date")
        ls_released_date = self.dfs_store.get_dfs_names_if_contain_col("released_date")

        self.dfs_store.add_col_to_dfs(ls_deceased_date + ls_released_date, "severity_illness1", "")

        for name_df in ls_deceased_date:
            self.dfs_store.get_df_by_name(name_df).loc[self.dfs_store.get_df_by_name(name_df).deceased_date.notnull(),
                                                      'severity_illness1'] = "deceased"
            Display.print_with_num_of_line("deceased_date -> severity_illness1")

        for name_df in ls_released_date:
            self.dfs_store.get_df_by_name(name_df).loc[self.dfs_store.get_df_by_name(name_df).released_date.notnull(),
                                                 'severity_illness1'] += ",cured"
            Display.print_with_num_of_line("released_date -> severity_illness1")


    def background_diseases_binary_by_background_diseases(self):
        self.world["background_diseases_binary"] = np.nan
        for df in [self.dfs_store.get_dfs_names_if_contain_col("background_diseases")]:
            self.dfs_store.get_df_by_name(df)["background_diseases_binary"] = \
                self.dfs_store.get_df_by_name(df)["background_diseases"].apply(lambda x: 1 if x == x else 0)

            Display.print_with_num_of_line("background_diseases -> background_diseases_binary")

        for name_df, col in \
                self.dfs_store.dict_keys_names_dfs_values_cols_contain_x("background_diseases_binary").items():
            Clean.replace_value_by_comparison(self.dfs_store.get_df_by_name(name_df),
                                             col, {1: [1, "Yes"],
                                                   0: [0, "No"]}, name_output_col="background_diseases_binary")

        # Clean.replace_value_by_comparison(self.usa, "background_diseases_binary",
        #                                   {1: ["Yes"], 0: ["No"], np.nan: ["Missing", "Unknown"]})

