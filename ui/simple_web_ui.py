import time
from io import StringIO
import pandas as pd
import urllib.request
from projectlib.get_data import GetData


class WebUi(GetData):

    def __init__(self, origin_dict, save_path):
        super().__init__(origin_dict, save_path)

    @staticmethod
    def request_data(url):
        request = urllib.request.urlopen(url)
        return request.read()

    @staticmethod
    def care_type_file(request):
        if isinstance(request, (bytes, bytearray)):
            s = str(request, 'utf-8')
            data = StringIO(s)
            return pd.read_csv(data)

    def downland_data(self):
        for k in self.origin_dict.keys():
            a = time.time()
            request = WebUi.request_data(self.origin_dict[k][0])
            print(type(request))
            df = WebUi.care_type_file(request)
            b = time.time()
            print(b-a)
            df.to_csv(self.save_path + "/" + self.origin_dict[k][1])
            c = time.time()
            print(c - b)




