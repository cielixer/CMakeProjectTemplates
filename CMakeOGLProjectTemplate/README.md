# CMakeOGLProjectTemplate
Simple and basic CMake OpenGL Project structure

## Setup
* run ``` scripts/make_project.py ``` to make(copy) CMake OGL project file
  * ```-h  --help```        : help
  * ```-n  --name```        : name of the project
  * ```-d  --directory```   : directory of the project
  * ```-r   --relative```   : use relative directory

    ex) ```python ./scripts/make_project.py -n proj_name -d /folder/you/want/ -r```

* run  ``` scripts/setup_project.py ``` to generate blank folders
---
## Dependencies
* OpenGL version default by 4.6, you can change the specific major and minor version of GL by modifying the main.cpp 
* GLFW3 (using FindGLFW3.cmake)
* GLEW (using FindGLEW.cmake) 
---
## Structures

```
.
├── CMakeLists.txt
├── CMakeSettings.json
├── README.md
├── bin
├── build
├── cmake
│   ├── FindGLEW.cmake
│   └── FindGLFW3.cmake
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
    └── LICENSE.md
```
* ```includes/hello/hello.hpp``` and ```src/hello/hello.cpp``` is a dummy source file which gets ```std::string``` and ```std::cout``` the parameter strings
---
## Licenses
The repository itself is [MIT License](https://opensource.org/licenses/MIT), but uses GLFW3 and GLEW externally so if you want to modify, redistribute or anything with GLFW3 and GLEW in source or binary form, you need to follow the licenses of these