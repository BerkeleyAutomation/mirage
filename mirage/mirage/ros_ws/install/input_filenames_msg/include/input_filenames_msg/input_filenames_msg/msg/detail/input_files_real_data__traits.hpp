// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from input_filenames_msg:msg/InputFilesRealData.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_REAL_DATA__TRAITS_HPP_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_REAL_DATA__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "input_filenames_msg/msg/detail/input_files_real_data__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'rgb'
#include "sensor_msgs/msg/detail/image__traits.hpp"

namespace input_filenames_msg
{

namespace msg
{

inline void to_flow_style_yaml(
  const InputFilesRealData & msg,
  std::ostream & out)
{
  out << "{";
  // member: rgb
  {
    out << "rgb: ";
    to_flow_style_yaml(msg.rgb, out);
    out << ", ";
  }

  // member: depth_map
  {
    if (msg.depth_map.size() == 0) {
      out << "depth_map: []";
    } else {
      out << "depth_map: [";
      size_t pending_items = msg.depth_map.size();
      for (auto item : msg.depth_map) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
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

  // member: camera_name
  {
    out << "camera_name: ";
    rosidl_generator_traits::value_to_yaml(msg.camera_name, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const InputFilesRealData & msg,
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

  // member: depth_map
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.depth_map.size() == 0) {
      out << "depth_map: []\n";
    } else {
      out << "depth_map:\n";
      for (auto item : msg.depth_map) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
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

  // member: camera_name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "camera_name: ";
    rosidl_generator_traits::value_to_yaml(msg.camera_name, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const InputFilesRealData & msg, bool use_flow_style = false)
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
  const input_filenames_msg::msg::InputFilesRealData & msg,
  std::ostream & out, size_t indentation = 0)
{
  input_filenames_msg::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use input_filenames_msg::msg::to_yaml() instead")]]
inline std::string to_yaml(const input_filenames_msg::msg::InputFilesRealData & msg)
{
  return input_filenames_msg::msg::to_yaml(msg);
}

template<>
inline const char * data_type<input_filenames_msg::msg::InputFilesRealData>()
{
  return "input_filenames_msg::msg::InputFilesRealData";
}

template<>
inline const char * name<input_filenames_msg::msg::InputFilesRealData>()
{
  return "input_filenames_msg/msg/InputFilesRealData";
}

template<>
struct has_fixed_size<input_filenames_msg::msg::InputFilesRealData>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<input_filenames_msg::msg::InputFilesRealData>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<input_filenames_msg::msg::InputFilesRealData>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_REAL_DATA__TRAITS_HPP_
