# CMake Version
cmake_minimum_required(VERSION 3.8.2)

# Project Declaration
project(CXX_TEMPLATE VERSION 1.0)

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

# Architecture settings
set(x64 OFF)
if(CMAKE_SIZEOF_VOID_P EQUAL 8)
	set(x64 ON)
endif()

# Build type
if (NOT CMAKE_BUILD_TYPE)
	set(CMAKE_BUILD_TYPE Debug)
endif()

# include directories
include_directories(${PROJECT_ROOT}/includes)
include_directories(${PROJECT_ROOT}/res)

# subdirectories
add_subdirectory(src)

# make executable
add_executable(app main.cpp)
target_link_libraries(app hello_module)
