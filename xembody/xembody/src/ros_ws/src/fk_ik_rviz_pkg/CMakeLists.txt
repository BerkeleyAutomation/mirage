cmake_minimum_required(VERSION 3.16)
project(fk_ik_rviz_pkg LANGUAGES CXX)

if(CMAKE_CXX_COMPILER_ID MATCHES "(GNU|Clang)")
  add_compile_options(-Wall -Wextra)
endif()

# find dependencies
set(THIS_PACKAGE_INCLUDE_DEPENDS
  hardware_interface
  pluginlib
  rclcpp
  rclcpp_lifecycle
)

# find dependencies
find_package(ament_cmake REQUIRED)
foreach(Dependency IN ITEMS ${THIS_PACKAGE_INCLUDE_DEPENDS})
  find_package(${Dependency} REQUIRED)
endforeach()


## COMPILE
add_library(
  fk_ik_rviz_pkg
  SHARED
  hardware/rrbot.cpp
)
target_compile_features(fk_ik_rviz_pkg PUBLIC cxx_std_17)
target_include_directories(fk_ik_rviz_pkg PUBLIC
$<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/hardware/include>
$<INSTALL_INTERFACE:include/fk_ik_rviz_pkg>
)
ament_target_dependencies(
  fk_ik_rviz_pkg PUBLIC
  ${THIS_PACKAGE_INCLUDE_DEPENDS}
)

# Causes the visibility macros to use dllexport rather than dllimport,
# which is appropriate when building the dll but not consuming it.
target_compile_definitions(${PROJECT_NAME} PRIVATE "fk_ik_rviz_pkg_BUILDING_DLL")

# Export hardware plugins
pluginlib_export_plugin_description_file(hardware_interface fk_ik_rviz_pkg.xml)

# INSTALL
install(
  DIRECTORY hardware/include/
  DESTINATION include/fk_ik_rviz_pkg
)
install(
  DIRECTORY description/ros2_control description/urdf description/rviz
  DESTINATION share/fk_ik_rviz_pkg
)
install(
  DIRECTORY bringup/launch bringup/config
  DESTINATION share/fk_ik_rviz_pkg
)
install(TARGETS fk_ik_rviz_pkg
  EXPORT export_fk_ik_rviz_pkg
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin
)

if(BUILD_TESTING)
  find_package(ament_cmake_gtest REQUIRED)
endif()

## EXPORTS
ament_export_targets(export_fk_ik_rviz_pkg HAS_LIBRARY_TARGET)
ament_export_dependencies(${THIS_PACKAGE_INCLUDE_DEPENDS})
ament_package()
