cmake_minimum_required(VERSION 2.6)
project(cmaketest)
#set(CMAKE_CXX_FLAGS "-std=c++11")
#find_package (Threads)
include_directories( include/mavlink/v1.0)
add_executable(mavlink mavlink_control.cpp serial_port.cpp autopilot_interface.cpp)
#target_link_libraries (cmaketest ${CMAKE_THREAD_LIBS_INIT})
target_link_libraries (mavlink  pthread)
