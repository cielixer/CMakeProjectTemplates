import os
import sys
import enum
import shutil
import fileinput

def print_help():
    print("Make a C++ CMake project by copying the files and renaming it")
    print("-h,  --help      : help")
    print("-n,  --name      : name of the project")
    print("-d,  --directory : directory of the project")
    print("-r,  --relative  : use relative directory")

class StateMachine(enum.Enum):
    NONE = 0
    NAME = 1
    DIR  = 2

project_name = "cxx_project"
directory = "./"
relative_path = False

cur_state = StateMachine.NONE

if __name__ == "__main__":
    
    project_file_path = os.path.abspath(sys.argv[0])
    project_file_path = os.path.join(project_file_path, "..")
    project_file_path = os.path.join(project_file_path, "..")
    project_file_path = os.path.abspath(project_file_path)
    
    for idx in range(1, len(sys.argv)):
        in_data = sys.argv[idx]
        
        if cur_state == StateMachine.NONE:
            if   in_data == "-h" or in_data == "--help":
                print_help()
                sys.exit()
            elif in_data == "-n" or in_data == "--name":
                cur_state = StateMachine.NAME
            elif in_data == "-d" or in_data == "--directory":
                cur_state = StateMachine.DIR
            elif in_data == "-r" or in_data == "--relative":
                relative_path = True
            else :
                print("invalid arguments : ", in_data)
        
        elif cur_state == StateMachine.NAME:
            project_name = in_data
            cur_state = StateMachine.NONE
        
        elif cur_state == StateMachine.DIR:
            directory = in_data
            cur_state = StateMachine.NONE
    
    if relative_path == True:
        directory_paths = os.path.split(directory)
        directory = os.getcwd()
        
        for splited_dir in directory_paths:
            directory = os.path.join(directory, splited_dir)
            assert os.path.isdir(directory), "Path is not available : " + directory
    else:
        directory_paths = os.path.split(directory)
        for splited_dir in directory_paths:
            directory = os.path.join(directory, splited_dir)
            assert os.path.isdir(directory), "Path is not available : " + directory
    
    print("Project Name : ", project_name)
    print("Directory    : ", directory)
    
    os.chdir(directory)
    print("Copying cmake project files at : ", project_file_path)
    
    dst = os.path.join(os.getcwd(), project_name)
    print("Copying CMake project to ", dst)
    dst_root = shutil.copytree(project_file_path, dst)
    
    os.chdir(dst_root)
    
    # Modify CMake Project name(declaration) CXX_TEMPLATE -> ${project_name}
    print("Renaming project name CXX_TEMPLATE to ", project_name)
    for line in fileinput.input("./CMakeLists.txt", inplace=True):
        if "CXX_TEMPLATE" in line:
            line = line.replace(line, "project(" + project_name + " VERSION 1.0)\n")
        sys.stdout.write(line)
    
    for line in fileinput.input("./src/CMakeLists.txt", inplace=True):
        if "CXX_TEMPLATE" in line:
            line = line.replace(line, "project(" + project_name + " VERSION 1.0)\n")
        sys.stdout.write(line)