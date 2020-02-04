project(CXX_TEMPLATE VERSION 1.0)

set(target app.exe)

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../includes)

file(GLOB header_dir
	${PROJECT_ROOT}/includes
)

file(GLOB_RECURSE headers
	${header_dir}/*.h
	${header_dir}/*/*.h
	${header_dir}/*.hpp
	${header_dir}/*/*.hpp
)

file(GLOB_RECURSE sources
	${CMAKE_CURRENT_SOURCE_DIR}/*.c
	${CMAKE_CURRENT_SOURCE_DIR}/*/*.c
	${CMAKE_CURRENT_SOURCE_DIR}/*.cpp
	${CMAKE_CURRENT_SOURCE_DIR}/*/*.cpp
)

add_library(hello_module STATIC ${headers} ${sources})

target_include_directories(
	hello_module
	PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}
)