// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from input_filenames_msg:msg/InputFiles.idl
// generated code does not contain a copyright notice
#include "input_filenames_msg/msg/detail/input_files__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "input_filenames_msg/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "input_filenames_msg/msg/detail/input_files__struct.h"
#include "input_filenames_msg/msg/detail/input_files__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "rosidl_runtime_c/string.h"  // depth_file, joints, segmentation
#include "rosidl_runtime_c/string_functions.h"  // depth_file, joints, segmentation

// forward declare type support functions


using _InputFiles__ros_msg_type = input_filenames_msg__msg__InputFiles;

static bool _InputFiles__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _InputFiles__ros_msg_type * ros_message = static_cast<const _InputFiles__ros_msg_type *>(untyped_ros_message);
  // Field name: depth_file
  {
    const rosidl_runtime_c__String * str = &ros_message->depth_file;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  // Field name: segmentation
  {
    const rosidl_runtime_c__String * str = &ros_message->segmentation;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  // Field name: joints
  {
    const rosidl_runtime_c__String * str = &ros_message->joints;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  return true;
}

static bool _InputFiles__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _InputFiles__ros_msg_type * ros_message = static_cast<_InputFiles__ros_msg_type *>(untyped_ros_message);
  // Field name: depth_file
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->depth_file.data) {
      rosidl_runtime_c__String__init(&ros_message->depth_file);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->depth_file,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'depth_file'\n");
      return false;
    }
  }

  // Field name: segmentation
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->segmentation.data) {
      rosidl_runtime_c__String__init(&ros_message->segmentation);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->segmentation,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'segmentation'\n");
      return false;
    }
  }

  // Field name: joints
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->joints.data) {
      rosidl_runtime_c__String__init(&ros_message->joints);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->joints,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'joints'\n");
      return false;
    }
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_input_filenames_msg
size_t get_serialized_size_input_filenames_msg__msg__InputFiles(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _InputFiles__ros_msg_type * ros_message = static_cast<const _InputFiles__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name depth_file
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->depth_file.size + 1);
  // field.name segmentation
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->segmentation.size + 1);
  // field.name joints
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->joints.size + 1);

  return current_alignment - initial_alignment;
}

static uint32_t _InputFiles__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_input_filenames_msg__msg__InputFiles(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_input_filenames_msg
size_t max_serialized_size_input_filenames_msg__msg__InputFiles(
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

  // member: depth_file
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
  // member: segmentation
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
  // member: joints
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

static size_t _InputFiles__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_input_filenames_msg__msg__InputFiles(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_InputFiles = {
  "input_filenames_msg::msg",
  "InputFiles",
  _InputFiles__cdr_serialize,
  _InputFiles__cdr_deserialize,
  _InputFiles__get_serialized_size,
  _InputFiles__max_serialized_size
};

static rosidl_message_type_support_t _InputFiles__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_InputFiles,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, input_filenames_msg, msg, InputFiles)() {
  return &_InputFiles__type_support;
}

#if defined(__cplusplus)
}
#endif
