import pandas as pd
import pytest

from store_dfs_lib.store_dfs import StoreDF
from test_tool.tool_for_test import Tool


class TestStoreDF:

    @pytest.fixture(scope="function")
    def store_dfs(self):
        dfs = [pd.DataFrame({"a": [1, 3, 4],
                             "b": [1, 3, 4]}),
               pd.DataFrame({"n": [1, 3, 4],
                             "b": [1, 3, 4]})]
        dfs_name = ["a", "b"]
        store_dfs = StoreDF(dfs, dfs_name)
        yield store_dfs

    def test_remove(self, store_dfs):
        store_dfs.remove("a")
        x = pd.DataFrame({"a": [1, 3, 4],
                          "b": [1, 3, 4]})
        assert not all([Tool.compare_dfs(i, x) for i in store_dfs.dfs])
        assert "a" not in store_dfs.dfs_names

    def test_add(self, store_dfs):
        x = pd.DataFrame({"m": [1, 3, 4],
                          "x": [1, 3, 4]})
        store_dfs.add("x", x)
        assert any([Tool.compare_dfs(i, x) for i in store_dfs.dfs])
        assert "x" in store_dfs.dfs_names

    def test_get_df_by_name(self, store_dfs):
        target = pd.DataFrame({"a": [1, 3, 4],
                               "b": [1, 3, 4]})
        result = store_dfs.get_df_by_name("a")
        assert Tool.compare_dfs(target, result)


if __name__ == "__main__":
    pytest.main()
