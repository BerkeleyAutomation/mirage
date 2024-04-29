// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from input_filenames_msg:msg/InputFilesRealDataMulti.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_REAL_DATA_MULTI__TRAITS_HPP_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_REAL_DATA_MULTI__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "input_filenames_msg/msg/detail/input_files_real_data_multi__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'data_pieces'
#include "input_filenames_msg/msg/detail/input_files_real_data__traits.hpp"

namespace input_filenames_msg
{

namespace msg
{

inline void to_flow_style_yaml(
  const InputFilesRealDataMulti & msg,
  std::ostream & out)
{
  out << "{";
  // member: data_pieces
  {
    if (msg.data_pieces.size() == 0) {
      out << "data_pieces: []";
    } else {
      out << "data_pieces: [";
      size_t pending_items = msg.data_pieces.size();
      for (auto item : msg.data_pieces) {
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
  const InputFilesRealDataMulti & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: data_pieces
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.data_pieces.size() == 0) {
      out << "data_pieces: []\n";
    } else {
      out << "data_pieces:\n";
      for (auto item : msg.data_pieces) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const InputFilesRealDataMulti & msg, bool use_flow_style = false)
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
  const input_filenames_msg::msg::InputFilesRealDataMulti & msg,
  std::ostream & out, size_t indentation = 0)
{
  input_filenames_msg::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use input_filenames_msg::msg::to_yaml() instead")]]
inline std::string to_yaml(const input_filenames_msg::msg::InputFilesRealDataMulti & msg)
{
  return input_filenames_msg::msg::to_yaml(msg);
}

template<>
inline const char * data_type<input_filenames_msg::msg::InputFilesRealDataMulti>()
{
  return "input_filenames_msg::msg::InputFilesRealDataMulti";
}

template<>
inline const char * name<input_filenames_msg::msg::InputFilesRealDataMulti>()
{
  return "input_filenames_msg/msg/InputFilesRealDataMulti";
}

template<>
struct has_fixed_size<input_filenames_msg::msg::InputFilesRealDataMulti>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<input_filenames_msg::msg::InputFilesRealDataMulti>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<input_filenames_msg::msg::InputFilesRealDataMulti>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_REAL_DATA_MULTI__TRAITS_HPP_
