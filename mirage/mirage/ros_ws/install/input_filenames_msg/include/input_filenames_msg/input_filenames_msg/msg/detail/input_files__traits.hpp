// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from input_filenames_msg:msg/InputFiles.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES__TRAITS_HPP_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "input_filenames_msg/msg/detail/input_files__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace input_filenames_msg
{

namespace msg
{

inline void to_flow_style_yaml(
  const InputFiles & msg,
  std::ostream & out)
{
  out << "{";
  // member: depth_file
  {
    out << "depth_file: ";
    rosidl_generator_traits::value_to_yaml(msg.depth_file, out);
    out << ", ";
  }

  // member: segmentation
  {
    out << "segmentation: ";
    rosidl_generator_traits::value_to_yaml(msg.segmentation, out);
    out << ", ";
  }

  // member: joints
  {
    out << "joints: ";
    rosidl_generator_traits::value_to_yaml(msg.joints, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const InputFiles & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: depth_file
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "depth_file: ";
    rosidl_generator_traits::value_to_yaml(msg.depth_file, out);
    out << "\n";
  }

  // member: segmentation
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "segmentation: ";
    rosidl_generator_traits::value_to_yaml(msg.segmentation, out);
    out << "\n";
  }

  // member: joints
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "joints: ";
    rosidl_generator_traits::value_to_yaml(msg.joints, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const InputFiles & msg, bool use_flow_style = false)
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
  const input_filenames_msg::msg::InputFiles & msg,
  std::ostream & out, size_t indentation = 0)
{
  input_filenames_msg::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use input_filenames_msg::msg::to_yaml() instead")]]
inline std::string to_yaml(const input_filenames_msg::msg::InputFiles & msg)
{
  return input_filenames_msg::msg::to_yaml(msg);
}

template<>
inline const char * data_type<input_filenames_msg::msg::InputFiles>()
{
  return "input_filenames_msg::msg::InputFiles";
}

template<>
inline const char * name<input_filenames_msg::msg::InputFiles>()
{
  return "input_filenames_msg/msg/InputFiles";
}

template<>
struct has_fixed_size<input_filenames_msg::msg::InputFiles>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<input_filenames_msg::msg::InputFiles>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<input_filenames_msg::msg::InputFiles>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES__TRAITS_HPP_
