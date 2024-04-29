// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from input_filenames_msg:msg/InputFilesSimData.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_SIM_DATA__BUILDER_HPP_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_SIM_DATA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "input_filenames_msg/msg/detail/input_files_sim_data__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace input_filenames_msg
{

namespace msg
{

namespace builder
{

class Init_InputFilesSimData_interpolated_gripper
{
public:
  explicit Init_InputFilesSimData_interpolated_gripper(::input_filenames_msg::msg::InputFilesSimData & msg)
  : msg_(msg)
  {}
  ::input_filenames_msg::msg::InputFilesSimData interpolated_gripper(::input_filenames_msg::msg::InputFilesSimData::_interpolated_gripper_type arg)
  {
    msg_.interpolated_gripper = std::move(arg);
    return std::move(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesSimData msg_;
};

class Init_InputFilesSimData_ee_pose
{
public:
  explicit Init_InputFilesSimData_ee_pose(::input_filenames_msg::msg::InputFilesSimData & msg)
  : msg_(msg)
  {}
  Init_InputFilesSimData_interpolated_gripper ee_pose(::input_filenames_msg::msg::InputFilesSimData::_ee_pose_type arg)
  {
    msg_.ee_pose = std::move(arg);
    return Init_InputFilesSimData_interpolated_gripper(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesSimData msg_;
};

class Init_InputFilesSimData_segmentation
{
public:
  explicit Init_InputFilesSimData_segmentation(::input_filenames_msg::msg::InputFilesSimData & msg)
  : msg_(msg)
  {}
  Init_InputFilesSimData_ee_pose segmentation(::input_filenames_msg::msg::InputFilesSimData::_segmentation_type arg)
  {
    msg_.segmentation = std::move(arg);
    return Init_InputFilesSimData_ee_pose(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesSimData msg_;
};

class Init_InputFilesSimData_depth_map
{
public:
  explicit Init_InputFilesSimData_depth_map(::input_filenames_msg::msg::InputFilesSimData & msg)
  : msg_(msg)
  {}
  Init_InputFilesSimData_segmentation depth_map(::input_filenames_msg::msg::InputFilesSimData::_depth_map_type arg)
  {
    msg_.depth_map = std::move(arg);
    return Init_InputFilesSimData_segmentation(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesSimData msg_;
};

class Init_InputFilesSimData_rgb
{
public:
  Init_InputFilesSimData_rgb()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_InputFilesSimData_depth_map rgb(::input_filenames_msg::msg::InputFilesSimData::_rgb_type arg)
  {
    msg_.rgb = std::move(arg);
    return Init_InputFilesSimData_depth_map(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesSimData msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::input_filenames_msg::msg::InputFilesSimData>()
{
  return input_filenames_msg::msg::builder::Init_InputFilesSimData_rgb();
}

}  // namespace input_filenames_msg

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_SIM_DATA__BUILDER_HPP_
