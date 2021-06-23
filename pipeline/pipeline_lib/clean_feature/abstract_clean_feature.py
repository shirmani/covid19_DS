from abc import ABC, abstractmethod


class CleanJAbstract(ABC):
    @abstractmethod
    def __init__(self, dfs_store):
        self.dfs_store = dfs_store



