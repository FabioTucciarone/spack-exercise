cmake_minimum_required(VERSION "3.12")

project("spackexample" VERSION 0.3.0)

option(ENABLE_BOOST "Disable the Boost support of this package" ON)
option(ENABLE_YAML_CPP "Disable the Boost support of this package" ON)

add_library(spackexamplelib main.cpp)

if(ENABLE_BOOST)
  find_package(Boost
    1.65.1
    REQUIRED
    filesystem
  )
  target_sources(spackexamplelib PRIVATE filesystem/filesystem.cpp flatset/flatset.cpp)

  set_target_properties(spackexamplelib PROPERTIES
    PUBLIC_HEADER filesystem/filesystem.hpp
    PUBLIC_HEADER flatset/flatset.hpp
  )
  target_link_libraries(spackexamplelib Boost::filesystem)
  add_compile_definitions(ENABLE_BOOST)
endif()

if(ENABLE_YAML_CPP)
  find_package(yaml-cpp
    0.7.0
    REQUIRED
  )
  target_sources(spackexamplelib PRIVATE yamlParser/yamlParser.cpp)

  set_target_properties(spackexamplelib PROPERTIES
    PUBLIC_HEADER yamlParser/yamlParser.hpp
  )
  target_link_libraries(spackexamplelib yaml-cpp)
  add_compile_definitions(ENABLE_YAML_CPP)
endif()

include_directories(${YAML_CPP_INCLUDE_DIR})

add_executable(spackexample main.cpp)

target_link_libraries(spackexample spackexamplelib)

target_include_directories(spackexamplelib
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/spackexamplelib
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/spackexamplelib>
        $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}/spackexamplelib>
  )

# Create install targets
include(GNUInstallDirs)
install(TARGETS spackexample spackexamplelib
  LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
  ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
  RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
  PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/spackexample
  INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/spackexample
)
