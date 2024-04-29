// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from input_filenames_msg:msg/MultipleInpaintImages.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "input_filenames_msg/msg/detail/multiple_inpaint_images__rosidl_typesupport_introspection_c.h"
#include "input_filenames_msg/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "input_filenames_msg/msg/detail/multiple_inpaint_images__functions.h"
#include "input_filenames_msg/msg/detail/multiple_inpaint_images__struct.h"


// Include directives for member types
// Member `images`
#include "sensor_msgs/msg/image.h"
// Member `images`
#include "sensor_msgs/msg/detail/image__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void input_filenames_msg__msg__MultipleInpaintImages__rosidl_typesupport_introspection_c__MultipleInpaintImages_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  input_filenames_msg__msg__MultipleInpaintImages__init(message_memory);
}

void input_filenames_msg__msg__MultipleInpaintImages__rosidl_typesupport_introspection_c__MultipleInpaintImages_fini_function(void * message_memory)
{
  input_filenames_msg__msg__MultipleInpaintImages__fini(message_memory);
}

size_t input_filenames_msg__msg__MultipleInpaintImages__rosidl_typesupport_introspection_c__size_function__MultipleInpaintImages__images(
  const void * untyped_member)
{
  const sensor_msgs__msg__Image__Sequence * member =
    (const sensor_msgs__msg__Image__Sequence *)(untyped_member);
  return member->size;
}

const void * input_filenames_msg__msg__MultipleInpaintImages__rosidl_typesupport_introspection_c__get_const_function__MultipleInpaintImages__images(
  const void * untyped_member, size_t index)
{
  const sensor_msgs__msg__Image__Sequence * member =
    (const sensor_msgs__msg__Image__Sequence *)(untyped_member);
  return &member->data[index];
}

void * input_filenames_msg__msg__MultipleInpaintImages__rosidl_typesupport_introspection_c__get_function__MultipleInpaintImages__images(
  void * untyped_member, size_t index)
{
  sensor_msgs__msg__Image__Sequence * member =
    (sensor_msgs__msg__Image__Sequence *)(untyped_member);
  return &member->data[index];
}

void input_filenames_msg__msg__MultipleInpaintImages__rosidl_typesupport_introspection_c__fetch_function__MultipleInpaintImages__images(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const sensor_msgs__msg__Image * item =
    ((const sensor_msgs__msg__Image *)
    input_filenames_msg__msg__MultipleInpaintImages__rosidl_typesupport_introspection_c__get_const_function__MultipleInpaintImages__images(untyped_member, index));
  sensor_msgs__msg__Image * value =
    (sensor_msgs__msg__Image *)(untyped_value);
  *value = *item;
}

void input_filenames_msg__msg__MultipleInpaintImages__rosidl_typesupport_introspection_c__assign_function__MultipleInpaintImages__images(
  void * untyped_member, size_t index, const void * untyped_value)
{
  sensor_msgs__msg__Image * item =
    ((sensor_msgs__msg__Image *)
    input_filenames_msg__msg__MultipleInpaintImages__rosidl_typesupport_introspection_c__get_function__MultipleInpaintImages__images(untyped_member, index));
  const sensor_msgs__msg__Image * value =
    (const sensor_msgs__msg__Image *)(untyped_value);
  *item = *value;
}

bool input_filenames_msg__msg__MultipleInpaintImages__rosidl_typesupport_introspection_c__resize_function__MultipleInpaintImages__images(
  void * untyped_member, size_t size)
{
  sensor_msgs__msg__Image__Sequence * member =
    (sensor_msgs__msg__Image__Sequence *)(untyped_member);
  sensor_msgs__msg__Image__Sequence__fini(member);
  return sensor_msgs__msg__Image__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember input_filenames_msg__msg__MultipleInpaintImages__rosidl_typesupport_introspection_c__MultipleInpaintImages_message_member_array[1] = {
  {
    "images",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg__msg__MultipleInpaintImages, images),  // bytes offset in struct
    NULL,  // default value
    input_filenames_msg__msg__MultipleInpaintImages__rosidl_typesupport_introspection_c__size_function__MultipleInpaintImages__images,  // size() function pointer
    input_filenames_msg__msg__MultipleInpaintImages__rosidl_typesupport_introspection_c__get_const_function__MultipleInpaintImages__images,  // get_const(index) function pointer
    input_filenames_msg__msg__MultipleInpaintImages__rosidl_typesupport_introspection_c__get_function__MultipleInpaintImages__images,  // get(index) function pointer
    input_filenames_msg__msg__MultipleInpaintImages__rosidl_typesupport_introspection_c__fetch_function__MultipleInpaintImages__images,  // fetch(index, &value) function pointer
    input_filenames_msg__msg__MultipleInpaintImages__rosidl_typesupport_introspection_c__assign_function__MultipleInpaintImages__images,  // assign(index, value) function pointer
    input_filenames_msg__msg__MultipleInpaintImages__rosidl_typesupport_introspection_c__resize_function__MultipleInpaintImages__images  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers input_filenames_msg__msg__MultipleInpaintImages__rosidl_typesupport_introspection_c__MultipleInpaintImages_message_members = {
  "input_filenames_msg__msg",  // message namespace
  "MultipleInpaintImages",  // message name
  1,  // number of fields
  sizeof(input_filenames_msg__msg__MultipleInpaintImages),
  input_filenames_msg__msg__MultipleInpaintImages__rosidl_typesupport_introspection_c__MultipleInpaintImages_message_member_array,  // message members
  input_filenames_msg__msg__MultipleInpaintImages__rosidl_typesupport_introspection_c__MultipleInpaintImages_init_function,  // function to initialize message memory (memory has to be allocated)
  input_filenames_msg__msg__MultipleInpaintImages__rosidl_typesupport_introspection_c__MultipleInpaintImages_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t input_filenames_msg__msg__MultipleInpaintImages__rosidl_typesupport_introspection_c__MultipleInpaintImages_message_type_support_handle = {
  0,
  &input_filenames_msg__msg__MultipleInpaintImages__rosidl_typesupport_introspection_c__MultipleInpaintImages_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_input_filenames_msg
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, input_filenames_msg, msg, MultipleInpaintImages)() {
  input_filenames_msg__msg__MultipleInpaintImages__rosidl_typesupport_introspection_c__MultipleInpaintImages_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sensor_msgs, msg, Image)();
  if (!input_filenames_msg__msg__MultipleInpaintImages__rosidl_typesupport_introspection_c__MultipleInpaintImages_message_type_support_handle.typesupport_identifier) {
    input_filenames_msg__msg__MultipleInpaintImages__rosidl_typesupport_introspection_c__MultipleInpaintImages_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &input_filenames_msg__msg__MultipleInpaintImages__rosidl_typesupport_introspection_c__MultipleInpaintImages_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
