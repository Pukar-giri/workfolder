cmake_minimum_required(VERSION 3.12)
project(templater)

set(CMAKE_CXX_STANDARD 11)

add_executable(templater main.cpp main.cpp sqlitedb.cpp sqlitedb.h)
target_link_libraries(templater LINK_PUBLIC sqlite3)