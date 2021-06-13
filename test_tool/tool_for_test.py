import pandas as pd


class Tool:
    @staticmethod
    def compare_dfs(dfa, dfb):
        return dfa.equals(dfb)
