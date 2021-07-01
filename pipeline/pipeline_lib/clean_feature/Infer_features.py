import numpy as np
import pandas as pd
from clean_lib.clean import Clean
from clean_text.guess.guess_by_dict import GuessByDict
from clean_text.organize_col.category_col import CategoryCol
from clean_text.pre_process_text.without_process import NOPreProcess
from clean_text.text_analysis import TextAnalysis
from disply_code_clear.display import Display
from pipeline.pipeline_lib.clean_feature.abstract_clean_feature import CleanJAbstract
from pipeline.pipeline_value.value_for_clean_data import severity_illness_from_symptoms_by_WHO
from unite_dfs_parts.unite_col import Unite


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

    def severity_illness_over_time_by_deceased_or_released_date(self):
        ls_deceased_date = self.dfs_store.get_dfs_names_if_contain_col("deceased_date")
        ls_released_date = self.dfs_store.get_dfs_names_if_contain_col("released_date")

        self.dfs_store.add_col_to_dfs(ls_deceased_date + ls_released_date, "a", "")

        for name_df in ls_deceased_date:
            self.dfs_store.get_df_by_name(name_df).loc[self.dfs_store.get_df_by_name(name_df).deceased_date.notnull(),
                                                      'a'] = "deceased"
            Unite.unite_cols(self.dfs_store.get_df_by_name(name_df), ["severity_illness_over_time", "a"])
            Display.print_with_num_of_line("deceased_date ->severity_illness_over_time")

        for name_df in ls_released_date:
            self.dfs_store.get_df_by_name(name_df).loc[self.dfs_store.get_df_by_name(name_df).released_date.notnull(),
                                                 'b'] += ",cured"
            Unite.unite_cols(self.dfs_store.get_df_by_name(name_df), ["severity_illness_over_time", "b"])
            Display.print_with_num_of_line("released_date ->severity_illness_over_time")

    def severity_illness_over_time_by_ever_icu_and_intubated(self):
        for col in ["ever_intubated", "ever_icu"]:
            dfs_ever_intubated = self.dfs_store.get_dfs_names_if_contain_col(col)
            for name_df in dfs_ever_intubated:
                Clean.replace_value_by_comparison(self.dfs_store.get_df_by_name(name_df),
                                                  col, {"critical": [1]},
                                                  name_output_col="a")
                print( name_df)
                print(self.dfs_store.get_df_by_name(name_df)["a"].value_counts())
                Unite.unite_cols(self.dfs_store.get_df_by_name(name_df), ["severity_illness_over_time", "a"])

    def severity_illness_over_time_by_symptoms(self):
        for name_df in self.dfs_store.get_dfs_names_if_contain_col("symptoms"):
            TextAnalysis.text_analysis(name_df, "symptoms", "a",
                                       pre_process_text=NOPreProcess(),
                                       guess_type=GuessByDict(bag_words=severity_illness_from_symptoms_by_WHO,
                                                              bag_sentences={}),
                                       col_type=CategoryCol(priorities_dict={"asymptomatic": 0, "good": 1,
                                                                             "critical": 2, "deceased": 3,
                                                                             "cured": 3}))
            Unite.unite_cols(self.dfs_store.get_df_by_name(name_df), ["severity_illness_over_time", "a"])

    def background_diseases_binary_by_background_diseases(self):
        for df_name in self.dfs_store.get_dfs_names_if_contain_col("background_diseases"):
            self.dfs_store.get_df_by_name(df_name)["background_diseases_binary"] = \
                self.dfs_store.get_df_by_name(df_name)["background_diseases"].apply(lambda x: 1 if x == x else 0)

            Display.print_with_num_of_line("background_diseases -> background_diseases_binary")

        d = self.dfs_store.get_dict_keys_names_dfs_values_cols_contain_x("background_diseases_binary")
        for name_df in d:
            for col in d[name_df]:
                Clean.replace_value_by_comparison(self.dfs_store.get_df_by_name(name_df),
                                                  col, {1: [1, "Yes"],
                                                  0: [0, "No"]}, name_output_col="background_diseases_binary")



