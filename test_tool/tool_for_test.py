import pandas as pd


class Tool:

    @staticmethod
    def compare_dfs(dfa, dfb):
        dfa.sort_index(inplace=True, axis=1)
        dfb.sort_index(inplace=True, axis=1)
        return dfa.equals(dfb)

    @staticmethod
    def if_val_equal_0_return_True_else_False(val):
        if val == 0:
            return True
        else:
            return False

    @staticmethod
    def compare_dict_with_list_as_value_without_consider_order(dicta, dictb):
        if dicta.keys() != dictb.keys():
            return False

        for k in dicta.keys():
            a = dicta[k]
            b = dictb[k]
            a.sort()
            b.sort()
            if a != b:
                return False
        return True

    @staticmethod
    def if_a_category_column_contains_only_valid_values(df, col, valid_values):
        result = 0
        for i in set(dict(df[col].value_counts()).keys()):
            if i not in set(valid_values):
                result += 1
        return Tool.if_val_equal_0_return_True_else_False(result)

    @staticmethod
    def if_category_col_contains_only_valid_values_on_ls_of_dfs(dfs, col, valid_values):
        result = 0
        for df in dfs:
            if col in df.columns:
                if not Tool.if_a_category_column_contains_only_valid_values(df, col, valid_values):
                    result += 1
        return Tool.if_val_equal_0_return_True_else_False(result)


