import pytest
import pandas as pd

from store_dfs_lib.controller_store_dfs import ControllerStoreDFs
from store_dfs_lib.store_dfs import StoreDF
from test_tool.tool_for_test import Tool


class TestControllerStoreDFs:
    @pytest.fixture(scope="function")
    def c_store_dfs(self):
        dfs = [pd.DataFrame({"a": [1, 3, 4],
                             "b": [1, 3, 4]}),
               pd.DataFrame({"n": [1, 3, 4],
                             "b": [1, 3, 4]}),
               pd.DataFrame({"n": [1, 3, 4],
                             "x": [1, 3, 4]})]
        dfs_name = ["a", "b", "c"]
        c_store_dfs = ControllerStoreDFs(StoreDF(dfs, dfs_name))
        yield c_store_dfs

    def test_get_ls_of_dfs_that_contain_col(self, c_store_dfs):
        result = c_store_dfs.get_ls_of_dfs_that_contain_col("b")
        target = [pd.DataFrame({"a": [1, 3, 4],
                                "b": [1, 3, 4]}),
                  pd.DataFrame({"n": [1, 3, 4],
                                "b": [1, 3, 4]})]
        worng_num = 0 # TODO : make it func in Tool
        for i in range(len(result)):
            if not Tool.compare_dfs(result[i], target[i]):
                worng_num += 1
        assert worng_num < 1


if __name__ == "__main__":
    pytest.main()
