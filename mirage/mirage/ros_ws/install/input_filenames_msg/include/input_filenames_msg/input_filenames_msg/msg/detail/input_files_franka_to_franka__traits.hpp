// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from input_filenames_msg:msg/InputFilesFrankaToFranka.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_FRANKA_TO_FRANKA__TRAITS_HPP_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_FRANKA_TO_FRANKA__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "input_filenames_msg/msg/detail/input_files_franka_to_franka__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'rgb'
#include "sensor_msgs/msg/detail/image__traits.hpp"
// Member 'demo_num'
// Member 'traj_num'
#include "std_msgs/msg/detail/int16__traits.hpp"

namespace input_filenames_msg
{

namespace msg
{

inline void to_flow_style_yaml(
  const InputFilesFrankaToFranka & msg,
  std::ostream & out)
{
  out << "{";
  // member: rgb
  {
    out << "rgb: ";
    to_flow_style_yaml(msg.rgb, out);
    out << ", ";
  }

  // member: joints
  {
    if (msg.joints.size() == 0) {
      out << "joints: []";
    } else {
      out << "joints: [";
      size_t pending_items = msg.joints.size();
      for (auto item : msg.joints) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: demo_num
  {
    out << "demo_num: ";
    to_flow_style_yaml(msg.demo_num, out);
    out << ", ";
  }

  // member: traj_num
  {
    out << "traj_num: ";
    to_flow_style_yaml(msg.traj_num, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const InputFilesFrankaToFranka & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: rgb
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "rgb:\n";
    to_block_style_yaml(msg.rgb, out, indentation + 2);
  }

  // member: joints
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.joints.size() == 0) {
      out << "joints: []\n";
    } else {
      out << "joints:\n";
      for (auto item : msg.joints) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: demo_num
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "demo_num:\n";
    to_block_style_yaml(msg.demo_num, out, indentation + 2);
  }

  // member: traj_num
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "traj_num:\n";
    to_block_style_yaml(msg.traj_num, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const InputFilesFrankaToFranka & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace input_filenames_msg

namespace rosidl_generator_traits
{

[[deprecated("use input_filenames_msg::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const input_filenames_msg::msg::InputFilesFrankaToFranka & msg,
  std::ostream & out, size_t indentation = 0)
{
  input_filenames_msg::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use input_filenames_msg::msg::to_yaml() instead")]]
inline std::string to_yaml(const input_filenames_msg::msg::InputFilesFrankaToFranka & msg)
{
  return input_filenames_msg::msg::to_yaml(msg);
}

template<>
inline const char * data_type<input_filenames_msg::msg::InputFilesFrankaToFranka>()
{
  return "input_filenames_msg::msg::InputFilesFrankaToFranka";
}

template<>
inline const char * name<input_filenames_msg::msg::InputFilesFrankaToFranka>()
{
  return "input_filenames_msg/msg/InputFilesFrankaToFranka";
}

template<>
struct has_fixed_size<input_filenames_msg::msg::InputFilesFrankaToFranka>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<input_filenames_msg::msg::InputFilesFrankaToFranka>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<input_filenames_msg::msg::InputFilesFrankaToFranka>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_FRANKA_TO_FRANKA__TRAITS_HPP_
