import pandas as pd
from clean_lib.clean import Clean
from python_expansion_lib.python_expansion import Pexpansion


class Unite:

    @staticmethod
    def unite_cols_separate_by_comma(df, cols):
        for i in range(1, len(cols)):
            Clean.add_comma_to_value_and_replace_null_with_empty_str(df, cols[0])
            Clean.replace_all_null_to_x(df, cols[i], "")
            df[cols[0]] = df[cols[0]].astype(str) + df[cols[i]].astype(str)
        return df

    @staticmethod
    def unite_cols(df, cols, delete=True):
        """Vector connection of text columns
        with a separation of "," between the connections"""
        df = Unite.unite_cols_separate_by_comma(df, cols)
        # process
        df[cols[0]] = df[cols[0]].apply(lambda x: Pexpansion.del_duplicate_categories_in_multicategories_str(x))
        df[cols[0]] = df[cols[0]].apply(lambda x: x.strip(",") if type(x) == str else x)
        df[cols[0]] = df[cols[0]].apply(lambda x: None if x == "" else x)
        # Delete unnecessary columns
        if delete:
            cols.pop(0)
            df.drop(cols, axis=1, inplace=True)

    @staticmethod
    def unite_all_the_cols_that_contain_x(df, x, name_output_col, delete):
        cols_that_contain_x = list(df.filter(like=x).columns)
        if len(cols_that_contain_x) > 0:
            df[name_output_col] = ""
            Unite.unite_cols(df, [name_output_col] + cols_that_contain_x, delete=delete)
