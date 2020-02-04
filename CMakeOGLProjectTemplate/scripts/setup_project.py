import os
import sys

directory_names = [
    "bin",
    "build",
    "cmake",
    "include",
    "lib",
    "out",
    "res",
    "scripts",
    "src",
    "thirdparty"
]

if __name__ == "__main__":
    os.chdir(os.path.join(os.path.join(os.path.abspath(sys.argv[0]), ".."), ".."))
    print("Project root at ", os.getcwd())
    
    for dir_name in directory_names:
        print("Making directory : ", dir_name)
        if not os.path.isdir(dir_name):
            os.mkdir(dir_name)
        else:
            print(dir_name + " already exist!")