from abc import ABC, abstractmethod


class Guess(ABC):
    @abstractmethod
    def __init__(self, df=None, input_col=None, output_col_name=None):
        self.df = df
        self.input_col = input_col
        self.output_col_name = output_col_name

    @abstractmethod
    def guess(self):
        raise NotImplemented

