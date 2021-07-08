import numpy as np
from clean_lib.clean import Clean
from clean_text.guess.guess_by_dict import GuessByDict
from clean_text.organize_col.category_col import CategoryCol
from clean_text.text_analysis import TextAnalysis
from pipeline.pipeline_lib.clean_feature.abstract_clean_feature import CleanJAbstract
from pipeline.pipeline_value.value_for_clean_data import world_severity_illness_bag_words, \
    world_severity_illness_sentences_bag
from python_expansion_lib.python_expansion import Pexpansion
from unite_dfs_parts.unite_col import Unite


class CleanJ(CleanJAbstract):
    def __init__(self, dfs_store):
        super().__init__(dfs_store)
        for name in dfs_store.dfs_names:
            setattr(self, name, dfs_store.get_df_by_name(name))

    def sex(self, sex_dict):
        for dataset in self.dfs_store.dfs:
            Clean.replace_value_by_comparison(dataset, "sex", sex_dict)

    def symptoms(self, symptoms_bag_words, symptoms_sentences_bag):
        text_analysis_dict = self.dfs_store.get_dict_keys_names_dfs_values_cols_contain_x("origin_symptoms")
        for df_name, cols in text_analysis_dict.items():
            TextAnalysis.text_analysis(self.dfs_store.get_df_by_name(df_name), cols,
                                       "symptoms", GuessByDict(symptoms_bag_words,
                                                               symptoms_sentences_bag))

    def background_diseases(self, background_diseases_bag_words, background_diseases_sentences_bag,
                            mexico_background_diseases_cols):
        text_analysis_dict = self.dfs_store.get_dict_keys_names_dfs_values_cols_contain_x("origin_background_diseases")
        text_analysis_dict["world"].append("origin_symptoms")

        for df_name, cols in text_analysis_dict.items():
            TextAnalysis.text_analysis(self.dfs_store.get_df_by_name(df_name), cols,
                                       "background_diseases",
                                       GuessByDict(bag_words=background_diseases_bag_words,
                                                   bag_sentences=background_diseases_sentences_bag))

        # mexico
        self.mexico["background_diseases"] = ""
        for col in mexico_background_diseases_cols:
            self.mexico.loc[self.mexico[col] != 1, col] = ""
            self.mexico.loc[self.mexico[col] == 1, col] = col
            self.mexico["background_diseases"] = self.mexico["background_diseases"] + self.mexico[col]

        names_dfs = self.dfs_store.get_dfs_names_if_contain_col("background_diseases")
        for name_df in names_dfs:
            Clean.replace_all_null_to_x(self.dfs_store.get_df_by_name(name_df),
                                        "background_diseases",  np.nan)

    def ever_intubated(self, binary_dict):
        d = {"ever_intubated": self.dfs_store.get_dfs_names_if_contain_col("ever_intubated"),
             "current_intubated": self.dfs_store.get_dfs_names_if_contain_col("current_intubated")}

        for col, ls_df in d.items():
            for name_df in ls_df:
                Clean.replace_value_by_comparison(self.dfs_store.get_df_by_name(name_df),
                                                  col, binary_dict, name_output_col="ever_intubated")

        # TextAnalysis.text_analysis(self.world, ["symptoms_origin", "origin_severity_illness"],
        #                            "severity_illness4",
        #                            GuessByDict(bag_words={},
        #                                        bag_sentences=world_severity_illness_sentences_bag),
        #                            col_type=CategoryCol(priorities_dict={"asymptomatic": 0, "good": 1,
        #                                                                  "critical": 2, "deceased": 3,
        #                                                                  "cured": 3}))

        #  "origin_severity_illness": intensive care unit,  hospital , released from quarantine

    def ever_icu(self, binary_dict):
        d = {"ever_icu": self.dfs_store.get_dfs_names_if_contain_col("ever_icu"),
             "current_icu": self.dfs_store.get_dfs_names_if_contain_col("current_icu")}

        for col, ls_df in d.items():
            for name_df in ls_df:
                print(name_df + " ever icu")
                Clean.replace_value_by_comparison(self.dfs_store.get_df_by_name(name_df),
                                                  col, binary_dict, name_output_col="ever_icu")

        Clean.replace_value_by_comparison(self.colombia, "origin_treatment",
                                          {1: ["Hospital Uci"]}, name_output_col="ever_icu")

    def treatment(self, world_treatment_bag_words, world_treatment_sentences_bag):
        for df in self.dfs_store.get_dfs_names_if_contain_col("origin_treatment"):
            Clean.replace_value_by_comparison(self.dfs_store.get_df_by_name(df),
                                              "origin_treatment",
                                              {"hospitalized": ["released0", "hospital",
                                                                "Hospital Uci", "Hospital", 2],
                                               "home isolation": ["Casa", 1]},
                                              name_output_col="treatment")

        # usa
        Clean.replace_value_by_comparison(self.usa, "ever_hospitalized",
                                          {"hospitalized": ["Yes"],
                                           "home isolation": ["No"]},
                                          name_output_col='treatment')

        # world
        TextAnalysis.text_analysis(self.world, ["origin_severity_illness", "origin_symptoms"], "treatment",
                                   guess_type=GuessByDict(bag_words=world_treatment_bag_words,
                                                          bag_sentences=world_treatment_sentences_bag),
                                   col_type=CategoryCol({"hospitalized": 2, "clinic": 1, "home isolation": 0}))

    def treatment_by_origin_severity_illness(self):
        for df in self.dfs_store.get_dfs_names_if_contain_col("origin_severity_illness"):
            Clean.replace_value_by_comparison(self.dfs_store.get_df_by_name(df), "origin_severity_illness",
                                              {"hospitalized": ["Hospitalized", "Hospitalised"]},
                                              name_output_col="treatment")

    def treatment_by_name_of_hospital(self):
        for name_df in self.dfs_store.get_dfs_names_if_contain_col("name_of_hospital"):
            Clean.replace_value_by_comparison(self.dfs_store.get_df_by_name(name_df), "name_of_hospital",
                                              {np.nan: ["For validation", "?"]})

            self.dfs_store.get_df_by_name(name_df).loc[
                self.dfs_store.get_df_by_name(name_df)["name_of_hospital"].notnull(), "treatment"] = "hospitalized"

    def severity_illness_over_time(self, severity_illness_dict):
        self.dfs_store.add_col_to_dfs(self.dfs_store.dfs_names, "severity_illness_over_time", "")

        d_a = self.dfs_store.get_dict_keys_names_dfs_values_cols_contain_x("severity_illness")
        for name_df in d_a:
            for col in d_a[name_df]:
                self.dfs_store.get_df_by_name(name_df)["a"] = ""
                self.dfs_store.get_df_by_name(name_df)["a"] = self.dfs_store.get_df_by_name(name_df)[
                col].apply(lambda x: Pexpansion.get_key_from_dict_by_value(severity_illness_dict, x))
                Unite.unite_cols(self.dfs_store.get_df_by_name(name_df), ["severity_illness_over_time", "a"])


        d_b = self.dfs_store.get_dfs_names_if_contain_col("death_yn")
        for name_df in d_b:
            self.dfs_store.get_df_by_name(name_df)["a"] = ""
            Clean.replace_value_by_comparison(self.dfs_store.get_df_by_name(name_df)
                                              , "death_yn", {"deceased": [True, "Yes"]},
                                              name_output_col='a')
            Unite.unite_cols(self.dfs_store.get_df_by_name(name_df), ["severity_illness_over_time", "a"])


        TextAnalysis.text_analysis(self.world, ["origin_symptoms", "origin_severity_illness"], "a",
                                   GuessByDict(bag_words=world_severity_illness_bag_words,
                                               bag_sentences=world_severity_illness_sentences_bag),
                                   col_type=CategoryCol(priorities_dict={"asymptomatic": 0, "good": 1,
                                                                         "critical": 2, "deceased": 3,
                                                                         "cured": 3}))
        Unite.unite_cols(self.world, ["severity_illness_over_time", "a"])


    def severity_illness_over_time_by_origin_treatment(self):
        Clean.replace_value_by_comparison(self.colombia, "origin_treatment", {"critical": ["Hospital Uci"],
                                                                         "deceased": ["Fallecido"],
                                                                         "cured": ["Recuperado"],
                                                                         "good": ["Casa", "Hospital"]},
                                          name_output_col='a')
        Unite.unite_cols(self.colombia, ["severity_illness_over_time", "a"])
