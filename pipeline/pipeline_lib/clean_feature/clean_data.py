from pipeline.pipeline_lib.clean_feature.Infer_features import InferJ
from pipeline.pipeline_lib.clean_feature.clean_feature import CleanJ
from pipeline.pipeline_value.value_for_clean_data import sex_dict, symptoms_bag_words, symptoms_sentences_bag, \
    background_diseases_bag_words, mexico_background_diseases_cols, background_diseases_sentences_bag, \
    world_treatment_bag_words, world_treatment_sentences_bag, binary_dict, severity_illness_dict
import time

class CleanData:

    @staticmethod
    def clean_feature(store_df, severity_illness_dict):
        a = time.time()
        cleanJ = CleanJ(store_df)
        # cleanJ.sex(sex_dict)
        cleanJ.symptoms(symptoms_bag_words, symptoms_sentences_bag)
        # cleanJ.background_diseases(background_diseases_bag_words, background_diseases_sentences_bag,
        #                            mexico_background_diseases_cols)
        cleanJ.ever_intubated(binary_dict)
        cleanJ.ever_icu(binary_dict)
        cleanJ.treatment(world_treatment_bag_words, world_treatment_sentences_bag)
        cleanJ.treatment_by_name_of_hospital()
        cleanJ.treatment_by_origin_severity_illness()
        cleanJ.severity_illness_over_time(severity_illness_dict)

        b = time.time()
        store_df.print_col_values_by_dfs("severity_illness_over_time")
        print("***cleanJ "+ str(b-a))


    @staticmethod
    def infer_feature(store_df):
        a = time.time()
        inferJ = InferJ(store_df)
        inferJ.ever_icu_by_treatment()
        inferJ.treatment_by_ever_icu_and_intubated()
        inferJ.severity_illness_over_time_by_deceased_or_released_date()
        inferJ.severity_illness_over_time_by_ever_icu_and_intubated()
        inferJ.severity_illness_over_time_by_symptoms()
        # inferJ.background_diseases_binary_by_background_diseases()

        b = time.time()
        print("****infer " + str(b - a))


    @staticmethod
    def clean_data(store_df):
        CleanData.clean_feature(store_df, severity_illness_dict)

        # for col in ["sex", "symptoms", "background_diseases", "ever_intubated",
        #             "ever_icu", "treatment"]:
        #     store_df.print_col_values_by_dfs(col)
        # CleanData.infer_feature(store_df)
        # for col in ["sex", "symptoms", "background_diseases", "ever_intubated",
        #             "ever_icu", "treatment", "background_diseases_binary"]:
        #     store_df.print_col_values_by_dfs(col)

