# package configuration file

get_filename_component(SELF_DIR "${CMAKE_CURRENT_LIST_FILE}" DIRECTORY)
find_dependency(Boost REQUIRED)
find_dependency(a_project REQUIRED)

if (NOT TARGET a_project)
    include(${SELF_DIR}/a_project-export.cmake)
endif()
