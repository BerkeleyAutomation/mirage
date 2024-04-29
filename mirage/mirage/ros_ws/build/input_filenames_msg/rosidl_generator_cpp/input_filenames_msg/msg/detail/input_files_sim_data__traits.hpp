// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from input_filenames_msg:msg/InputFilesSimData.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_SIM_DATA__TRAITS_HPP_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_SIM_DATA__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "input_filenames_msg/msg/detail/input_files_sim_data__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'rgb'
#include "sensor_msgs/msg/detail/image__traits.hpp"

namespace input_filenames_msg
{

namespace msg
{

inline void to_flow_style_yaml(
  const InputFilesSimData & msg,
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

  // member: segmentation
  {
    if (msg.segmentation.size() == 0) {
      out << "segmentation: []";
    } else {
      out << "segmentation: [";
      size_t pending_items = msg.segmentation.size();
      for (auto item : msg.segmentation) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: ee_pose
  {
    if (msg.ee_pose.size() == 0) {
      out << "ee_pose: []";
    } else {
      out << "ee_pose: [";
      size_t pending_items = msg.ee_pose.size();
      for (auto item : msg.ee_pose) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: interpolated_gripper
  {
    if (msg.interpolated_gripper.size() == 0) {
      out << "interpolated_gripper: []";
    } else {
      out << "interpolated_gripper: [";
      size_t pending_items = msg.interpolated_gripper.size();
      for (auto item : msg.interpolated_gripper) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const InputFilesSimData & msg,
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

  // member: segmentation
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.segmentation.size() == 0) {
      out << "segmentation: []\n";
    } else {
      out << "segmentation:\n";
      for (auto item : msg.segmentation) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: ee_pose
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.ee_pose.size() == 0) {
      out << "ee_pose: []\n";
    } else {
      out << "ee_pose:\n";
      for (auto item : msg.ee_pose) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: interpolated_gripper
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.interpolated_gripper.size() == 0) {
      out << "interpolated_gripper: []\n";
    } else {
      out << "interpolated_gripper:\n";
      for (auto item : msg.interpolated_gripper) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const InputFilesSimData & msg, bool use_flow_style = false)
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
  const input_filenames_msg::msg::InputFilesSimData & msg,
  std::ostream & out, size_t indentation = 0)
{
  input_filenames_msg::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use input_filenames_msg::msg::to_yaml() instead")]]
inline std::string to_yaml(const input_filenames_msg::msg::InputFilesSimData & msg)
{
  return input_filenames_msg::msg::to_yaml(msg);
}

template<>
inline const char * data_type<input_filenames_msg::msg::InputFilesSimData>()
{
  return "input_filenames_msg::msg::InputFilesSimData";
}

template<>
inline const char * name<input_filenames_msg::msg::InputFilesSimData>()
{
  return "input_filenames_msg/msg/InputFilesSimData";
}

template<>
struct has_fixed_size<input_filenames_msg::msg::InputFilesSimData>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<input_filenames_msg::msg::InputFilesSimData>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<input_filenames_msg::msg::InputFilesSimData>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_SIM_DATA__TRAITS_HPP_
