import os
import sys
import enum
import shutil
import fileinput

clean_dirs = [
    "bin",
    "build",
    "lib",
    "out"
]

if __name__ == "__main__":
    os.chdir(os.path.join(os.path.join(os.path.abspath(sys.argv[0]), ".."), ".."))
    print("Cleaning project : remove all cmake cache and other build datas")
    for _dir in clean_dirs:
        if os.path.isdir(_dir):
            print("removing all files in " + _dir)
            os.chdir(_dir)
            for filename in os.listdir(os.getcwd()):
                file_path = os.path.join(os.getcwd(), filename)
                if os.path.isfile(file_path):
                    os.remove(filename)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            os.chdir("..")