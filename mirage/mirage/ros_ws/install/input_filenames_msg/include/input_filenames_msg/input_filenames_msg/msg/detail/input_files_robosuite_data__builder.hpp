// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from input_filenames_msg:msg/InputFilesRobosuiteData.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_ROBOSUITE_DATA__BUILDER_HPP_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_ROBOSUITE_DATA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "input_filenames_msg/msg/detail/input_files_robosuite_data__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace input_filenames_msg
{

namespace msg
{

namespace builder
{

class Init_InputFilesRobosuiteData_joints
{
public:
  explicit Init_InputFilesRobosuiteData_joints(::input_filenames_msg::msg::InputFilesRobosuiteData & msg)
  : msg_(msg)
  {}
  ::input_filenames_msg::msg::InputFilesRobosuiteData joints(::input_filenames_msg::msg::InputFilesRobosuiteData::_joints_type arg)
  {
    msg_.joints = std::move(arg);
    return std::move(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesRobosuiteData msg_;
};

class Init_InputFilesRobosuiteData_segmentation
{
public:
  explicit Init_InputFilesRobosuiteData_segmentation(::input_filenames_msg::msg::InputFilesRobosuiteData & msg)
  : msg_(msg)
  {}
  Init_InputFilesRobosuiteData_joints segmentation(::input_filenames_msg::msg::InputFilesRobosuiteData::_segmentation_type arg)
  {
    msg_.segmentation = std::move(arg);
    return Init_InputFilesRobosuiteData_joints(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesRobosuiteData msg_;
};

class Init_InputFilesRobosuiteData_depth_map
{
public:
  explicit Init_InputFilesRobosuiteData_depth_map(::input_filenames_msg::msg::InputFilesRobosuiteData & msg)
  : msg_(msg)
  {}
  Init_InputFilesRobosuiteData_segmentation depth_map(::input_filenames_msg::msg::InputFilesRobosuiteData::_depth_map_type arg)
  {
    msg_.depth_map = std::move(arg);
    return Init_InputFilesRobosuiteData_segmentation(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesRobosuiteData msg_;
};

class Init_InputFilesRobosuiteData_rgb
{
public:
  Init_InputFilesRobosuiteData_rgb()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_InputFilesRobosuiteData_depth_map rgb(::input_filenames_msg::msg::InputFilesRobosuiteData::_rgb_type arg)
  {
    msg_.rgb = std::move(arg);
    return Init_InputFilesRobosuiteData_depth_map(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesRobosuiteData msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::input_filenames_msg::msg::InputFilesRobosuiteData>()
{
  return input_filenames_msg::msg::builder::Init_InputFilesRobosuiteData_rgb();
}

}  // namespace input_filenames_msg

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_ROBOSUITE_DATA__BUILDER_HPP_
