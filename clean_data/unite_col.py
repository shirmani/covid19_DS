from clean_data.clean import Clean
from python_expansion.python_expansion import Pexpansion


class Unite:

    @staticmethod
    def unite_cols_separate_by_comma(df, cols):
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

    @staticmethod
    def unite_all_the_cols_that_contain_x(df, x, name_output_col):
        cols_that_contain_x = []
        for i in df.columns:
            if x in i:
                cols_that_contain_x.append(i)
        if len(cols_that_contain_x) > 0:
            df["0"] = ""
            Unite.unite_cols(df, ["0"] + cols_that_contain_x, delete=True)
            df.rename(columns={"0": name_output_col}, inplace=True)



