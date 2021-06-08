from clean_data.clean import Clean
from clean_data.clean_time import CTime
from clean_text.guess.guess_by_dict import GuessByDict
from clean_text.text_analysis import TextAnalysis
from programmerUI.display import Display


class CleanJ:
    @staticmethod
    def date_death_or_discharge(**kwargs):
        CTime.update_s_time_basic_multi_df([philippines, india_data, india_wiki, world],
                                           'date_death_or_discharge', False)
        Display.print_with_num_of_line("death_or_discharge_date")

    @staticmethod
    def sex(access_df_store, sex_dict):
        for dataset in access_df_store.dfs:
            Clean.replace_value_by_comparison(dataset, "sex", sex_dict)

    @staticmethod
    def symptoms(symptoms_bag_words, symptoms_sentences_bag, **kwargs):
        for df in [vietnam, world]:
            TextAnalysis.text_analysis(df, "symptoms_origin", "symptoms",
                                       GuessByDict(symptoms_bag_words,
                                                   symptoms_sentences_bag))

        TextAnalysis.text_analysis(philippines, ["Final Diagnosis", "symptoms_origin"],
                                   "symptoms",
                                   GuessByDict(bag_words=symptoms_bag_words,
                                               bag_sentences=symptoms_sentences_bag))