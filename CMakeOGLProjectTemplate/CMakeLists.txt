# CMake Version
cmake_minimum_required(VERSION 3.8.2)

# Project Declaration
project(CXX_PROJECT_TEMPLATE VERSION 1.0)

# Variables
set(PROJECT_ROOT ${PROJECT_SOURCE_DIR})

# Modern CXX Configuration
set(CMAKE_CXX_STANDARD 17)
set(LINKER_LANGUAGE "CXX")
set(CMAKE_CXX_STANDARD_REQUIRED true)

# Output Directory
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${PROJECT_ROOT}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${PROJECT_ROOT}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_ROOT}/bin)

# CMake module path
set(CMAKE_MODULE_PATH ${PROJECT_ROOT}/cmake)

# Architecture settings
set(x64 OFF)
if(CMAKE_SIZEOF_VOID_P EQUAL 8)
	set(x64 ON)
endif()

# Build type
if (NOT CMAKE_BUILD_TYPE)
	set(CMAKE_BUILD_TYPE Debug)
endif()

# find libraries
find_package(OpenGL REQUIRED)
find_package(glfw3 REQUIRED)
find_package(glew REQUIRED)
if (GLEW_FOUND)
	message("-- Found GLEW ")
endif()

# include directories
include_directories(${PROJECT_ROOT}/includes)
include_directories(${PROJECT_ROOT}/res)
include_directories(${GLFW3_INCLUDE_PATH})
include_directories(${GLEW_INCLUDE_PATH})
include_directories(${OPENGL_INCLUDE_DIR})

# subdirectories
add_subdirectory(src)

# copy all resource datas
file(COPY ${PROJECT_ROOT}/res DESTINATION ${CMAKE_CURRENT_BINARY_DIR}/)
file(COPY ${PROJECT_ROOT}/res DESTINATION ${PROJECT_ROOT}/bin/)

# make executable
add_executable(app main.cpp)
target_link_libraries(app 
	Modules 
	${GLFW3_LIBRARY}
	${GLEW_LIBRARY}
	${OPENGL_LIBRARIES}
)
