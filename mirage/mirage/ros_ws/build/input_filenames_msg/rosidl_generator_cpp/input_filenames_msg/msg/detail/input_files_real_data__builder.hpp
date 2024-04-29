// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from input_filenames_msg:msg/InputFilesRealData.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_REAL_DATA__BUILDER_HPP_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_REAL_DATA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "input_filenames_msg/msg/detail/input_files_real_data__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace input_filenames_msg
{

namespace msg
{

namespace builder
{

class Init_InputFilesRealData_camera_name
{
public:
  explicit Init_InputFilesRealData_camera_name(::input_filenames_msg::msg::InputFilesRealData & msg)
  : msg_(msg)
  {}
  ::input_filenames_msg::msg::InputFilesRealData camera_name(::input_filenames_msg::msg::InputFilesRealData::_camera_name_type arg)
  {
    msg_.camera_name = std::move(arg);
    return std::move(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesRealData msg_;
};

class Init_InputFilesRealData_joints
{
public:
  explicit Init_InputFilesRealData_joints(::input_filenames_msg::msg::InputFilesRealData & msg)
  : msg_(msg)
  {}
  Init_InputFilesRealData_camera_name joints(::input_filenames_msg::msg::InputFilesRealData::_joints_type arg)
  {
    msg_.joints = std::move(arg);
    return Init_InputFilesRealData_camera_name(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesRealData msg_;
};

class Init_InputFilesRealData_depth_map
{
public:
  explicit Init_InputFilesRealData_depth_map(::input_filenames_msg::msg::InputFilesRealData & msg)
  : msg_(msg)
  {}
  Init_InputFilesRealData_joints depth_map(::input_filenames_msg::msg::InputFilesRealData::_depth_map_type arg)
  {
    msg_.depth_map = std::move(arg);
    return Init_InputFilesRealData_joints(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesRealData msg_;
};

class Init_InputFilesRealData_rgb
{
public:
  Init_InputFilesRealData_rgb()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_InputFilesRealData_depth_map rgb(::input_filenames_msg::msg::InputFilesRealData::_rgb_type arg)
  {
    msg_.rgb = std::move(arg);
    return Init_InputFilesRealData_depth_map(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesRealData msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::input_filenames_msg::msg::InputFilesRealData>()
{
  return input_filenames_msg::msg::builder::Init_InputFilesRealData_rgb();
}

}  // namespace input_filenames_msg

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_REAL_DATA__BUILDER_HPP_
