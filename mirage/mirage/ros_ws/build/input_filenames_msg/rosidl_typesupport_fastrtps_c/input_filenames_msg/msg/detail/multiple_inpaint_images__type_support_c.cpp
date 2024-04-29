// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from input_filenames_msg:msg/MultipleInpaintImages.idl
// generated code does not contain a copyright notice
#include "input_filenames_msg/msg/detail/multiple_inpaint_images__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "input_filenames_msg/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "input_filenames_msg/msg/detail/multiple_inpaint_images__struct.h"
#include "input_filenames_msg/msg/detail/multiple_inpaint_images__functions.h"
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

#include "sensor_msgs/msg/detail/image__functions.h"  // images

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


using _MultipleInpaintImages__ros_msg_type = input_filenames_msg__msg__MultipleInpaintImages;

static bool _MultipleInpaintImages__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _MultipleInpaintImages__ros_msg_type * ros_message = static_cast<const _MultipleInpaintImages__ros_msg_type *>(untyped_ros_message);
  // Field name: images
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, sensor_msgs, msg, Image
      )()->data);
    size_t size = ros_message->images.size;
    auto array_ptr = ros_message->images.data;
    cdr << static_cast<uint32_t>(size);
    for (size_t i = 0; i < size; ++i) {
      if (!callbacks->cdr_serialize(
          &array_ptr[i], cdr))
      {
        return false;
      }
    }
  }

  return true;
}

static bool _MultipleInpaintImages__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _MultipleInpaintImages__ros_msg_type * ros_message = static_cast<_MultipleInpaintImages__ros_msg_type *>(untyped_ros_message);
  // Field name: images
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, sensor_msgs, msg, Image
      )()->data);
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->images.data) {
      sensor_msgs__msg__Image__Sequence__fini(&ros_message->images);
    }
    if (!sensor_msgs__msg__Image__Sequence__init(&ros_message->images, size)) {
      fprintf(stderr, "failed to create array for field 'images'");
      return false;
    }
    auto array_ptr = ros_message->images.data;
    for (size_t i = 0; i < size; ++i) {
      if (!callbacks->cdr_deserialize(
          cdr, &array_ptr[i]))
      {
        return false;
      }
    }
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_input_filenames_msg
size_t get_serialized_size_input_filenames_msg__msg__MultipleInpaintImages(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _MultipleInpaintImages__ros_msg_type * ros_message = static_cast<const _MultipleInpaintImages__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name images
  {
    size_t array_size = ros_message->images.size;
    auto array_ptr = ros_message->images.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += get_serialized_size_sensor_msgs__msg__Image(
        &array_ptr[index], current_alignment);
    }
  }

  return current_alignment - initial_alignment;
}

static uint32_t _MultipleInpaintImages__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_input_filenames_msg__msg__MultipleInpaintImages(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_input_filenames_msg
size_t max_serialized_size_input_filenames_msg__msg__MultipleInpaintImages(
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

  // member: images
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);


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

  return current_alignment - initial_alignment;
}

static size_t _MultipleInpaintImages__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_input_filenames_msg__msg__MultipleInpaintImages(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_MultipleInpaintImages = {
  "input_filenames_msg::msg",
  "MultipleInpaintImages",
  _MultipleInpaintImages__cdr_serialize,
  _MultipleInpaintImages__cdr_deserialize,
  _MultipleInpaintImages__get_serialized_size,
  _MultipleInpaintImages__max_serialized_size
};

static rosidl_message_type_support_t _MultipleInpaintImages__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_MultipleInpaintImages,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, input_filenames_msg, msg, MultipleInpaintImages)() {
  return &_MultipleInpaintImages__type_support;
}

#if defined(__cplusplus)
}
#endif
