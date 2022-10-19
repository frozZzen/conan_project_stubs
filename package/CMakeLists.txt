cmake_minimum_required(VERSION 3.1.0)

set(BOOST_LOGGING OFF CACHE BOOL "Enable or disable boost logging")

project(a_project)

set(SRCS
    ${CMAKE_SOURCE_DIR}/src/...
)

set(PUBLIC_HEADERS
    ${CMAKE_SOURCE_DIR}/include/...
)

set(PRIVATE_HEADERS
    ${CMAKE_SOURCE_DIR}/src/...
)

add_library(${CMAKE_PROJECT_NAME} STATIC ${SRCS} ${PUBLIC_HEADERS} ${PRIVATE_HEADERS})

set_target_properties(${CMAKE_PROJECT_NAME}
    PROPERTIES
    CXX_STANDARD 20
    PUBLIC_HEADER "${PUBLIC_HEADERS}"
)

include(GNUInstallDirs)

find_package(Boost REQUIRED)

target_include_directories(${CMAKE_PROJECT_NAME}
    PUBLIC
    $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
)

if(NOT MSVC)
    target_compile_options(${CMAKE_PROJECT_NAME}
        PRIVATE
        -Wall -Wextra -pedantic -Wlogical-op -Wold-style-cast -Wuseless-cast -Wshadow -Wdouble-promotion -Wformat=2 -Wno-format-nonliteral -Weffc++
    )
endif()

if(NOT MSVC)
    target_link_options(${CMAKE_PROJECT_NAME} PRIVATE -no-pie)
endif()

target_link_libraries(${CMAKE_PROJECT_NAME}
    Boost::Boost
)

if (${BOOST_LOGGING})
    add_compile_definitions(BOOST_LOGGING_ENABLED)
endif()

# Install lib and headers
set(LIB_INSTALL_DEST ${CMAKE_INSTALL_LIBDIR}/${CMAKE_PROJECT_NAME})
set(INCLUDE_INSTALL_DEST ${CMAKE_INSTALL_INCLUDEDIR}/${CMAKE_PROJECT_NAME})

install(TARGETS ${CMAKE_PROJECT_NAME}
        EXPORT ${CMAKE_PROJECT_NAME}-export
        ARCHIVE DESTINATION ${LIB_INSTALL_DEST}
        PUBLIC_HEADER DESTINATION ${INCLUDE_INSTALL_DEST}
)

# Install exported targets
install(EXPORT ${CMAKE_PROJECT_NAME}-export DESTINATION ${LIB_INSTALL_DEST})

# Install *-config.cmake to support find_package()
install(FILES ${CMAKE_PROJECT_NAME}-config.cmake DESTINATION ${LIB_INSTALL_DEST})
