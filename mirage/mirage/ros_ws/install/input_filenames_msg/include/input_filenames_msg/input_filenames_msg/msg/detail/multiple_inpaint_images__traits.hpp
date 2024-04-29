// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from input_filenames_msg:msg/MultipleInpaintImages.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__MULTIPLE_INPAINT_IMAGES__TRAITS_HPP_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__MULTIPLE_INPAINT_IMAGES__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "input_filenames_msg/msg/detail/multiple_inpaint_images__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'images'
#include "sensor_msgs/msg/detail/image__traits.hpp"

namespace input_filenames_msg
{

namespace msg
{

inline void to_flow_style_yaml(
  const MultipleInpaintImages & msg,
  std::ostream & out)
{
  out << "{";
  // member: images
  {
    if (msg.images.size() == 0) {
      out << "images: []";
    } else {
      out << "images: [";
      size_t pending_items = msg.images.size();
      for (auto item : msg.images) {
        to_flow_style_yaml(item, out);
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
  const MultipleInpaintImages & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: images
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.images.size() == 0) {
      out << "images: []\n";
    } else {
      out << "images:\n";
      for (auto item : msg.images) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const MultipleInpaintImages & msg, bool use_flow_style = false)
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
  const input_filenames_msg::msg::MultipleInpaintImages & msg,
  std::ostream & out, size_t indentation = 0)
{
  input_filenames_msg::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use input_filenames_msg::msg::to_yaml() instead")]]
inline std::string to_yaml(const input_filenames_msg::msg::MultipleInpaintImages & msg)
{
  return input_filenames_msg::msg::to_yaml(msg);
}

template<>
inline const char * data_type<input_filenames_msg::msg::MultipleInpaintImages>()
{
  return "input_filenames_msg::msg::MultipleInpaintImages";
}

template<>
inline const char * name<input_filenames_msg::msg::MultipleInpaintImages>()
{
  return "input_filenames_msg/msg/MultipleInpaintImages";
}

template<>
struct has_fixed_size<input_filenames_msg::msg::MultipleInpaintImages>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<input_filenames_msg::msg::MultipleInpaintImages>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<input_filenames_msg::msg::MultipleInpaintImages>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__MULTIPLE_INPAINT_IMAGES__TRAITS_HPP_
