import pandas as pd
from clean_text.organize_col.multicategories_col import *
from clean_text.guess.guess import *
from clean_text.pre_process_text.make_text_to_root import *
from clean_data.preservation import *
from programmerUI.display import Display


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
    def textAnalysis(df, input_cols, output_col_name,
                     guess_type: Guess,
                     pre_process_text=ToRoot(),
                     col_type=MultiCategoriesCol()):
        print(Display.num_of_line(2) + " textAnalysis " + str(input_cols) + " -> " + output_col_name)
        store = PreservationCol(df, input_cols)
        df_col = TextAnalysis._analysis_flow(df, input_cols, output_col_name, pre_process_text, guess_type, col_type)
        df[output_col_name] = df_col[df_col.columns[0]]
        store.release()
