from abc import ABC, abstractmethod


class Guess(ABC):
    @abstractmethod
    def __init__(self, df=None, input_col="", output_col_name=""):
        self.df = df
        self.input_col: str = input_col
        self.output_col_name: str = output_col_name

    @abstractmethod
    def guess(self):
        raise NotImplemented

