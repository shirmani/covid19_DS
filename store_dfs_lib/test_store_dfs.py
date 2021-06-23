import pandas as pd
import pytest

from python_expansion_lib.python_expansion import Pexpansion
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

    def test_add_col_to_dfs(self, store_dfs):
        store_dfs.add_col_to_dfs(["a", "b"], "dd", 0)
        target_a = pd.DataFrame({"a": [1, 3, 4],
                                 "b": [1, 3, 4],
                                 "dd": [0, 0, 0]})

        target_b = pd.DataFrame({"n": [1, 3, 4],
                                 "b": [1, 3, 4],
                                "dd": [0, 0, 0]})
        assert Tool.compare_dfs(store_dfs.get_df_by_name("a"), target_a)
        assert Tool.compare_dfs(store_dfs.get_df_by_name("b"), target_b)


    @pytest.mark.parametrize("change_dict, target_a, target_b",
                             [({"a": {"a": "first", "b": "last"},
                               "b": {"n": "x"}},
                              pd.DataFrame({"first": [1, 3, 4],
                                            "last": [1, 3, 4]}),
                              pd.DataFrame({"x": [1, 3, 4],
                                            "b": [1, 3, 4]})),
                              ({"a": {},
                                "b": {"n": "x", "k": "tt"}},
                               pd.DataFrame({"a": [1, 3, 4],
                                             "b": [1, 3, 4]}),
                               pd.DataFrame({"x": [1, 3, 4],
                                             "b": [1, 3, 4]})),
                              ])
    def test_rename_dfs_cols(self, store_dfs, change_dict, target_a, target_b):
        store_dfs.rename_dfs_cols(change_dict)
        assert Tool.compare_dfs(store_dfs.get_df_by_name("a"), target_a)
        assert Tool.compare_dfs(store_dfs.get_df_by_name("b"), target_b)

    @pytest.mark.parametrize("change_dict, target_a, target_b",
                             [({"a": ["a"],
                               "b": ["b"]},
                              pd.DataFrame({"b": [1, 3, 4]}),
                              pd.DataFrame({"n": [1, 3, 4]}))])
    def test_drop_cols_from_dfs(self, store_dfs, change_dict, target_a, target_b):
        store_dfs.drop_cols_from_dfs(change_dict)
        assert Tool.compare_dfs(store_dfs.get_df_by_name("a"), target_a)
        assert Tool.compare_dfs(store_dfs.get_df_by_name("b"), target_b)

    @pytest.mark.parametrize("change_dict, target_a",
                             [({"a": ["gg"]},
                              pd.DataFrame({"a": [1, 3, 4],
                                            "b": [1, 3, 4]}))])
    def test_w(self, store_dfs, change_dict, target_a):
        store_dfs.drop_cols_from_dfs(change_dict)
        assert Tool.compare_dfs(store_dfs.get_df_by_name("a"), target_a)



if __name__ == "__main__":
    pytest.main()
