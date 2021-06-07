

class GetData:
    def __init__(self, origin_dict, save_path):
        self.origin_dict = origin_dict
        self.save_path = save_path

    def downland_data(self):
        raise NotImplementedError("Subclass must implement abstract method")



    #


    # @staticmethod
    # def downland_kaggle_datasets(origin_dict, path_origin):
    #     KaggleUI.authenticate_api()
    #     for k in origin_dict.keys():
    #         KaggleUI.downland_kaggleDS(origin_dict[k][0], origin_dict[k][1], path_origin)
    #         SystemUI.unzip_file(path_origin + "\\" + origin_dict[k][1] + ".zip", path_origin)
    #
    # @staticmethod
    # def datasets_as_dfs(path_origin, name_file):
    #     return pd.read_csv(SystemUI.joint_path_and_dirname(path_origin, name_file))


