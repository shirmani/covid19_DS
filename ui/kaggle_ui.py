# from kaggle.api.kaggle_api_extended import *
import kaggle
from projectlib.get_data import GetData
from projectlib.systemUI import *
import time


class KaggleUI(GetData):

    def __init__(self, origin_dict, save_path):
        super().__init__(origin_dict, save_path)
        self.api = KaggleApi()
        self.api.authenticate()

    def downland_data(self):
        for k in self.origin_dict.keys():
            a = time.time()
            self.api.dataset_download_file(self.origin_dict[k][0], self.origin_dict[k][1],
                                           self.save_path)
            b = time.time()
            print(str(k) + ": " + str(b-a))

