cmake_minimum_required(VERSION 3.1.0)

include(GNUInstallDirs)

project(a_project)

add_library(${CMAKE_PROJECT_NAME} INTERFACE)

set(DUMMY_FILE ${CMAKE_CURRENT_BINARY_DIR}/dummy.cpp)
file(WRITE ${DUMMY_FILE}
"#include <${CMAKE_CURRENT_SOURCE_DIR}/include/some_header.h>
int main(int argc, char* argv[]){return 0;}"
)

add_executable(check_header_for_warnings ${DUMMY_FILE})
set_target_properties(check_header_for_warnings
    PROPERTIES
    CXX_STANDARD 20
)
target_link_libraries(check_header_for_warnings ${CMAKE_PROJECT_NAME})

target_link_libraries(${CMAKE_PROJECT_NAME} INTERFACE)

target_include_directories(${CMAKE_PROJECT_NAME}
    INTERFACE
    $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
)

# Install lib and headers
set(LIB_INSTALL_DEST ${CMAKE_INSTALL_LIBDIR}/${CMAKE_PROJECT_NAME})
set(INCLUDE_INSTALL_DEST ${CMAKE_INSTALL_INCLUDEDIR}/${CMAKE_PROJECT_NAME})

install(
    TARGETS ${CMAKE_PROJECT_NAME}
    EXPORT ${CMAKE_PROJECT_NAME}-export
    PUBLIC_HEADER DESTINATION ${INCLUDE_INSTALL_DEST}
)

# Install exported targets
install(EXPORT ${CMAKE_PROJECT_NAME}-export DESTINATION ${LIB_INSTALL_DEST})

# Install *-config.cmake to support find_package()
install(FILES ${CMAKE_PROJECT_NAME}-config.cmake DESTINATION ${LIB_INSTALL_DEST})
