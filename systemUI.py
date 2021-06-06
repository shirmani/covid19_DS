import os
import zipfile
from datetime import date


class SystemUI:
    @staticmethod
    def joint_path_and_dirname(path, name):
        return os.path.join(path, name)

    @staticmethod
    def unzip_file(path_file, name_file, save_path):
        if ".zip" in name_file:
            try:
                path_file = SystemUI.joint_path_and_dirname(path_file, name_file )

                with zipfile.ZipFile(path_file, 'r') as zipObj:
                    zipObj.extractall(save_path)
                    os.remove(path_file)
            except Exception:
                pass

    @staticmethod
    def get_today_strdate():
        return date.today().strftime("%d.%m.%Y")




