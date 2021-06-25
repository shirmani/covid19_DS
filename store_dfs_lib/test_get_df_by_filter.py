import pandas as pd
import pytest

from store_dfs_lib.get_df_by_filter import FilterStoreDF
from store_dfs_lib.store_dfs import StoreDF
from test_tool.tool_for_test import Tool


class TestStoreDF:
    @pytest.fixture(scope="function")
    def filter_df(self):
        dfs = [pd.DataFrame({"a": [1, 3, 4],
                             "b": [1, 3, 4]}),
               pd.DataFrame({"n": [1, 3, 4],
                             "b": [1, 3, 4]}),
               pd.DataFrame({"n": [1, 3, 4],
                             "x": [1, 3, 4]})]
        dfs_name = ["a", "b", "c"]
        filter_df = FilterStoreDF(StoreDF(dfs, dfs_name))
        yield filter_df



    @pytest.fixture(scope="function")
    def dfs_name(self):
        dfs_name = ["a", "b", "c"]
        yield dfs_name

    def test_make_df_of_presence_col_within_df(self, filter_df, dfs_name):
        target = pd.DataFrame({"a": [1, 0, 0],
                               "x": [0, 0, 1],
                               "b": [1, 1, 0],
                               "n": [0, 1, 1]})
        target.index = dfs_name
        result = filter_df.make_df_of_presence_col_within_df()
        assert Tool.compare_dfs(target, result)

    @pytest.mark.parametrize("col, target",
                             [("b", ["a", "b"]),
                              ("f", []),
                              ("x", ["c"])])
    def test_get_dfs_names_if_contain_col(self, filter_df, col, target):
        result = filter_df.get_dfs_names_if_contain_col(col)
        assert result == target

    @pytest.fixture(scope="function")
    def complex_filter_df(self):
        dfs = [pd.DataFrame({"symptoms_origin_1": [1, 3, 4],
                             "b": [1, 3, 4],
                             "symptoms_origin_2": [1, 3, 4],
                             "symptoms": [1, 3, 4],
                             "origin_+-1": [1, 3, 4],
                             "symptoms_origin_3": [1, 3, 4],}),
               pd.DataFrame({"n": [1, 3, 4],
                             "b": [1, 3, 4],
                             "symptoms_origin": [1, 3, 4],}),
               pd.DataFrame({"symptoms_origin_1": [1, 3, 4],
                             "n": [1, 3, 4],
                             "_x": [1, 3, 4],
                             "symptoms_origin_2": [1, 3, 4],})]
        dfs_name = ["vietnam", "world", "philippines"]
        complex_filter_df = FilterStoreDF(StoreDF(dfs, dfs_name))
        yield complex_filter_df

    @pytest.mark.parametrize("x, target",
                             [("symptoms_origin",
                               {"vietnam": ["symptoms_origin_1", "symptoms_origin_2", "symptoms_origin_3"],
                                "world": ["symptoms_origin"],
                                "philippines": ["symptoms_origin_1", "symptoms_origin_2"]}),
                              ("x", {"philippines": ["_x"]})])
    def test_get_dict_keys_names_dfs_values_cols_contain_x(self, complex_filter_df, x, target):
        result = complex_filter_df.get_dict_keys_names_dfs_values_cols_contain_x(x)
        assert Tool.compare_dict_with_list_as_value_without_consider_order(result, target)


if __name__ == "__main__":
    pytest.main()
