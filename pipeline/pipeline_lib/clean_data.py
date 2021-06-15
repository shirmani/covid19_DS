from pipeline.pipeline_lib.clean_feature import CleanJ
from pipeline.pipeline_value.value_for_clean_data import sex_dict, symptoms_bag_words, symptoms_sentences_bag, \
    background_diseases_bag_words, mexico_background_diseases_cols, background_diseases_sentences_bag, \
    world_treatment_bag_words, world_treatment_sentences_bag, change_cols_names_by_df, drop_cols_by_df


class CleanData:

    @staticmethod
    def clean_data(store_df, access_df_store):
        cleanJ = CleanJ(store_df)
        cleanJ.change_name_cols(change_cols_names_by_df)
        cleanJ.drop_unnecessary_cols(drop_cols_by_df)
        cleanJ.sex(sex_dict)
        access_df_store.print_col_values_by_dfs("sex")
        cleanJ.symptoms(symptoms_bag_words, symptoms_sentences_bag)
        access_df_store.print_col_values_by_dfs("symptoms")
        cleanJ.background_diseases(background_diseases_bag_words, background_diseases_sentences_bag,
                                   mexico_background_diseases_cols)
        access_df_store.print_col_values_by_dfs("background_diseases")
        cleanJ.background_diseases_binary_by_background_diseases()
        access_df_store.print_col_values_by_dfs("background_diseases_binary")
        cleanJ.treatment(world_treatment_bag_words, world_treatment_sentences_bag)
        access_df_store.print_col_values_by_dfs("treatment")
