import pandas as pd

from clean_data.clean import Clean
from clean_data.unite_col import Unite
from clean_text.guess.guess import Guess
from python_expansion.python_expansion import Pexpansion


class GuessByDict(Guess):
    def __init__(self, bag_words, bag_sentences, num_decision=2):
        super().__init__()
        self.bag_words = Pexpansion.upside_down_dictionary(bag_words)
        self.bag_sentences = Pexpansion.upside_down_dictionary(bag_sentences)
        self.num_decision = num_decision

    def _get_hotvec_of_value_from_col(self):
        return pd.get_dummies(self.df[self.input_col])

    def _build_guide_dict_to_guess_sentence(self, ls_phrase):
        guide_dict_to_guess_sentence = {}
        for j in ls_phrase:
            for root, cats in self.bag_sentences.items():
                if root in j:
                    for category in cats:
                        if j + "," + category in guide_dict_to_guess_sentence.keys():
                            guide_dict_to_guess_sentence[j + "," + category] += 1
                        else:
                            guide_dict_to_guess_sentence[j + "," + category] = 1
        return guide_dict_to_guess_sentence

    def _make_guess_sentence_col_by_guide_dict(self, df_hotvec_phrase, guide_dict_to_guess_sentence):
        df_hotvec_phrase["guess_sentence"] = ""
        for k, v in guide_dict_to_guess_sentence.items():
            if v > self.num_decision - 1:
                ls = k.split(",")
                j, cat = ls[0], ls[1]
                df_hotvec_phrase.loc[df_hotvec_phrase[j] == 1, "guess_sentence"] += cat + ","
        return df_hotvec_phrase.pop("guess_sentence")

    def _make_guess_sentence_col(self, df_hotvec_phrase):
        guide_dict = GuessByDict._build_guide_dict_to_guess_sentence(self, df_hotvec_phrase.columns)
        return GuessByDict._make_guess_sentence_col_by_guide_dict(self, df_hotvec_phrase, guide_dict)

    def _make_guess_word_col(self, df_hotvec_phrase):
        df_hotvec_phrase["guess_word"] = ""
        for j in df_hotvec_phrase:
            for root, cats in self.bag_words.items():
                if root in j:
                    for category in cats:
                        df_hotvec_phrase.loc[df_hotvec_phrase[j] == 1, "guess_word"] += category + ","
        return df_hotvec_phrase.pop("guess_word")

    def _concat_word_sentence_guesses(self, cols):
        df = pd.concat(cols, axis=1)
        df[self.output_col_name] = ""
        Unite.unite_cols(df, [self.output_col_name, "guess_word", "guess_sentence"])
        Clean.replace_empty_value_to_npnan(df, self.output_col_name)
        return df

    def guess(self):
        df_hotvec_phrase = self._get_hotvec_of_value_from_col()
        sentence_col = self._make_guess_sentence_col(df_hotvec_phrase)
        word_col = self._make_guess_word_col(df_hotvec_phrase)
        return self._concat_word_sentence_guesses([word_col, sentence_col])

