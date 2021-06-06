from clean_data.unite_col import *
from clean_text.organize_col.organize_col import *


class MultiCategoriesCol(OrganizerCol):

    def organize(self, df_gross_guess_col):
        Unite.unite_cols(df_gross_guess_col, list(df_gross_guess_col.columns))
        return df_gross_guess_col
