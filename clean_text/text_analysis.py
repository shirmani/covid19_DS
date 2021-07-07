from unite_dfs_parts.preservation import PreservationCol
from clean_text.guess.abstract_guess import Guess
from clean_text.organize_col.multicategories_col import MultiCategoriesCol
from clean_text.organize_col.abstract_organize_col import OrganizerCol
from clean_text.pre_process_text.make_text_to_root import ToRoot
from clean_text.pre_process_text.abstract_pre_process_text import PreProcessText
# from disply_code_clear.display import Display
from python_expansion_lib.python_expansion import Pexpansion


class TextAnalysis:

    @staticmethod
    def _analysis_flow(df, input_cols, output_col_name,
                       pre_process_text, guess_type, col_type):
        input_cols = Pexpansion.if_x_not_ls_make_x_ls(input_cols)
        Pexpansion.set_up_class_var({"df": df, "input_cols": input_cols},
                                    pre_process_text)

        pre_process_text.process_text()
        Pexpansion.set_up_class_var({"df": df, "input_col": "process",
                                    "output_col_name": output_col_name}, guess_type)
        df_gross_guess_col = guess_type.guess()
        df.drop("process", axis=1, inplace=True)
        return col_type.organize(df_gross_guess_col)

    @staticmethod
    def text_analysis(df, input_cols, output_col_name,
                      guess_type: Guess,
                      pre_process_text: PreProcessText = ToRoot(),
                      col_type: OrganizerCol = MultiCategoriesCol()):
        # print(Display.num_of_line(3) + " text_analysis " + str(input_cols) + " -> " + output_col_name)
        store = PreservationCol(df, input_cols)
        df_col = TextAnalysis._analysis_flow(df, input_cols, output_col_name, pre_process_text, guess_type, col_type)
        df[output_col_name] = df_col[df_col.columns[0]]
        store.release()
