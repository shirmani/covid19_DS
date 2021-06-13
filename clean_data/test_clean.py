import numpy as np
import pandas as pd
import pytest

from clean_data.clean import *
from test_tool.tool_for_test import *


class TestClean:

    @pytest.fixture(scope="function")
    def df(self):
        yield pd.DataFrame({"a": ["x", "ax", np.nan, 1, 2, "  ", None, "|  ", "", 11, [1, 2, '3', 2]]})

    @pytest.fixture(scope="function")
    def text_df(self):
        yield pd.DataFrame({"a": ["Dad: went to the Garden.", None, " Tulik-sits by the sea",
                                  "Rina loves strawberries?", "Assaf, bought   |5 cars", np.nan,
                                  33,]})

    def test_replace_value_by_comparison(self, df):
        Clean.replace_value_by_comparison(df, "a", {"v": ["x"], np.nan: [2]})
        target = pd.DataFrame({"a": ["v", "ax", np.nan, 1, np.nan, "  ", None, "|  ", "", 11, [1, 2, "3", 2]]})
        assert Tool.compare_dfs(df, target)

    def test_replace_value_by_contained_string(self, df):
        Clean.replace_value_by_contained_string(df, "a", {"v": ["x"], "l": [" "], "3": [1]})
        target = pd.DataFrame({"a": ["v", "v", np.nan, 1, 2, "l", None, "l", "", 11, [1, 2, "3", 2]]})
        assert Tool.compare_dfs(df, target)

    def test_replace_value_by_contained_all_x_in_ls(self):
        pass

    def test_replace_empty_value_to_npnan(self, df):
        Clean.replace_empty_value_to_npnan(df, "a")
        target = pd.DataFrame({"a": ["x", "ax", np.nan, 1, 2, np.nan, np.nan, "|  ", np.nan, 11, [1, 2, "3", 2]]})
        assert Tool.compare_dfs(df, target)

    def test_clean_text_col_from_punctuation(self, text_df):
        Clean.clean_text_col_from_punctuation(text_df, "a")
        target = pd.DataFrame({"a": ["Dad  went to the Garden ", None, " Tulik sits by the sea",
                                     "Rina loves strawberries ", "Assaf  bought    5 cars", np.nan,
                                     33]})
        assert Tool.compare_dfs(text_df, target)

    def test_add_comma_to_value_and_replace_null_with_empty_str(self, df):
        Clean.add_comma_to_value_and_replace_null_with_empty_str(df, "a")
        target = pd.DataFrame({"a": ["x,", "ax,", "", "1,", "2,", "", "", "|  ,", "",
                                     "11,", "[1, 2, '3', 2],"]})
        assert Tool.compare_dfs(df, target)

    def test_change_words_col_to_ls_word_col(self, text_df):
        Clean.change_text_col_to_ls_words_col(text_df, "a")
        target = pd.DataFrame({"a": [["Dad", "went", "to", "the", "Garden"], None,
                                     ["Tulik", "sits", "by", "the", "sea"],
                                     ["Rina", "loves", "strawberries"],
                                     ["Assaf", "bought", "5", "cars"], np.nan, 33]})
        assert Tool.compare_dfs(text_df, target)

    # @pytest.fixture
    # def fixt(self, request):
    #     return request.param * 3
    #
    # @pytest.mark.parametrize("fixt", ["a", "b"], indirect=True)
    # def test_indirect(self, fixt):
    #     assert len(fixt) == 3
    #
    #
    #
    # def test_del_col(self, df):
    #     Clean.del_col(df, ["a", "c"])
    #     target = pd.DataFrame({"a": ["x", "ax"],
    #                        "c": ["x", "ax"],})
    #     assert df == target



if __name__ == "__main__":
    pytest.main()
