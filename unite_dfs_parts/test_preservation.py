import pandas as pd
import pytest

from test_tool.tool_for_test import Tool
from unite_dfs_parts.preservation import PreservationCol


class TestPreservation:
    @pytest.fixture(scope="function")
    def df(self):
        df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
        yield df

    def test_store(self, df):
        PreservationCol(df, "a")
        target = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9], "Preservation,a": [1, 2, 3]})
        assert Tool.compare_dfs(df, target)

    def test_store_multi_cols(self, df):
        PreservationCol(df, ["a", "b"])
        target = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9],
                               "Preservation,a": [1, 2, 3], "Preservation,b": [4, 5, 6]})
        assert Tool.compare_dfs(df, target)

    def test_release(self, df):
        save_col = PreservationCol(df, "a")
        df["a"] = df["a"] + df["b"]
        save_col.release()
        target = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
        assert Tool.compare_dfs(df, target)

    def test_release_multi_cols(self, df):
        save_col = PreservationCol(df, ["a", "b"])
        df["a"] = df["a"] + df["b"]
        df["b"] = df["a"] + df["b"]
        save_col.release()
        target = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
        assert Tool.compare_dfs(df, target)


if __name__ == "__main__":
    pytest.main()