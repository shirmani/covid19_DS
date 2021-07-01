import numpy as np
import pandas as pd
import pytest

from clean_lib.clean_date import CDate
from test_tool.tool_for_test import Tool


class TestCDate:

    def test_detect_range_of_dates_return_list(self):
        df = pd.DataFrame({"a": ["19.02.2020 - 21.02.2020 ", "19.02.2020 - ",
                                 "06.01.2020, 11.01.2020, 17.01.2020", "frfrfrfvv",
                                 "Sep 25 2000 - Sep 28 2000", "2020-03-05 00:00:00"]})
        target = {"19.02.2020 - 21.02.2020 ", "Sep 25 2000 - Sep 28 2000"}
        result = set(CDate.detect_range_of_dates_return_list(df, "a", "-"))
        assert target == result

    @pytest.mark.parametrize("x, character_separator, format, target",
                             [("19.02.2020 - 21.02.2020 ", "-", "%d.%m.%Y", '2020-02-19'),
                              ("Sep 25 2000 - Sep 28 2000", "-", "%b %d %Y", "2000-09-25"),
                              ("06.01.2020, 11.01.2020, 17.01.2020", ",", "%d.%m.%Y", "2020-01-06")])
    def test_get_range_of_dates_give_one_date_earliest(self, x, character_separator, format, target):
        result = CDate.get_range_of_dates_give_one_date(x, character_separator, format)
        assert str(result) == target

    @pytest.mark.parametrize("x, character_separator, format, target",
                             [("19.02.2020 - 21.02.2020 ", "-", "%d.%m.%Y", '2020-02-21'),
                              ("Sep 25 2000 - Sep 28 2000", "-", "%b %d %Y", "2000-09-28"),
                              ("06.01.2020, 11.01.2020, 17.01.2020", ",", "%d.%m.%Y", "2020-01-17")])
    def test_get_range_of_dates_give_one_date_latest(self, x, character_separator, format, target):
        result = CDate.get_range_of_dates_give_one_date(x, character_separator, format, earliest=False)
        assert str(result) == target

    @pytest.mark.parametrize("df, format, target",
                             [( pd.DataFrame({"a": ["19.02.2020 - 21.02.2020 ", np.nan, "desdede"]}), "%d.%m.%Y", pd.DataFrame({"a": ["2020-02-19", "nan", "desdede"]})
                              ),
                              (pd.DataFrame({"a": ["Sep 25 2000 - Sep 28 2000", np.nan, "Sep 28 2000"]}),
                               "%b %d %Y",
                               pd.DataFrame({"a": ["2000-09-25", "nan", "Sep 28 2000"]})),
                              (pd.DataFrame({"a": ["06.01.2020, 11.01.2020, 17.01.2020",  np.nan, "17.01.2020"]}),
                               "%d.%m.%Y",
                               pd.DataFrame({"a": ["2020-01-06",  "nan", "17.01.2020"]}))])
    def test_replace_range_of_dates_to_1_date(self, df, format, target):
        CDate.replace_range_of_dates_to_1_date(df, "a", format, earliest=True)
        df["a"] = df["a"].astype(str)
        assert Tool.compare_dfs(df, target)

    def test_strip_pollution(self):
        df = pd.DataFrame({"a": ["21.02.2020   :: -", "19.02.2020 ,",
                                 "06.01.2020, 11.01.2020, 17.01.2020 -", "frfrfrfvv -",
                                 "Sep 25 2000-", "2020-03-05,,"]})
        target = pd.DataFrame({"a": ["21.02.2020", "19.02.2020",
                                     "06.01.2020,11.01.2020,17.01.2020", "frfrfrfvv",
                                     "Sep252000", "2020-03-05"]})
        CDate.strip_pollution(df, "a")
        assert Tool.compare_dfs(df, target)



if __name__ == "__main__":
    pytest.main()
