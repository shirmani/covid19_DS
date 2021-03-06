import sys


class Display:

    @staticmethod
    def num_of_line(depth):
        return str(sys._getframe(depth).f_lineno)

    @staticmethod
    def buffer_with_num_of_line():
        print()
        print()
        print(Display.num_of_line(3) + "-----------------------------")

    @staticmethod
    def print_with_num_of_line(string, depth=2):
        print(Display.num_of_line(depth) + " " + string)
