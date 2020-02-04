#include <iostream>

#include "hello/hello.hpp"

#include <gl/glew.h>
#include <GLFW/glfw3.h>

#include <cassert>

int main(void)
{
	if (!glfwInit()) {
		std::cerr << "[GLFW3] ERROR! : Failed glfwInit()" << std::endl;
		assert(false);
	}

	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 6);
	glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
	glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GLFW_TRUE);

	auto gl_window = glfwCreateWindow(640, 480, "FakeRE", nullptr, nullptr);

	if (gl_window == nullptr) {
		std::cerr << "[GLFW3] ERROR! : Failed to create GLFW window (glfwCreateWindow)" << std::endl;
		glfwTerminate();
		assert(false);
	}

	glfwMakeContextCurrent(gl_window);

	glewExperimental = GL_TRUE;
	if (glewInit() != GLEW_OK) {
		std::cerr << "[GLEW]ERROR! : Failed to initialize GLEW" << std::endl;
		assert(false);
	}
	
	glClearColor(0.1f, 0.1f, 0.1f, 1.f);

	while (glfwWindowShouldClose(gl_window) != true) {
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

		glfwSwapBuffers(gl_window);
		glfwPollEvents();
	}

	glfwDestroyWindow(gl_window);
	glfwTerminate();

	return 0;
}
