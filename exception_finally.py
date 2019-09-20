import os
import sys


def make_at(path, dir_name):
    original_path = os.getcwd()
    print(original_path)
    try:
        os.chdir(path)
        os.mkdir(dir_name)
    except OSError as e:
        print("--Error--", e)
        # raise
    finally:
        print(os.getcwd())
        os.chdir(original_path)


make_at('C:\IRM\workk', 'new')
print(os.getcwd())