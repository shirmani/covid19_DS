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


if __name__ == "__main__":
    pytest.main()
