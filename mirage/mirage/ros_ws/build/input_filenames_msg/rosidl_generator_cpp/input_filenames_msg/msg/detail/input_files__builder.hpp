// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from input_filenames_msg:msg/InputFiles.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES__BUILDER_HPP_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "input_filenames_msg/msg/detail/input_files__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace input_filenames_msg
{

namespace msg
{

namespace builder
{

class Init_InputFiles_joints
{
public:
  explicit Init_InputFiles_joints(::input_filenames_msg::msg::InputFiles & msg)
  : msg_(msg)
  {}
  ::input_filenames_msg::msg::InputFiles joints(::input_filenames_msg::msg::InputFiles::_joints_type arg)
  {
    msg_.joints = std::move(arg);
    return std::move(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFiles msg_;
};

class Init_InputFiles_segmentation
{
public:
  explicit Init_InputFiles_segmentation(::input_filenames_msg::msg::InputFiles & msg)
  : msg_(msg)
  {}
  Init_InputFiles_joints segmentation(::input_filenames_msg::msg::InputFiles::_segmentation_type arg)
  {
    msg_.segmentation = std::move(arg);
    return Init_InputFiles_joints(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFiles msg_;
};

class Init_InputFiles_depth_file
{
public:
  Init_InputFiles_depth_file()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_InputFiles_segmentation depth_file(::input_filenames_msg::msg::InputFiles::_depth_file_type arg)
  {
    msg_.depth_file = std::move(arg);
    return Init_InputFiles_segmentation(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFiles msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::input_filenames_msg::msg::InputFiles>()
{
  return input_filenames_msg::msg::builder::Init_InputFiles_depth_file();
}

}  // namespace input_filenames_msg

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES__BUILDER_HPP_
