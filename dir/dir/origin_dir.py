from dir.dir import *
from local_pc_UI.local_pc_UI import *
import pandas as pd


class OriginDir(Dir):
    def __init__(self, path, dir_name):
        if not dir_name:
            dir_name = "origin" + SystemUI.get_today_strdate()
        super().__init__(path, dir_name)

    def unzip_file(self):
        OriginDir.format_file_name(self)
        arr = os.listdir(self.path)
        for file_name in arr:
            PcUI.unzip_file(self.path, file_name, self.path)

    def format_file_name(self):
        arr = os.listdir(self.path)
        for file_name in arr:
            new_file_name = file_name.replace("%20", " ")
            new_file_name = new_file_name.replace("%28", "(")
            new_file_name = new_file_name.replace("%29", ")")
            os.rename(self.path + "/" + file_name, self.path + "/" + new_file_name)

    def read_file_as_DataFrame(self, **param):
        if ".xlsx" in param["name_file"]:
            return pd.read_excel(os.path.join(self.path, param["name_file"]), sheet_name=param["sheet_name"])
        return pd.read_csv(os.path.join(self.path, param["name_file"]))


