// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from input_filenames_msg:msg/InputFilesDiffusionData.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_DIFFUSION_DATA__TRAITS_HPP_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_DIFFUSION_DATA__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "input_filenames_msg/msg/detail/input_files_diffusion_data__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'segmentation'
#include "sensor_msgs/msg/detail/image__traits.hpp"
// Member 'demo_num'
// Member 'traj_num'
#include "std_msgs/msg/detail/int16__traits.hpp"

namespace input_filenames_msg
{

namespace msg
{

inline void to_flow_style_yaml(
  const InputFilesDiffusionData & msg,
  std::ostream & out)
{
  out << "{";
  // member: rgb
  {
    if (msg.rgb.size() == 0) {
      out << "rgb: []";
    } else {
      out << "rgb: [";
      size_t pending_items = msg.rgb.size();
      for (auto item : msg.rgb) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
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

  // member: segmentation
  {
    out << "segmentation: ";
    to_flow_style_yaml(msg.segmentation, out);
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
  const InputFilesDiffusionData & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: rgb
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.rgb.size() == 0) {
      out << "rgb: []\n";
    } else {
      out << "rgb:\n";
      for (auto item : msg.rgb) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
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

  // member: segmentation
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "segmentation:\n";
    to_block_style_yaml(msg.segmentation, out, indentation + 2);
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

inline std::string to_yaml(const InputFilesDiffusionData & msg, bool use_flow_style = false)
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
  const input_filenames_msg::msg::InputFilesDiffusionData & msg,
  std::ostream & out, size_t indentation = 0)
{
  input_filenames_msg::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use input_filenames_msg::msg::to_yaml() instead")]]
inline std::string to_yaml(const input_filenames_msg::msg::InputFilesDiffusionData & msg)
{
  return input_filenames_msg::msg::to_yaml(msg);
}

template<>
inline const char * data_type<input_filenames_msg::msg::InputFilesDiffusionData>()
{
  return "input_filenames_msg::msg::InputFilesDiffusionData";
}

template<>
inline const char * name<input_filenames_msg::msg::InputFilesDiffusionData>()
{
  return "input_filenames_msg/msg/InputFilesDiffusionData";
}

template<>
struct has_fixed_size<input_filenames_msg::msg::InputFilesDiffusionData>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<input_filenames_msg::msg::InputFilesDiffusionData>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<input_filenames_msg::msg::InputFilesDiffusionData>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_DIFFUSION_DATA__TRAITS_HPP_
