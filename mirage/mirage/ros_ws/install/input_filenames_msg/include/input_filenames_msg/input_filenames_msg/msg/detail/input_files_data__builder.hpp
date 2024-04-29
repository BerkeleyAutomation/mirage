// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from input_filenames_msg:msg/InputFilesData.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_DATA__BUILDER_HPP_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_DATA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "input_filenames_msg/msg/detail/input_files_data__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace input_filenames_msg
{

namespace msg
{

namespace builder
{

class Init_InputFilesData_joints
{
public:
  explicit Init_InputFilesData_joints(::input_filenames_msg::msg::InputFilesData & msg)
  : msg_(msg)
  {}
  ::input_filenames_msg::msg::InputFilesData joints(::input_filenames_msg::msg::InputFilesData::_joints_type arg)
  {
    msg_.joints = std::move(arg);
    return std::move(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesData msg_;
};

class Init_InputFilesData_segmentation_data
{
public:
  explicit Init_InputFilesData_segmentation_data(::input_filenames_msg::msg::InputFilesData & msg)
  : msg_(msg)
  {}
  Init_InputFilesData_joints segmentation_data(::input_filenames_msg::msg::InputFilesData::_segmentation_data_type arg)
  {
    msg_.segmentation_data = std::move(arg);
    return Init_InputFilesData_joints(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesData msg_;
};

class Init_InputFilesData_depth_data
{
public:
  Init_InputFilesData_depth_data()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_InputFilesData_segmentation_data depth_data(::input_filenames_msg::msg::InputFilesData::_depth_data_type arg)
  {
    msg_.depth_data = std::move(arg);
    return Init_InputFilesData_segmentation_data(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesData msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::input_filenames_msg::msg::InputFilesData>()
{
  return input_filenames_msg::msg::builder::Init_InputFilesData_depth_data();
}

}  // namespace input_filenames_msg

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_DATA__BUILDER_HPP_
