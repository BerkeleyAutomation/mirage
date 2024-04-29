// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from input_filenames_msg:msg/InputFilesSimData.idl
// generated code does not contain a copyright notice
#include "input_filenames_msg/msg/detail/input_files_sim_data__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "input_filenames_msg/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "input_filenames_msg/msg/detail/input_files_sim_data__struct.h"
#include "input_filenames_msg/msg/detail/input_files_sim_data__functions.h"
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

#include "rosidl_runtime_c/primitives_sequence.h"  // depth_map, ee_pose, interpolated_gripper, segmentation
#include "rosidl_runtime_c/primitives_sequence_functions.h"  // depth_map, ee_pose, interpolated_gripper, segmentation
#include "sensor_msgs/msg/detail/image__functions.h"  // rgb

// forward declare type support functions
ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_input_filenames_msg
size_t get_serialized_size_sensor_msgs__msg__Image(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_input_filenames_msg
size_t max_serialized_size_sensor_msgs__msg__Image(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_input_filenames_msg
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, sensor_msgs, msg, Image)();


using _InputFilesSimData__ros_msg_type = input_filenames_msg__msg__InputFilesSimData;

static bool _InputFilesSimData__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _InputFilesSimData__ros_msg_type * ros_message = static_cast<const _InputFilesSimData__ros_msg_type *>(untyped_ros_message);
  // Field name: rgb
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, sensor_msgs, msg, Image
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->rgb, cdr))
    {
      return false;
    }
  }

  // Field name: depth_map
  {
    size_t size = ros_message->depth_map.size;
    auto array_ptr = ros_message->depth_map.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: segmentation
  {
    size_t size = ros_message->segmentation.size;
    auto array_ptr = ros_message->segmentation.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: ee_pose
  {
    size_t size = ros_message->ee_pose.size;
    auto array_ptr = ros_message->ee_pose.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: interpolated_gripper
  {
    size_t size = ros_message->interpolated_gripper.size;
    auto array_ptr = ros_message->interpolated_gripper.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  return true;
}

static bool _InputFilesSimData__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _InputFilesSimData__ros_msg_type * ros_message = static_cast<_InputFilesSimData__ros_msg_type *>(untyped_ros_message);
  // Field name: rgb
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, sensor_msgs, msg, Image
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->rgb))
    {
      return false;
    }
  }

  // Field name: depth_map
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->depth_map.data) {
      rosidl_runtime_c__double__Sequence__fini(&ros_message->depth_map);
    }
    if (!rosidl_runtime_c__double__Sequence__init(&ros_message->depth_map, size)) {
      fprintf(stderr, "failed to create array for field 'depth_map'");
      return false;
    }
    auto array_ptr = ros_message->depth_map.data;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: segmentation
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->segmentation.data) {
      rosidl_runtime_c__uint8__Sequence__fini(&ros_message->segmentation);
    }
    if (!rosidl_runtime_c__uint8__Sequence__init(&ros_message->segmentation, size)) {
      fprintf(stderr, "failed to create array for field 'segmentation'");
      return false;
    }
    auto array_ptr = ros_message->segmentation.data;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: ee_pose
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->ee_pose.data) {
      rosidl_runtime_c__double__Sequence__fini(&ros_message->ee_pose);
    }
    if (!rosidl_runtime_c__double__Sequence__init(&ros_message->ee_pose, size)) {
      fprintf(stderr, "failed to create array for field 'ee_pose'");
      return false;
    }
    auto array_ptr = ros_message->ee_pose.data;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: interpolated_gripper
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->interpolated_gripper.data) {
      rosidl_runtime_c__double__Sequence__fini(&ros_message->interpolated_gripper);
    }
    if (!rosidl_runtime_c__double__Sequence__init(&ros_message->interpolated_gripper, size)) {
      fprintf(stderr, "failed to create array for field 'interpolated_gripper'");
      return false;
    }
    auto array_ptr = ros_message->interpolated_gripper.data;
    cdr.deserializeArray(array_ptr, size);
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_input_filenames_msg
size_t get_serialized_size_input_filenames_msg__msg__InputFilesSimData(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _InputFilesSimData__ros_msg_type * ros_message = static_cast<const _InputFilesSimData__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name rgb

  current_alignment += get_serialized_size_sensor_msgs__msg__Image(
    &(ros_message->rgb), current_alignment);
  // field.name depth_map
  {
    size_t array_size = ros_message->depth_map.size;
    auto array_ptr = ros_message->depth_map.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name segmentation
  {
    size_t array_size = ros_message->segmentation.size;
    auto array_ptr = ros_message->segmentation.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ee_pose
  {
    size_t array_size = ros_message->ee_pose.size;
    auto array_ptr = ros_message->ee_pose.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name interpolated_gripper
  {
    size_t array_size = ros_message->interpolated_gripper.size;
    auto array_ptr = ros_message->interpolated_gripper.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _InputFilesSimData__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_input_filenames_msg__msg__InputFilesSimData(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_input_filenames_msg
size_t max_serialized_size_input_filenames_msg__msg__InputFilesSimData(
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

  // member: rgb
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      current_alignment +=
        max_serialized_size_sensor_msgs__msg__Image(
        inner_full_bounded, inner_is_plain, current_alignment);
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }
  // member: depth_map
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: segmentation
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: ee_pose
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: interpolated_gripper
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  return current_alignment - initial_alignment;
}

static size_t _InputFilesSimData__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_input_filenames_msg__msg__InputFilesSimData(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_InputFilesSimData = {
  "input_filenames_msg::msg",
  "InputFilesSimData",
  _InputFilesSimData__cdr_serialize,
  _InputFilesSimData__cdr_deserialize,
  _InputFilesSimData__get_serialized_size,
  _InputFilesSimData__max_serialized_size
};

static rosidl_message_type_support_t _InputFilesSimData__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_InputFilesSimData,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, input_filenames_msg, msg, InputFilesSimData)() {
  return &_InputFilesSimData__type_support;
}

#if defined(__cplusplus)
}
#endif
