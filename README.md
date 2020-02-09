# CMakeProjectTemplates
* Collection of my Basic CMake project structure templates.
* Purpose of this repository is from my laziness of making CMake scripts every time making a project.

## Templates
* C++
  * basic modern C++(17) project structure
* OpenGL
  * OpenGL project template based on Modern C++(17) using GLFW3 and GLEW
* OpenCV (in process)
  * OpenCV project template based on Modern C++(17) using only OpenCV
* AR(OpenGL + OpenCV) (in process)
  * Augmented Reality project template based on Modern C++(17) using combinations of right above two project templates(OpenGL, OpenCV)
* Vulkan (in process)
  * Vulkan project template ...

## Scripts
* All template projects above contains ```scripts/make_project.py``` and ```scripts/setup_project.py``` to generate(make a copy and renaming it) the basic project template
* run ``` scripts/make_project.py ``` to make(copy) CMake project structures
  * ```-h  --help```        : help
  * ```-n  --name```        : name of the project
  * ```-d  --directory```   : directory of the project
  * ```-r   --relative```   : use relative directory

    ex) ```python ./scripts/make_project.py -n proj_name -d /folder/you/want/ -r```

* run  ``` scripts/setup_project.py ``` to generate blank folders
* run  ``` scripts/clean_project.py ``` to clean(remove) all cmake caches and build files

## Basic structures
* The basic structure is exactly same as the C++ Project templates, and other templates are modified version(adding FindXXXX.cmake... something like that)
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
│   ├── clean_project.py
│   ├── make_project.py
│   └── setup_project.py
├── src
│   ├── CMakeLists.txt
│   └── hello
│       └── hello.cpp
└── thirdparty
```
* ```includes/hello/hello.hpp``` and ```src/hello/hello.cpp``` is a dummy source file which gets ```std::string``` and ```std::cout``` the parameter strings\

## License
The repository is under [MIT License](https://opensource.org/licenses/MIT), but uses thirdparty libraries(GLFW, GLEW, OpenCV, ...), so you need to follow the license for modification or redistribution of the thirdparty libraries
