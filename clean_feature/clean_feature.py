import numpy as np
from clean_data.clean import Clean
from clean_data.clean_time import CTime
from clean_text.guess.guess_by_dict import GuessByDict
from clean_text.text_analysis import TextAnalysis
from programmerUI.display import Display


class CleanJ:
    def __init__(self, store_df):
        self.store_df = store_df
        for name in store_df.dfs_names:
            setattr(self, name, store_df.get_df_by_name(name))

    def date_death_or_discharge(self):
        CTime.update_s_time_basic_multi_df([self.philippines, self.india_data, self.india_wiki, self.world],
                                           'date_death_or_discharge', False)
        Display.print_with_num_of_line("death_or_discharge_date", depth=3)

    def sex(self, sex_dict):
        for dataset in self.store_df.dfs:
            Clean.replace_value_by_comparison(dataset, "sex", sex_dict)

    def symptoms(self, symptoms_bag_words, symptoms_sentences_bag):
        text_analysis_dict = {"vietnam": ["symptoms_origin"],
                              "world": ["symptoms_origin"],
                              "philippines": ["Final Diagnosis", "symptoms_origin"]}

        for df_name, cols in text_analysis_dict.items():
            TextAnalysis.text_analysis(self.store_df.get_df_by_name(df_name), cols,
                                       "symptoms", GuessByDict(symptoms_bag_words,
                                                               symptoms_sentences_bag))

    def background_diseases(self, background_diseases_bag_words, background_diseases_sentences_bag,
                            mexico_background_diseases_cols):

        text_analysis_dict = {"vietnam": ["background_diseases_origin"],
                              "guatemala": ["background_diseases_origin"],
                              "world": ["symptoms_origin", "background_diseases_origin"],
                              "philippines":  ["Final Diagnosis", "background_diseases_origin"]}

        for df_name, cols in text_analysis_dict.items():
            TextAnalysis.text_analysis(self.store_df.get_df_by_name(df_name), cols,
                                       "background_diseases",
                                       GuessByDict(bag_words=background_diseases_bag_words,
                                                   bag_sentences=background_diseases_sentences_bag))

        # mexico
        self.mexico["background_diseases"] = ""
        for col in mexico_background_diseases_cols:
            self.mexico.loc[self.mexico[col] != 1, col] = ""
            self.mexico.loc[self.mexico[col] == 1, col] = col
            self.mexico["background_diseases"] = self.mexico["background_diseases"] + self.mexico[col]

        Clean.replace_empty_value_to_npnan([df for df in self.store_df.dfs if "background_diseases" in df.columns],
                                           "background_diseases")

    def background_diseases_binary_by_background_diseases(self):
        self.world["background_diseases_binary"] = np.nan
        for df in [self.world, self.philippines, self.guatemala, self.vietnam, self.mexico]:
            df["background_diseases_binary"] = df["background_diseases"].apply(lambda x: 1 if x == x else 0)
            Display.print_with_num_of_line("background_diseases -> background_diseases_binary")

        Clean.replace_value_by_comparison(self.world, "more_data_and_background_diseases_binary",
                                          {1: [1]}, name_output_col="background_diseases_binary")

        Clean.replace_value_by_comparison(self.usa, "background_diseases_binary",
                                          {1: ["Yes"], 0: ["No"], np.nan: ["Missing", "Unknown"]})