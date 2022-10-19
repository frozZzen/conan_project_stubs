# package configuration file

include(CMakeFindDependencyMacro)
find_dependency(a_project REQUIRED)

get_filename_component(SELF_DIR "${CMAKE_CURRENT_LIST_FILE}" DIRECTORY)

if (NOT TARGET a_project)
    include(${SELF_DIR}/a_project-export.cmake)
endif()
