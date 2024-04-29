// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from input_filenames_msg:msg/InputFilesDiffusionData.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_DIFFUSION_DATA__BUILDER_HPP_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_DIFFUSION_DATA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "input_filenames_msg/msg/detail/input_files_diffusion_data__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace input_filenames_msg
{

namespace msg
{

namespace builder
{

class Init_InputFilesDiffusionData_traj_num
{
public:
  explicit Init_InputFilesDiffusionData_traj_num(::input_filenames_msg::msg::InputFilesDiffusionData & msg)
  : msg_(msg)
  {}
  ::input_filenames_msg::msg::InputFilesDiffusionData traj_num(::input_filenames_msg::msg::InputFilesDiffusionData::_traj_num_type arg)
  {
    msg_.traj_num = std::move(arg);
    return std::move(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesDiffusionData msg_;
};

class Init_InputFilesDiffusionData_demo_num
{
public:
  explicit Init_InputFilesDiffusionData_demo_num(::input_filenames_msg::msg::InputFilesDiffusionData & msg)
  : msg_(msg)
  {}
  Init_InputFilesDiffusionData_traj_num demo_num(::input_filenames_msg::msg::InputFilesDiffusionData::_demo_num_type arg)
  {
    msg_.demo_num = std::move(arg);
    return Init_InputFilesDiffusionData_traj_num(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesDiffusionData msg_;
};

class Init_InputFilesDiffusionData_joints
{
public:
  explicit Init_InputFilesDiffusionData_joints(::input_filenames_msg::msg::InputFilesDiffusionData & msg)
  : msg_(msg)
  {}
  Init_InputFilesDiffusionData_demo_num joints(::input_filenames_msg::msg::InputFilesDiffusionData::_joints_type arg)
  {
    msg_.joints = std::move(arg);
    return Init_InputFilesDiffusionData_demo_num(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesDiffusionData msg_;
};

class Init_InputFilesDiffusionData_segmentation
{
public:
  explicit Init_InputFilesDiffusionData_segmentation(::input_filenames_msg::msg::InputFilesDiffusionData & msg)
  : msg_(msg)
  {}
  Init_InputFilesDiffusionData_joints segmentation(::input_filenames_msg::msg::InputFilesDiffusionData::_segmentation_type arg)
  {
    msg_.segmentation = std::move(arg);
    return Init_InputFilesDiffusionData_joints(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesDiffusionData msg_;
};

class Init_InputFilesDiffusionData_depth_map
{
public:
  explicit Init_InputFilesDiffusionData_depth_map(::input_filenames_msg::msg::InputFilesDiffusionData & msg)
  : msg_(msg)
  {}
  Init_InputFilesDiffusionData_segmentation depth_map(::input_filenames_msg::msg::InputFilesDiffusionData::_depth_map_type arg)
  {
    msg_.depth_map = std::move(arg);
    return Init_InputFilesDiffusionData_segmentation(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesDiffusionData msg_;
};

class Init_InputFilesDiffusionData_rgb
{
public:
  Init_InputFilesDiffusionData_rgb()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_InputFilesDiffusionData_depth_map rgb(::input_filenames_msg::msg::InputFilesDiffusionData::_rgb_type arg)
  {
    msg_.rgb = std::move(arg);
    return Init_InputFilesDiffusionData_depth_map(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesDiffusionData msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::input_filenames_msg::msg::InputFilesDiffusionData>()
{
  return input_filenames_msg::msg::builder::Init_InputFilesDiffusionData_rgb();
}

}  // namespace input_filenames_msg

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_DIFFUSION_DATA__BUILDER_HPP_
