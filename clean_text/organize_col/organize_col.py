from abc import ABC, abstractmethod


class OrganizerCol(ABC):

    @abstractmethod
    def organize(self, df_gross_guess_col):
        raise NotImplemented
