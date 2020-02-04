# CMakeCxxProjectTemplate
* Simple and easy Modern C++ CMake Projeect

## Setup
* run ``` scripts/make_project.py ``` to make(copy) CMake C++ project file
  * ```-h  --help```        : help
  * ```-n  --name```        : name of the project
  * ```-d  --directory```   : directory of the project
  * ```-r   --relative```   : use relative directory

    ex) ```python ./scripts/make_project.py -n proj_name -d /folder/you/want/ -r```

* run  ``` scripts/setup_project.py ``` to generate blank folders


## Structures

```
.
├── CMakeLists.txt
├── CMakeSettings.json
├── README.md
├── bin
├── build
├── cmake
├── includes
│   └── hello
│       └── hello.hpp
├── lib
├── main.cpp
├── out
├── res
├── scripts
│   ├── make_project.py
│   └── setup_project.py
├── src
│   ├── CMakeLists.txt
│   └── hello
│       └── hello.cpp
└── thirdparty
```
* ```includes/hello/hello.hpp``` and ```src/hello/hello.cpp``` is a dummy source file which gets ```std::string``` and ```std::cout``` the parameter strings
## Licenses
The repository is under [MIT License](https://opensource.org/licenses/MIT).