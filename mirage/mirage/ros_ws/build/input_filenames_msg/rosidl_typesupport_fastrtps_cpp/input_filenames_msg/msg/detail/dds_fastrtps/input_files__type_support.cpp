// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from input_filenames_msg:msg/InputFiles.idl
// generated code does not contain a copyright notice
#include "input_filenames_msg/msg/detail/input_files__rosidl_typesupport_fastrtps_cpp.hpp"
#include "input_filenames_msg/msg/detail/input_files__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace input_filenames_msg
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_input_filenames_msg
cdr_serialize(
  const input_filenames_msg::msg::InputFiles & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: depth_file
  cdr << ros_message.depth_file;
  // Member: segmentation
  cdr << ros_message.segmentation;
  // Member: joints
  cdr << ros_message.joints;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_input_filenames_msg
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  input_filenames_msg::msg::InputFiles & ros_message)
{
  // Member: depth_file
  cdr >> ros_message.depth_file;

  // Member: segmentation
  cdr >> ros_message.segmentation;

  // Member: joints
  cdr >> ros_message.joints;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_input_filenames_msg
get_serialized_size(
  const input_filenames_msg::msg::InputFiles & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: depth_file
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message.depth_file.size() + 1);
  // Member: segmentation
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message.segmentation.size() + 1);
  // Member: joints
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message.joints.size() + 1);

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_input_filenames_msg
max_serialized_size_InputFiles(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;


  // Member: depth_file
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  // Member: segmentation
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  // Member: joints
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  return current_alignment - initial_alignment;
}

static bool _InputFiles__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const input_filenames_msg::msg::InputFiles *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _InputFiles__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<input_filenames_msg::msg::InputFiles *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _InputFiles__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const input_filenames_msg::msg::InputFiles *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _InputFiles__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_InputFiles(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _InputFiles__callbacks = {
  "input_filenames_msg::msg",
  "InputFiles",
  _InputFiles__cdr_serialize,
  _InputFiles__cdr_deserialize,
  _InputFiles__get_serialized_size,
  _InputFiles__max_serialized_size
};

static rosidl_message_type_support_t _InputFiles__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_InputFiles__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace input_filenames_msg

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_input_filenames_msg
const rosidl_message_type_support_t *
get_message_type_support_handle<input_filenames_msg::msg::InputFiles>()
{
  return &input_filenames_msg::msg::typesupport_fastrtps_cpp::_InputFiles__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, input_filenames_msg, msg, InputFiles)() {
  return &input_filenames_msg::msg::typesupport_fastrtps_cpp::_InputFiles__handle;
}

#ifdef __cplusplus
}
#endif
