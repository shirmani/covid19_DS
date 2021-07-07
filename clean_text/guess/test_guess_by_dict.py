import pytest
import pandas as pd
from test_tool.tool_for_test import *
from clean_text.guess.guess_by_dict import *


class TestGuessRoot:
    @pytest.fixture(scope="function")
    def instance_guess(self):
        df = pd.DataFrame({"text": ["fever", "Mild to moderate, like a flu",
                                    "Mild:moderate ", "cough, fever   ", np.nan,
                                    "respiratory distress, fever, dysphagia",
                                    "fever:cough:acute respiratory distress syndrome "]})

        bag_words = {"fever": ["fever"],
                     "cough": ["cough"],
                     "dysphagia": ['dysphagia']}

        bag_sentences = {"fever": ['flu', 'like'],
                         "myalgia": ['flu', 'like'],
                         "respiratory infection": ["respiratory", "distress", "syndrome"]}

        instance_guess = GuessByDict(bag_words, bag_sentences)
        instance_guess.df = df
        instance_guess.input_col = "text"
        instance_guess.output_col_name = "text"
        yield instance_guess



    def test_make_guess_word_col(self, instance_guess):
        df_hotvec_phrase = pd.get_dummies(instance_guess.df[instance_guess.input_col])
        result = instance_guess._make_guess_word_col(df_hotvec_phrase)
        target = pd.DataFrame({"text": ["fever,", "",
                                        "", "cough,fever,", "",
                                        "fever,dysphagia,",
                                        "fever,cough,"]})
        assert Tool.compare_multicategory_cols(target["text"], result)



    def test_build_dict_key_phrase_with_category_value_num_of_word_that_point_on_cat(self, instance_guess):
        df_hotvec_phrase = pd.get_dummies(instance_guess.df[instance_guess.input_col])
        result = instance_guess._build_dict_key_phrase_with_category_value_num_of_word_that_point_on_cat(
                 df_hotvec_phrase.columns)
        target = {'Mild to moderate, like a flu|cat|fever': 2, 'Mild to moderate, like a flu|cat|myalgia': 2,
                  'fever:cough:acute respiratory distress syndrome |cat|respiratory infection': 3,
                  'respiratory distress, fever, dysphagia|cat|respiratory infection': 2}
        assert (target == result)



    # def test_guess(self, class_guess):
    #     result = class_guess.guess()
    #     target = pd.DataFrame({"text": ["fever", "fever,myalgia",
    #                              "", "cough,fever", "",
    #                              "respiratory infection,fever,dysphagia",
    #                              "fever,cough,respiratory infection"]})
    #     assert Tool.compare_multicategory_cols(target["text"], result["text"])


if __name__ == "__main__":
    pytest.main()
