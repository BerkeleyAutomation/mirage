# Install script for directory: /home/mirage/mirage/mirage/mirage/ros_ws/src/gazebo_env

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/mirage/mirage/mirage/mirage/ros_ws/install/gazebo_env")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/home/mirage/mambaforge/envs/mirage/bin/x86_64-conda-linux-gnu-objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gazebo_env" TYPE FILE FILES "/home/mirage/mirage/mirage/mirage/ros_ws/src/gazebo_env/ros2_control_demo_ur5e.xml")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gazebo_env" TYPE DIRECTORY FILES "/home/mirage/mirage/mirage/mirage/ros_ws/src/gazebo_env/meshes")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gazebo_env" TYPE DIRECTORY FILES "/home/mirage/mirage/mirage/mirage/ros_ws/src/gazebo_env/bringup/launch")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gazebo_env" TYPE DIRECTORY FILES "/home/mirage/mirage/mirage/mirage/ros_ws/src/gazebo_env/worlds")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gazebo_env" TYPE DIRECTORY FILES "/home/mirage/mirage/mirage/mirage/ros_ws/src/gazebo_env/description/urdf")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gazebo_env" TYPE DIRECTORY FILES "/home/mirage/mirage/mirage/mirage/ros_ws/src/gazebo_env/ur5e_description")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/gazebo_env" TYPE PROGRAM FILES "/home/mirage/mirage/mirage/mirage/ros_ws/src/gazebo_env/scripts/write_data_node_panda_gripper_to_panda_ur5_gripper_multi_real_better_early_inpaint_reproject.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/gazebo_env" TYPE PROGRAM FILES "/home/mirage/mirage/mirage/mirage/ros_ws/src/gazebo_env/scripts/write_data_node_panda_gripper_to_panda_ur5_gripper_multi_real_better_early_inpaint_reproject.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/gazebo_env" TYPE PROGRAM FILES "/home/mirage/mirage/mirage/mirage/ros_ws/src/gazebo_env/scripts/write_data_node_panda_gripper_to_panda_ur5_gripper_multi_real_better_wrist_early_inpaint.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/gazebo_env" TYPE PROGRAM FILES "/home/mirage/mirage/mirage/mirage/ros_ws/src/gazebo_env/scripts/read_data_node_input_files_real_data_node.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/gazebo_env" TYPE PROGRAM FILES "/home/mirage/mirage/mirage/mirage/ros_ws/src/gazebo_env/scripts/write_data_node_panda_ur5_gripper_to_panda_gripper_multi_real_better_wrist_early_inpaint.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/gazebo_env" TYPE PROGRAM FILES "/home/mirage/mirage/mirage/mirage/ros_ws/src/gazebo_env/scripts/write_data_node_ur5_to_panda_no_gripper_multi_real_better_reproject.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/gazebo_env" TYPE PROGRAM FILES "/home/mirage/mirage/mirage/mirage/ros_ws/src/gazebo_env/scripts/dummy_joint_command_publisher.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/gazebo_env" TYPE PROGRAM FILES "/home/mirage/mirage/mirage/mirage/ros_ws/src/gazebo_env/scripts/write_data_node_panda_ur5_gripper_to_panda_gripper_real_better_early_inpaint.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/gazebo_env" TYPE PROGRAM FILES "/home/mirage/mirage/mirage/mirage/ros_ws/src/gazebo_env/scripts/write_data_node_ur5_to_panda_no_gripper_multi_real_better_early_inpaint.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/gazebo_env" TYPE PROGRAM FILES "/home/mirage/mirage/mirage/mirage/ros_ws/src/gazebo_env/scripts/write_data_node_ur5_to_panda_gripper_multi_real_better_early_inpaint.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/gazebo_env" TYPE PROGRAM FILES "/home/mirage/mirage/mirage/mirage/ros_ws/src/gazebo_env/scripts/write_data_node_panda_ur5_gripper_to_panda_gripper_multi_real_better_early_inpaint.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/gazebo_env" TYPE PROGRAM FILES "/home/mirage/mirage/mirage/mirage/ros_ws/src/gazebo_env/scripts/write_data_node_panda_gripper_to_panda_ur5_gripper_multi_real_better_early_inpaint.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/gazebo_env" TYPE PROGRAM FILES "/home/mirage/mirage/mirage/mirage/ros_ws/src/gazebo_env/scripts/write_data_node_ur5_to_panda_no_gripper_multi_real_better.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/gazebo_env" TYPE PROGRAM FILES "/home/mirage/mirage/mirage/mirage/ros_ws/src/gazebo_env/scripts/reproject_test_node.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/gazebo_env" TYPE PROGRAM FILES "/home/mirage/mirage/mirage/mirage/ros_ws/src/gazebo_env/scripts/full_ur5_and_panda_no_gripper_joint_state_publisher_node.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/gazebo_env" TYPE PROGRAM FILES "/home/mirage/mirage/mirage/mirage/ros_ws/src/gazebo_env/scripts/full_ur5_and_panda_gripper_joint_state_publisher_node.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/gazebo_env" TYPE PROGRAM FILES "/home/mirage/mirage/mirage/mirage/ros_ws/src/gazebo_env/scripts/write_data_node_robosuite_better.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/gazebo_env" TYPE PROGRAM FILES "/home/mirage/mirage/mirage/mirage/ros_ws/src/gazebo_env/scripts/full_panda_joint_state_publisher_node.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/gazebo_env" TYPE PROGRAM FILES "/home/mirage/mirage/mirage/mirage/ros_ws/src/gazebo_env/scripts/panda_and_panda_grippers_joint_state_publisher_node.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gazebo_env/environment" TYPE FILE FILES "/home/mirage/mirage/mirage/mirage/ros_ws/build/gazebo_env/ament_cmake_environment_hooks/pythonpath.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gazebo_env/environment" TYPE FILE FILES "/home/mirage/mirage/mirage/mirage/ros_ws/build/gazebo_env/ament_cmake_environment_hooks/pythonpath.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3.10/site-packages/gazebo_env-0.0.0-py3.10.egg-info" TYPE DIRECTORY FILES "/home/mirage/mirage/mirage/mirage/ros_ws/build/gazebo_env/ament_cmake_python/gazebo_env/gazebo_env.egg-info/")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3.10/site-packages/gazebo_env" TYPE DIRECTORY FILES "/home/mirage/mirage/mirage/mirage/ros_ws/src/gazebo_env/gazebo_env/" REGEX "/[^/]*\\.pyc$" EXCLUDE REGEX "/\\_\\_pycache\\_\\_$" EXCLUDE)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(
        COMMAND
        "/home/mirage/mambaforge/envs/mirage/bin/python3.10" "-m" "compileall"
        "lib/python3.10/site-packages/gazebo_env"
      )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/package_run_dependencies" TYPE FILE FILES "/home/mirage/mirage/mirage/mirage/ros_ws/build/gazebo_env/ament_cmake_index/share/ament_index/resource_index/package_run_dependencies/gazebo_env")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/parent_prefix_path" TYPE FILE FILES "/home/mirage/mirage/mirage/mirage/ros_ws/build/gazebo_env/ament_cmake_index/share/ament_index/resource_index/parent_prefix_path/gazebo_env")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gazebo_env/environment" TYPE FILE FILES "/home/mirage/mambaforge/envs/mirage/share/ament_cmake_core/cmake/environment_hooks/environment/ament_prefix_path.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gazebo_env/environment" TYPE FILE FILES "/home/mirage/mirage/mirage/mirage/ros_ws/build/gazebo_env/ament_cmake_environment_hooks/ament_prefix_path.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gazebo_env/environment" TYPE FILE FILES "/home/mirage/mambaforge/envs/mirage/share/ament_cmake_core/cmake/environment_hooks/environment/path.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gazebo_env/environment" TYPE FILE FILES "/home/mirage/mirage/mirage/mirage/ros_ws/build/gazebo_env/ament_cmake_environment_hooks/path.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gazebo_env" TYPE FILE FILES "/home/mirage/mirage/mirage/mirage/ros_ws/build/gazebo_env/ament_cmake_environment_hooks/local_setup.bash")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gazebo_env" TYPE FILE FILES "/home/mirage/mirage/mirage/mirage/ros_ws/build/gazebo_env/ament_cmake_environment_hooks/local_setup.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gazebo_env" TYPE FILE FILES "/home/mirage/mirage/mirage/mirage/ros_ws/build/gazebo_env/ament_cmake_environment_hooks/local_setup.zsh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gazebo_env" TYPE FILE FILES "/home/mirage/mirage/mirage/mirage/ros_ws/build/gazebo_env/ament_cmake_environment_hooks/local_setup.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gazebo_env" TYPE FILE FILES "/home/mirage/mirage/mirage/mirage/ros_ws/build/gazebo_env/ament_cmake_environment_hooks/package.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/packages" TYPE FILE FILES "/home/mirage/mirage/mirage/mirage/ros_ws/build/gazebo_env/ament_cmake_index/share/ament_index/resource_index/packages/gazebo_env")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/hardware_interface__pluginlib__plugin" TYPE FILE FILES "/home/mirage/mirage/mirage/mirage/ros_ws/build/gazebo_env/ament_cmake_index/share/ament_index/resource_index/hardware_interface__pluginlib__plugin/gazebo_env")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gazebo_env/cmake" TYPE FILE FILES "/home/mirage/mirage/mirage/mirage/ros_ws/build/gazebo_env/ament_cmake_export_dependencies/ament_cmake_export_dependencies-extras.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gazebo_env/cmake" TYPE FILE FILES
    "/home/mirage/mirage/mirage/mirage/ros_ws/build/gazebo_env/ament_cmake_core/gazebo_envConfig.cmake"
    "/home/mirage/mirage/mirage/mirage/ros_ws/build/gazebo_env/ament_cmake_core/gazebo_envConfig-version.cmake"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gazebo_env" TYPE FILE FILES "/home/mirage/mirage/mirage/mirage/ros_ws/src/gazebo_env/package.xml")
endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/mirage/mirage/mirage/mirage/ros_ws/build/gazebo_env/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
