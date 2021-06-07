import pytest
from dir import *
import os


class TestDir:
    dir_test = Dir("/home/shir/project/covid19DS/projectlib/dir", "test_dir")

    def test_isdir(self):
        assert os.path.isdir("test_dir") == True

    def test_list_file_in_dir(self):
        assert self.dir_test.list_file_in_dir() == []

    def test_deldir(self):
        self.dir_test.deldir()
        assert os.path.isdir("/home/shir/project/covid19DS/projectlib/dir/test_dir") == False


if __name__ == "__main__":
    pytest.main()

