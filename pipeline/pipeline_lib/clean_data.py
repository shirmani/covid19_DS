from pipeline.pipeline_lib.clean_feature import CleanJ
from pipeline.pipeline_value.value_for_clean_data import sex_dict, symptoms_bag_words, symptoms_sentences_bag, \
    background_diseases_bag_words, mexico_background_diseases_cols, background_diseases_sentences_bag, \
    world_treatment_bag_words, world_treatment_sentences_bag


class CleanData:

    @staticmethod
    def clean_data(store_df):
        store_df.print_col_values_by_dfs("treatment_current_intubated")
        store_df.print_col_values_by_dfs("treatment_ever_icu")
        store_df.print_col_values_by_dfs("link_sicks")

        cleanJ = CleanJ(store_df)
        cleanJ.sex(sex_dict)
        store_df.print_col_values_by_dfs("sex")
        cleanJ.symptoms(symptoms_bag_words, symptoms_sentences_bag)
        store_df.print_col_values_by_dfs("symptoms")
        cleanJ.background_diseases(background_diseases_bag_words, background_diseases_sentences_bag,
                                   mexico_background_diseases_cols)
        store_df.print_col_values_by_dfs("background_diseases")
        cleanJ.background_diseases_binary_by_background_diseases()
        store_df.print_col_values_by_dfs("background_diseases_binary")

        cleanJ.ever_intubated()
        store_df.print_col_values_by_dfs("ever_intubated")
        cleanJ.ever_icu()
        store_df.print_col_values_by_dfs("ever_icu")

        cleanJ.treatment_by_ever_icu()
        cleanJ.treatment_by_ever_intubated()
        cleanJ.treatment_by_name_of_hospital()
        store_df.print_col_values_by_dfs("treatment")
        cleanJ.treatment(world_treatment_bag_words, world_treatment_sentences_bag)
        store_df.print_col_values_by_dfs("treatment")
