from clean_data.unite_col import *
from clean_text.organize_col.organize_col import *


class CategoryCol(OrganizerCol):
    def __init__(self, priorities_dict):
        self.priorities_dict = priorities_dict

    def find_importace_cat_in_value(self, j):
        ls_cat = j.split(",")
        importance = -1
        importance_cat = None
        for i in range(len(ls_cat)):
            if self.priorities_dict[ls_cat[i]] > importance:
                importance = self.priorities_dict[ls_cat[i]]
                importance_cat = ls_cat[i]
        return importance_cat

    def write_importance_cat_to_output_col(self, hotvec_values, importance_cat, j):
        if importance_cat is None:
            hotvec_values.loc[hotvec_values[j] == 1, "guess"] = j
        else:
            hotvec_values.loc[hotvec_values[j] == 1, "guess"] = importance_cat

    def organize(self, df_gross_guess_col):
        Unite.unite_cols(df_gross_guess_col, list(df_gross_guess_col.columns))
        hotvec_values = pd.get_dummies(df_gross_guess_col[df_gross_guess_col.columns[0]])
        for j in hotvec_values.columns:
            importance_cat = self.find_importace_cat_in_value(j)
            self.write_importance_cat_to_output_col(hotvec_values, importance_cat, j)
        Clean.del_col(hotvec_values, "guess")
        return hotvec_values
