import pandas as pd
from unite_dfs_parts.unite_col import *
from clean_text.organize_col.abstract_organize_col import *


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
            hotvec_values.loc[hotvec_values[j] == 1, "organize_process"] = j
        else:
            hotvec_values.loc[hotvec_values[j] == 1, "organize_process"] = importance_cat

    def organize(self, gross_guess_col):
        df = pd.DataFrame(gross_guess_col)
        hotvec_values = pd.get_dummies(df[df.columns[0]])
        for j in hotvec_values.columns:
            importance_cat = self.find_importace_cat_in_value(j)
            self.write_importance_cat_to_output_col(hotvec_values, importance_cat, j)
        Clean.del_col(hotvec_values, "organize_process")
        return hotvec_values
