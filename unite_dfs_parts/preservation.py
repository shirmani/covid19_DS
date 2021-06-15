from python_expansion_lib.python_expansion import Pexpansion


class PreservationCol:
    def __init__(self, df, cols):
        self.df = df
        self.cols = Pexpansion.if_x_not_ls_make_x_ls(cols)
        self.store()

    def store(self):
        for col in self.cols:
            self.df["Preservation," + col] = self.df[col]

    def release(self):
        for col in self.cols:
            self.df.drop(col, axis=1, inplace=True)
            self.df.rename(columns={"Preservation," + col: col}, inplace=True)
