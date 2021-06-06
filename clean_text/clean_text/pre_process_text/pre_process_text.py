from abc import ABC, abstractmethod


class PreProcessText(ABC):
    @abstractmethod
    def __init__(self, df=None, input_cols=None):
        self.df = df
        self.input_cols = input_cols

    def build_process_col(self):
        self.df["process"] = ""

    @abstractmethod
    def process_text(self):
        raise NotImplemented
