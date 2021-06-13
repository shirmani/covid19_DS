import pytest
import pandas as pd
import numpy as np

from test_tool.tool_for_test import Tool


class TestTool:

    @pytest.mark.parametrize("val, result",
                             [(0, True),
                              (1, False),
                              (4, False)])
    def test_if_val_equal_0_return_True_else_False(self, val, result):
        assert Tool.if_val_equal_0_return_True_else_False(val) == result

    @pytest.mark.parametrize("df, result",
                             [(pd.DataFrame({"binary_int": [0, 1, "2", "0", np.nan, 0.0, 1.0, 1.5, True]}), False),
                              (pd.DataFrame({"binary_int": [0, 1, np.nan, 0.0, 1.0, ]}), True),
                              (pd.DataFrame({"binary_int": [0, 1, np.nan, 0.0, 1.0, "1"]}), False),
                              (pd.DataFrame({"binary_int": [0, 0, np.nan, 0.0, 0, 0]}), True)])
    def test_if_category_col_contains_only_valid_values(self, df, result):
        assert result == Tool.if_a_category_column_contains_only_valid_values(df, "binary_int", [0, 1])

    @pytest.mark.parametrize("dfs, result",
                             [([pd.DataFrame({"binary_int": [0, 1, "2", "0", np.nan],
                                             "binary": [0, 1, np.nan, 0.0, 1.0]}),
                               pd.DataFrame({"binary": [0, 1, np.nan, 0.0, 1.0, True, 6]}),
                               pd.DataFrame({"loop": [0, 1, np.nan, 0.0, 1.0, True]})], False),

                             ([pd.DataFrame({"binary_int": [0, 1, "2", "0", np.nan],
                                            "binary": [0, 1, np.nan, 0.0, 1.0]}),
                              pd.DataFrame({"binary": [0, 1, np.nan, 0.0, 1.0, 0, 1]}),
                              pd.DataFrame({"loop": [0, 1, np.nan, 0.0, 1.0, 6]})], True)])

    def test_if_category_col_contains_only_valid_values_on_ls_of_dfs(self, dfs, result):
        assert result == Tool.if_category_col_contains_only_valid_values_on_ls_of_dfs(dfs, "binary", [0, 1])


if __name__ == '__main__':
    pytest.main()
