# coding=utf-8
import os
import shutil
TYPE_PNG = '.png'
class MyParser(object):
    """the main class
    """
    def __init__(self):
        self._first_round_outputs_tempdir = "first_round_outputs_dir"
        self._second_round_outputs_tempdir = "second_round_outputs_dir"


    def copy_file(self):
        for f in os.listdir(os.path.abspath(self._second_round_outputs_tempdir)):
            if (os.path.splitext(f)[1] == TYPE_PNG):
                shutil.copy(os.path.join(os.path.abspath(self._second_round_outputs_tempdir), f),
                            os.path.abspath(self._first_round_outputs_tempdir))

if __name__ == '__main__':
    mparse = MyParser()
    mparse.copy_file()
