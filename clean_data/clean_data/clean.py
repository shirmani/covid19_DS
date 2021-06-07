import numpy as np
from python_expansion import *


class Clean:
    """
    """
    @staticmethod
    def replace_value_by_comparison(df, name_input_col, replacement_dict, name_output_col=None): # clean_by_comparison
        """
        name_col_output: str
            if None output_col = col_input

        replacement_dict: ls
          {replacement_value: [ list of compare value], ..}

        Impossible: {None: [np.nan]}
        """
        if not name_output_col:
            name_output_col = name_input_col

        for k in replacement_dict:
            for i in replacement_dict[k]:
                df.loc[df[name_input_col] == i, name_output_col] = k

    @staticmethod
    def replace_value_by_contained_x(df, name_input_col, contained_dict, name_output_col=None): #clean_by_contained_values
        """
        name_col_output: str
            if None output_col = col_input

        contained_dict: ls
          {replacement_value: [ list of if contained value], ..}
        """
        if not name_output_col:
            name_output_col = name_input_col

        for k in contained_dict:
            for i in contained_dict[k]:
                df.loc[df[name_input_col].astype(str).str.contains(i,  na=False, regex=False),
                       name_output_col] = k

    @staticmethod
    def replace_value_by_contained_all_x_in_ls(df, name_input_col, contained_dict, name_output_col=None):
        """contained_dict = {replacment: [ls]}"""
        if not name_output_col:
            name_output_col = name_input_col

        check_df = pd.get_dummies(df[name_input_col])
        for k in contained_dict:
            for col in check_df.columns:
                if all(word in col for word in contained_dict[k]):
                    df.loc[check_df[col] == 1, name_output_col] = k

    @staticmethod
    def replace_empty_value_to_npnan(df, col):
        col_type = df[col].dtypes
        df[col] = df[col].astype("str")
        df[col] = df[col][df[col].notnull()].apply(lambda x: x.strip())
        df[col] = df[col].astype(col_type)
        Clean.replace_value_by_comparison(df, col, {np.nan: ["", "nan", "None"]})

    @staticmethod
    def clean_text_col_from_punctuation(df, col):
        df[col] = df[col].apply(lambda x: Pexpansion.replace_str_by_comparison(x,
                                {" ": [",", ".", ";", ":", "-", "‚", "+", "!", "_"]})
                                if x == x else x)

    @staticmethod
    def add_comma_to_notnull_value_in_col(df, col):
        Clean.replace_empty_value_to_npnan(df, col)
        df.loc[df[col].notnull(), col] = df[col] + ','

    # test
    @staticmethod
    def change_words_col_to_ls_word_col(df, col):
        """ "abc abc abc" -> ["abc","abc", "abc"] """
        Clean.clean_text_col_from_punctuation(df, col)
        Clean.replace_empty_value_to_npnan(df, col)
        df[col] = df[col].apply(lambda x: x.split(" ") if type(x) == str else x)
        df[col] = df[col].apply(lambda x: Pexpansion.remove_from_ls(x, ["", " "]) if type(x) == list else x)

    # test
    @staticmethod
    def rename_cols_by_index(df, add_for_name=""):
        df.columns = [add_for_name + str(i) for i in range(len(df.columns))]

    @staticmethod
    def del_col(df, dont_del_this_cols):
        col_to_del = list(df.columns)
        dont_del_this_cols = Pexpansion.if_x_not_ls_make_x_ls(dont_del_this_cols)
        for i in dont_del_this_cols:
            if i in col_to_del:
                col_to_del.remove(i)
        df.drop(col_to_del, axis=1, inplace=True)

    @staticmethod 
    def v():
        print(1)

