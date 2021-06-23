from pipeline.pipeline_lib.clean_feature.clean_feature import CleanJ
from pipeline.pipeline_value.value_for_clean_data import sex_dict, symptoms_bag_words, symptoms_sentences_bag, \
    background_diseases_bag_words, mexico_background_diseases_cols, background_diseases_sentences_bag, \
    world_treatment_bag_words, world_treatment_sentences_bag, binary_dict


class CleanData:
    # store_df.print_col_values_by_dfs("sex")
    @staticmethod
    def clean_data(store_df):
        cleanJ = CleanJ(store_df)
        # cleanJ.sex(sex_dict)
        # cleanJ.symptoms(symptoms_bag_words, symptoms_sentences_bag)
        # cleanJ.background_diseases(background_diseases_bag_words, background_diseases_sentences_bag,
        #                            mexico_background_diseases_cols)
        cleanJ.ever_intubated(binary_dict)
        store_df.print_col_values_by_dfs("ever_intubated")
        # cleanJ.ever_icu(binary_dict)
        # cleanJ.treatment(world_treatment_bag_words, world_treatment_sentences_bag)
        # cleanJ.treatment_by_name_of_hospital()
        # store_df.print_col_values_by_dfs("treatment")
