// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from input_filenames_msg:msg/InputFilesData.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "input_filenames_msg/msg/detail/input_files_data__rosidl_typesupport_introspection_c.h"
#include "input_filenames_msg/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "input_filenames_msg/msg/detail/input_files_data__functions.h"
#include "input_filenames_msg/msg/detail/input_files_data__struct.h"


// Include directives for member types
// Member `depth_data`
// Member `joints`
#include "rosidl_runtime_c/primitives_sequence_functions.h"
// Member `segmentation_data`
#include "sensor_msgs/msg/image.h"
// Member `segmentation_data`
#include "sensor_msgs/msg/detail/image__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__InputFilesData_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  input_filenames_msg__msg__InputFilesData__init(message_memory);
}

void input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__InputFilesData_fini_function(void * message_memory)
{
  input_filenames_msg__msg__InputFilesData__fini(message_memory);
}

size_t input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__size_function__InputFilesData__depth_data(
  const void * untyped_member)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return member->size;
}

const void * input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__get_const_function__InputFilesData__depth_data(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void * input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__get_function__InputFilesData__depth_data(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__fetch_function__InputFilesData__depth_data(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const float * item =
    ((const float *)
    input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__get_const_function__InputFilesData__depth_data(untyped_member, index));
  float * value =
    (float *)(untyped_value);
  *value = *item;
}

void input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__assign_function__InputFilesData__depth_data(
  void * untyped_member, size_t index, const void * untyped_value)
{
  float * item =
    ((float *)
    input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__get_function__InputFilesData__depth_data(untyped_member, index));
  const float * value =
    (const float *)(untyped_value);
  *item = *value;
}

bool input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__resize_function__InputFilesData__depth_data(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  rosidl_runtime_c__float__Sequence__fini(member);
  return rosidl_runtime_c__float__Sequence__init(member, size);
}

size_t input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__size_function__InputFilesData__joints(
  const void * untyped_member)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return member->size;
}

const void * input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__get_const_function__InputFilesData__joints(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void * input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__get_function__InputFilesData__joints(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__fetch_function__InputFilesData__joints(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const float * item =
    ((const float *)
    input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__get_const_function__InputFilesData__joints(untyped_member, index));
  float * value =
    (float *)(untyped_value);
  *value = *item;
}

void input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__assign_function__InputFilesData__joints(
  void * untyped_member, size_t index, const void * untyped_value)
{
  float * item =
    ((float *)
    input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__get_function__InputFilesData__joints(untyped_member, index));
  const float * value =
    (const float *)(untyped_value);
  *item = *value;
}

bool input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__resize_function__InputFilesData__joints(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  rosidl_runtime_c__float__Sequence__fini(member);
  return rosidl_runtime_c__float__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__InputFilesData_message_member_array[3] = {
  {
    "depth_data",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg__msg__InputFilesData, depth_data),  // bytes offset in struct
    NULL,  // default value
    input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__size_function__InputFilesData__depth_data,  // size() function pointer
    input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__get_const_function__InputFilesData__depth_data,  // get_const(index) function pointer
    input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__get_function__InputFilesData__depth_data,  // get(index) function pointer
    input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__fetch_function__InputFilesData__depth_data,  // fetch(index, &value) function pointer
    input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__assign_function__InputFilesData__depth_data,  // assign(index, value) function pointer
    input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__resize_function__InputFilesData__depth_data  // resize(index) function pointer
  },
  {
    "segmentation_data",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg__msg__InputFilesData, segmentation_data),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "joints",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg__msg__InputFilesData, joints),  // bytes offset in struct
    NULL,  // default value
    input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__size_function__InputFilesData__joints,  // size() function pointer
    input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__get_const_function__InputFilesData__joints,  // get_const(index) function pointer
    input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__get_function__InputFilesData__joints,  // get(index) function pointer
    input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__fetch_function__InputFilesData__joints,  // fetch(index, &value) function pointer
    input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__assign_function__InputFilesData__joints,  // assign(index, value) function pointer
    input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__resize_function__InputFilesData__joints  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__InputFilesData_message_members = {
  "input_filenames_msg__msg",  // message namespace
  "InputFilesData",  // message name
  3,  // number of fields
  sizeof(input_filenames_msg__msg__InputFilesData),
  input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__InputFilesData_message_member_array,  // message members
  input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__InputFilesData_init_function,  // function to initialize message memory (memory has to be allocated)
  input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__InputFilesData_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__InputFilesData_message_type_support_handle = {
  0,
  &input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__InputFilesData_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_input_filenames_msg
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, input_filenames_msg, msg, InputFilesData)() {
  input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__InputFilesData_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sensor_msgs, msg, Image)();
  if (!input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__InputFilesData_message_type_support_handle.typesupport_identifier) {
    input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__InputFilesData_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &input_filenames_msg__msg__InputFilesData__rosidl_typesupport_introspection_c__InputFilesData_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
