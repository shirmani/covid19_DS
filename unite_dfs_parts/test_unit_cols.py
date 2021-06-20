import pandas as pd
import pytest

from test_tool.tool_for_test import Tool
from unite_dfs_parts.unite_col import Unite


class TestUnite:
    @pytest.fixture(scope="function")
    def df(self):
        df = pd.DataFrame({"axg": [1, 3, 4],
                           "b": [1, 3, 4],
                           "nxg": [3, 3, 5],
                           "ggg": [1, 3, 4],
                           "xdg": [1, 3, 4]})

        yield df

    def test_unite_cols(self, df):
        Unite.unite_cols(df, ['axg', 'nxg'], delete=True)
        target = pd.DataFrame({"axg": ["1,3", "3", "4,5"],
                               "b": [1, 3, 4],
                               "ggg": [1, 3, 4],
                               "xdg": [1, 3, 4]})
        assert Tool.compare_dfs(target, df)

    def test_unite_all_the_cols_that_contain_x(self, df):
        Unite.unite_all_the_cols_that_contain_x(df, "xg", "new")
        target = pd.DataFrame({"b": [1, 3, 4],
                               "ggg": [1, 3, 4],
                               "xdg": [1, 3, 4],
                               "new": ["1,3", "3", "4,5"]})

        assert Tool.compare_dfs(target, df)


if __name__ == '__main__':
    pytest.main()
