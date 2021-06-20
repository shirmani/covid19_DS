from unite_dfs_parts.unite_col import Unite
from clean_text.organize_col.organize_col import OrganizerCol


class MultiCategoriesCol(OrganizerCol):

    def organize(self, df_gross_guess_col):
        Unite.unite_cols(df_gross_guess_col, list(df_gross_guess_col.columns))
        return df_gross_guess_col
