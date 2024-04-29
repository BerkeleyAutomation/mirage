// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from input_filenames_msg:msg/InputFilesRobosuite.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_ROBOSUITE__BUILDER_HPP_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_ROBOSUITE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "input_filenames_msg/msg/detail/input_files_robosuite__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace input_filenames_msg
{

namespace msg
{

namespace builder
{

class Init_InputFilesRobosuite_joints
{
public:
  explicit Init_InputFilesRobosuite_joints(::input_filenames_msg::msg::InputFilesRobosuite & msg)
  : msg_(msg)
  {}
  ::input_filenames_msg::msg::InputFilesRobosuite joints(::input_filenames_msg::msg::InputFilesRobosuite::_joints_type arg)
  {
    msg_.joints = std::move(arg);
    return std::move(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesRobosuite msg_;
};

class Init_InputFilesRobosuite_segmentation
{
public:
  explicit Init_InputFilesRobosuite_segmentation(::input_filenames_msg::msg::InputFilesRobosuite & msg)
  : msg_(msg)
  {}
  Init_InputFilesRobosuite_joints segmentation(::input_filenames_msg::msg::InputFilesRobosuite::_segmentation_type arg)
  {
    msg_.segmentation = std::move(arg);
    return Init_InputFilesRobosuite_joints(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesRobosuite msg_;
};

class Init_InputFilesRobosuite_depth
{
public:
  explicit Init_InputFilesRobosuite_depth(::input_filenames_msg::msg::InputFilesRobosuite & msg)
  : msg_(msg)
  {}
  Init_InputFilesRobosuite_segmentation depth(::input_filenames_msg::msg::InputFilesRobosuite::_depth_type arg)
  {
    msg_.depth = std::move(arg);
    return Init_InputFilesRobosuite_segmentation(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesRobosuite msg_;
};

class Init_InputFilesRobosuite_rgb
{
public:
  Init_InputFilesRobosuite_rgb()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_InputFilesRobosuite_depth rgb(::input_filenames_msg::msg::InputFilesRobosuite::_rgb_type arg)
  {
    msg_.rgb = std::move(arg);
    return Init_InputFilesRobosuite_depth(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesRobosuite msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::input_filenames_msg::msg::InputFilesRobosuite>()
{
  return input_filenames_msg::msg::builder::Init_InputFilesRobosuite_rgb();
}

}  // namespace input_filenames_msg

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_ROBOSUITE__BUILDER_HPP_
