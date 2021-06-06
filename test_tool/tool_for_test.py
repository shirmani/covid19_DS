import pandas as pd
from clean_data.clean import *


class Tool:
    @staticmethod
    def compare_dfs(dfa, dfb):
        return (dfa.notnull() == dfb.notnull())

    @staticmethod
    def compere_values_without_order(value_a, value_b):
        if value_a == value_a and value_b == value_b:
            value_a = value_a.strip(",")
            value_b = value_b.strip(",")
            return set(value_a.split(",")) == set(value_b.split(","))
        elif value_a != value_a and value_b != value_b:
            return True

        else:
            return False

    @staticmethod
    def compere_cols_str_of_ls_without_order(col_a, col_b):
        df = pd.concat([col_a, col_b], axis=1)
        df["test"] = df.apply(
            lambda x: Tool.compere_values_without_order(x[0], x[1]), axis=1)
        return df["test"].all() == True

