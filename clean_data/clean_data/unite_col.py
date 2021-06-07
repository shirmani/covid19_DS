from clean_data.clean import *
import pandas as pd


class Unite:

    @staticmethod
    def unite_cols_separate_by_comma(df, cols, delete=True):
        for i in range(1, len(cols)):
            Clean.add_comma_to_notnull_value_in_col(df, cols[0])
            df[cols[0]] = df[cols[0]].astype(str).replace('nan', "") + df[cols[i]]
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



