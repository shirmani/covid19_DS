import pandas as pd


class CDate:

    @staticmethod
    def detect_range_of_dates_return_list(df, col, character_separator):
        exceptional_df = df[df[col].str.contains(character_separator, na=False)]
        exceptional_df = exceptional_df[~exceptional_df[col].str.contains(":", na=False)]
        mask = (exceptional_df[col].str.len() > 13)
        exceptional_df = exceptional_df.loc[mask]
        return exceptional_df[col].to_list()

    @staticmethod
    def get_range_of_dates_give_one_date(x, character_separator, format, earliest=True):
        df = pd.DataFrame({"a": x.split(character_separator)})
        df["a"] = pd.to_datetime(df["a"].str.strip(), infer_datetime_format=False, errors='coerce', format=format)

        if earliest:
            return df["a"].min().date()
        else:
            return df["a"].max().date()

    @staticmethod
    def replace_range_of_dates_to_1_date(df, col, format, earliest):
        for character_separator in ["-", ","]:
            for x in CDate.detect_range_of_dates_return_list(df, col, character_separator):
                result = CDate.get_range_of_dates_give_one_date(x, character_separator, format, earliest=earliest)
                df.loc[df[col] == x, col] = result

    @staticmethod
    def strip_pollution(df, col):
        df[col] = df[col].str.replace(" ", "")
        for i in [" ", "-", ":", ","]:
            df[col] = df[col].str.strip(i)

    @staticmethod
    def clean_date_col(df, col, format="%Y-%m-%d", earliest=True):
        df[col] = df[col].astype(str)
        format = format.replace(" ", "")
        CDate.strip_pollution(df, col)
        CDate.replace_range_of_dates_to_1_date(df, col, format, earliest=earliest)
        df[col] = pd.to_datetime(df[col], errors='coerce', format=format)
        df[col] = df[col].dt.strftime('%d-%m-%Y')

    @staticmethod
    def v():
        print(15)
