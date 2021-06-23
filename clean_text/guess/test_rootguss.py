import pytest
import pandas as pd
from test_tool.tool_for_test import *
from clean.clean_text.guess_by_root import *


class TestGuessRoot:
    def setup_method(self):
        self.df = pd.DataFrame({"text": ["fever  ", "Mild to moderate, like a flu",
                                 "Mild:moderate ", "cough, fever  ",
                                 "chest pain, respiratory distress, fever, dysphagia, asthenia, weakness, fatigue ",
                                 "fever:cough:acute respiratory distress syndrome "]})

        self.bag_words = {"fever": ["fever", 'febr', 'feverish'],
                              "cough": ["cough", 'dcough', 'toss', 'couh'],
                              "fatigue": ["fatigu", 'fatigur', 'tired', 'lethargi', 'tire'],
                              "weakness": ["weak", 'slump', 'somnol'],
                              "diarrhea": ["diarrhea", 'diarrhoea'],
                              "no_symptom": ["asymptomat", 'oligosymptomat', 'asymptomatic?'],
                              "myalgia": ["malais", "myalgia", 'milagia', 'mialgia'],
                              "sepsis": ['sepsi'],
                              "gastritis": ['gastriti'],
                              "hypoxia": ['hypoxia'],
                              "cardiac arrhythmia": ['arrhythmia'],
                              'azotemia': ['azotemia'],
                              "dysphagia": ['dysphagia'],}

        self.bag_sentences = {"fever": ['flu', 'like'],
                                  "myalgia": ['general', 'muscular', "sore", 'ach', 'muscl', "pain", 'bodi', 'limb',
                                              'flu',
                                              'like'],

                                  "weakness": ['lack', 'energi', 'flu', 'like'],
                                  "respiratory infection": ['pulmonari', 'inflamm', 'respiratori', 'infect', '(arvi)',
                                                            'diseas'],
                                  "respiratory failure": ['respiratori', 'failur']}

    def test_guess(self):
        target = pd.DataFrame({"guess": ["fever",
                                        "fever,myalgia,weakness",
                                        np.nan,
                                        "cough,fever",
                                        "fever,dysphagia,weakness,fatigue",
                                        "fever,cough"]})

        guess = RootGuess(self.df, "text", bag_words=self.bag_words,
                          bag_sentences=self.bag_sentences, num_decision=2,
                          name_output_col="text")
        result = guess.guess()
        assert Tool.compere_cols_str_of_ls_without_order(result["guess"], target["guess"])





    #     simple_df = pd.DataFrame({"text": ["a", "ab", "c  f s", "b", "a"]})
    #     self.simple_ex = RootGuess(simple_df, "text", bag_words={},
    #                                bag_sentences={}, num_decision=2,
    #                                name_output_col="text")
    #     self.simple_result = self.simple_ex.df[self.simple_ex.col]
    #
    # # def test_clean_text(self):
    # #     self.guess.clean_text()
    # #     df = pd.DataFrame({"text": ["fever  ", "Mild to moderate",
    # #                                 "Mild moderate ", "cough  fever  ",
    # #                                  "chest pain  respiratory distress  fever  dysphagia  asthenia  weakness  fatigue ",
    # #                                 "fever cough acute respiratory distress syndrome "]})
    # #     target = df["text"]
    # #     assert Tool.compare_dfs(self.results, target)
    # #
    # # def test_make_text_to_root(self):
    # #     df_len = pd.DataFrame(columns=["len of results", "len of text"])
    # #     df_len["len of text"] = self.results.apply(lambda x : len(x.split(" ")))
    # #     self.guess.make_text_to_root()
    # #     df_len["len of text"] = self.results.apply(lambda x: len(x.split(" ")))
    # #     assert Tool.compare_dfs(df_len["len of text"], df_len["len of text"])
    # #
    # # # def test_get_dummies_from_input_col(self):
    # # #     target = pd.DataFrame({"a": [1, 0, 0, 0, 1], "ab": [0, 1, 0, 0, 0],
    # # #                            "b": [0, 0, 0, 1, 0], "c  f s": [0, 0, 1, 0, 0], })
    # # #     assert self.simple_ex.get_dummies_from_input_col()== target











if __name__ == "__main__":
    pytest.main()
