// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from input_filenames_msg:msg/InputFilesFrankaToFranka.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_FRANKA_TO_FRANKA__BUILDER_HPP_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_FRANKA_TO_FRANKA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "input_filenames_msg/msg/detail/input_files_franka_to_franka__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace input_filenames_msg
{

namespace msg
{

namespace builder
{

class Init_InputFilesFrankaToFranka_traj_num
{
public:
  explicit Init_InputFilesFrankaToFranka_traj_num(::input_filenames_msg::msg::InputFilesFrankaToFranka & msg)
  : msg_(msg)
  {}
  ::input_filenames_msg::msg::InputFilesFrankaToFranka traj_num(::input_filenames_msg::msg::InputFilesFrankaToFranka::_traj_num_type arg)
  {
    msg_.traj_num = std::move(arg);
    return std::move(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesFrankaToFranka msg_;
};

class Init_InputFilesFrankaToFranka_demo_num
{
public:
  explicit Init_InputFilesFrankaToFranka_demo_num(::input_filenames_msg::msg::InputFilesFrankaToFranka & msg)
  : msg_(msg)
  {}
  Init_InputFilesFrankaToFranka_traj_num demo_num(::input_filenames_msg::msg::InputFilesFrankaToFranka::_demo_num_type arg)
  {
    msg_.demo_num = std::move(arg);
    return Init_InputFilesFrankaToFranka_traj_num(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesFrankaToFranka msg_;
};

class Init_InputFilesFrankaToFranka_joints
{
public:
  explicit Init_InputFilesFrankaToFranka_joints(::input_filenames_msg::msg::InputFilesFrankaToFranka & msg)
  : msg_(msg)
  {}
  Init_InputFilesFrankaToFranka_demo_num joints(::input_filenames_msg::msg::InputFilesFrankaToFranka::_joints_type arg)
  {
    msg_.joints = std::move(arg);
    return Init_InputFilesFrankaToFranka_demo_num(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesFrankaToFranka msg_;
};

class Init_InputFilesFrankaToFranka_rgb
{
public:
  Init_InputFilesFrankaToFranka_rgb()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_InputFilesFrankaToFranka_joints rgb(::input_filenames_msg::msg::InputFilesFrankaToFranka::_rgb_type arg)
  {
    msg_.rgb = std::move(arg);
    return Init_InputFilesFrankaToFranka_joints(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesFrankaToFranka msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::input_filenames_msg::msg::InputFilesFrankaToFranka>()
{
  return input_filenames_msg::msg::builder::Init_InputFilesFrankaToFranka_rgb();
}

}  // namespace input_filenames_msg

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_FRANKA_TO_FRANKA__BUILDER_HPP_
