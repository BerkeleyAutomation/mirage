cmake_minimum_required(VERSION 3.8)
project(gazebo_env)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
set(THIS_PACKAGE_INCLUDE_DEPENDS
  hardware_interface
  pluginlib
  rclcpp
  rclcpp_lifecycle
)

# Find dependencies
set (CMAKE_PREFIX_PATH "/home/benchturtle/opencv_build")
find_package ( OpenCV REQUIRED)
find_package(ament_cmake REQUIRED)
foreach(Dependency IN ITEMS ${THIS_PACKAGE_INCLUDE_DEPENDS})
  find_package(${Dependency} REQUIRED)
endforeach()
find_package(ament_cmake_python REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(message_filters REQUIRED)
find_package(cv_bridge REQUIRED)

# Find Gazebo
find_package(gazebo REQUIRED)
find_package(gazebo_dev REQUIRED)
find_package(gazebo_ros REQUIRED)

include_directories(${GAZEBO_INCLUDE_DIRS})
link_directories(${GAZEBO_LIBRARY_DIRS})
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${GAZEBO_CXX_FLAGS}")

# Build our plugin
add_library(no_physics_plugin SHARED no_physics_plugin/no_physics_plugin.cc)
ament_target_dependencies(no_physics_plugin
  "gazebo_dev"
  "gazebo_ros"
  "rclcpp"
  "std_msgs"
)
target_link_libraries(no_physics_plugin ${GAZEBO_LIBRARIES})

add_library(ur5e_control_plugin SHARED ur5e_control_plugin/ur5e_control_plugin.cc)
ament_target_dependencies(ur5e_control_plugin
  "gazebo_dev"
  "gazebo_ros"
  "rclcpp"
  "std_msgs"
)
target_link_libraries(ur5e_control_plugin ${GAZEBO_LIBRARIES})

add_library(panda_control_plugin SHARED panda_control_plugin/panda_control_plugin.cc)
ament_target_dependencies(panda_control_plugin
  "gazebo_dev"
  "gazebo_ros"
  "rclcpp"
  "std_msgs"
  "sensor_msgs"
  "message_filters"
  "cv_bridge"
)
target_link_libraries(panda_control_plugin ${GAZEBO_LIBRARIES} ${OpenCV_LIBS})

add_library(panda_no_gripper_control_plugin SHARED panda_no_gripper_control_plugin/panda_no_gripper_control_plugin.cc)
ament_target_dependencies(panda_no_gripper_control_plugin
  "gazebo_dev"
  "gazebo_ros"
  "rclcpp"
  "std_msgs"
  "sensor_msgs"
  "message_filters"
  "cv_bridge"
)
target_link_libraries(panda_no_gripper_control_plugin ${GAZEBO_LIBRARIES} ${OpenCV_LIBS})

add_library(ur5_and_panda_no_gripper_control_plugin SHARED ur5_and_panda_no_gripper_control_plugin/ur5_and_panda_no_gripper_control_plugin.cc)
ament_target_dependencies(ur5_and_panda_no_gripper_control_plugin
  "gazebo_dev"
  "gazebo_ros"
  "rclcpp"
  "std_msgs"
  "sensor_msgs"
  "message_filters"
  "cv_bridge"
)
target_link_libraries(ur5_and_panda_no_gripper_control_plugin ${GAZEBO_LIBRARIES} ${OpenCV_LIBS})

add_library(ur5_and_panda_gripper_control_plugin SHARED ur5_and_panda_gripper_control_plugin/ur5_and_panda_gripper_control_plugin.cc)
ament_target_dependencies(ur5_and_panda_gripper_control_plugin
  "gazebo_dev"
  "gazebo_ros"
  "rclcpp"
  "std_msgs"
  "sensor_msgs"
  "message_filters"
  "cv_bridge"
)
target_link_libraries(ur5_and_panda_gripper_control_plugin ${GAZEBO_LIBRARIES} ${OpenCV_LIBS})

add_library(panda_control_ur5e_gripper_real_plugin SHARED panda_control_ur5e_gripper_real_plugin/panda_control_ur5e_gripper_real_plugin.cc)
ament_target_dependencies(panda_control_ur5e_gripper_real_plugin
  "gazebo_dev"
  "gazebo_ros"
  "rclcpp"
  "std_msgs"
  "sensor_msgs"
  "message_filters"
  "cv_bridge"
)
target_link_libraries(panda_control_ur5e_gripper_real_plugin ${GAZEBO_LIBRARIES} ${OpenCV_LIBS})

add_library(panda_and_panda_grippers_control_plugin SHARED panda_and_panda_grippers_control_plugin/panda_and_panda_grippers_control_plugin.cc)
ament_target_dependencies(panda_and_panda_grippers_control_plugin
  "gazebo_dev"
  "gazebo_ros"
  "rclcpp"
  "std_msgs"
  "sensor_msgs"
  "message_filters"
  "cv_bridge"
)
target_link_libraries(panda_and_panda_grippers_control_plugin ${GAZEBO_LIBRARIES} ${OpenCV_LIBS})

add_library(panda_and_panda_grippers_early_inpaint_control_plugin SHARED panda_and_panda_grippers_early_inpaint_control_plugin/panda_and_panda_grippers_early_inpaint_control_plugin.cc)
ament_target_dependencies(panda_and_panda_grippers_early_inpaint_control_plugin
  "gazebo_dev"
  "gazebo_ros"
  "rclcpp"
  "std_msgs"
  "sensor_msgs"
  "message_filters"
  "cv_bridge"
)
target_link_libraries(panda_and_panda_grippers_early_inpaint_control_plugin ${GAZEBO_LIBRARIES} ${OpenCV_LIBS})

add_library(gripper_control_plugin SHARED gripper_control_plugin/gripper_control_plugin.cc)
ament_target_dependencies(gripper_control_plugin
  "gazebo_dev"
  "gazebo_ros"
  "rclcpp"
  "std_msgs"
)
target_link_libraries(gripper_control_plugin ${GAZEBO_LIBRARIES})


# Include Cpp "include" directory
include_directories(include
${gazebo_dev_INCLUDE_DIRS}
${gazebo_ros_INCLUDE_DIRS})

## COMPILE
add_library(
  gazebo_env
  SHARED
  hardware/urbot.cpp
  #hardware/rrbot.cpp
)

target_compile_features(gazebo_env PUBLIC cxx_std_17)
target_include_directories(gazebo_env PUBLIC
$<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/hardware/include>
$<INSTALL_INTERFACE:include/gazebo_env>
)
ament_target_dependencies(
  gazebo_env PUBLIC
  ${THIS_PACKAGE_INCLUDE_DEPENDS}
)

target_compile_definitions(${PROJECT_NAME} PRIVATE "GAZEBO_ENV_BUILDING_DLL")
pluginlib_export_plugin_description_file(hardware_interface ros2_control_demo_ur5e.xml)

# INSTALL
install(
  DIRECTORY hardware/include/
  DESTINATION include/gazebo_env
)
install(
  DIRECTORY meshes
  DESTINATION share/gazebo_env
)

install(
  DIRECTORY worlds
  DESTINATION share/gazebo_env
)

install(
  DIRECTORY description/urdf
  DESTINATION share/gazebo_env
)
install(
  DIRECTORY ur5e_description
  DESTINATION share/gazebo_env
)
install(
  DIRECTORY bringup/launch bringup/config
  DESTINATION share/gazebo_env
)
install(TARGETS gazebo_env
  EXPORT export_gazebo_env
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin
)
install(PROGRAMS
  scripts/ee_pose.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/panda_point_cloud_publisher.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/read_data_node.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/write_data_node.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/read_data_node_real_ur5_check.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/write_data_node_ur5_to_panda_no_gripper_real_better.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/write_data_node_panda_ur5_gripper_to_panda_gripper_real_better.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/write_data_node_panda_ur5_gripper_to_panda_gripper_real_better_early_inpaint.py
  DESTINATION lib/${PROJECT_NAME}
)



install(PROGRAMS
  scripts/read_data_node_real_multi_ur5_check.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/write_data_node_panda_gripper_to_panda_ur5_gripper_real_better.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/panda_no_gripper_joint_command_publisher.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/write_data_node_ur5_to_panda_no_gripper_multi_real_better.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/write_data_node_panda_gripper_to_panda_ur5_gripper_multi_real_better.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/write_data_node_panda_ur5_gripper_to_panda_gripper_multi_real_better.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/write_data_node_ur5_to_panda_gripper_multi_real_better.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/write_data_node_ur5_to_panda_gripper_multi_real_better.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/write_data_node_ur5_to_panda_gripper_real_better.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/read_data_node_robosuite.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/reproject_test_node.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/read_data_node_real_franka_check2.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/full_ur5_and_panda_no_gripper_joint_state_publisher_node.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/full_ur5_and_panda_gripper_joint_state_publisher_node.py
  DESTINATION lib/${PROJECT_NAME}
)


install(PROGRAMS
  scripts/read_data_node_robosuite_better.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/read_data_node_robosuite_diffusion_better.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/read_data_node_robosuite_franka_to_franka.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/read_data_node_robosuite_franka_to_franka_better.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/write_data_node_robosuite.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/write_data_node_robosuite_better.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/write_data_node_panda_to_ur5_no_gripper_real_better.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/write_data_node_robosuite_diffusion_better.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/write_data_node_robosuite_franka_to_franka.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/write_data_node_robosuite_franka_to_franka_better.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/ur5e_point_cloud_publisher.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/panda_joint_command_publisher.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/panda_ur5_gripper_real_joint_command_publisher.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/ur5e_joint_command_publisher.py
  DESTINATION lib/${PROJECT_NAME}
)
install(PROGRAMS
  scripts/full_ur5e_joint_state_publisher_node.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/full_panda_joint_state_publisher_node.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/real_offline_check_node.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/panda_and_panda_grippers_joint_state_publisher_node.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/gripper_joint_state_publisher_node.py
  DESTINATION lib/${PROJECT_NAME}
)
install(PROGRAMS
  scripts/gazebo_image_test.py
  DESTINATION lib/${PROJECT_NAME}
)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

# Install Python modules
ament_python_install_package(${PROJECT_NAME})

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_export_targets(export_gazebo_env HAS_LIBRARY_TARGET)
ament_export_dependencies(${THIS_PACKAGE_INCLUDE_DEPENDS})
ament_package()
