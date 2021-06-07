import os


class Dir:
    def __init__(self, path, dir_name):
        self.dir_name = dir_name
        self.path = os.path.join(path, self.dir_name)

        if not os.path.isdir(self.path):
            os.makedirs(self.path)

    def list_file_in_dir(self):
        return os.listdir(self.path)

    def deldir(self):
        os.rmdir(self.path)
        self.dir_name = None
        self.path = None





