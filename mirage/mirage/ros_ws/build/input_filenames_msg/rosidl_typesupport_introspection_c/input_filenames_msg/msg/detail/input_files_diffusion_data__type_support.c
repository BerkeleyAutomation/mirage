// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from input_filenames_msg:msg/InputFilesDiffusionData.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "input_filenames_msg/msg/detail/input_files_diffusion_data__rosidl_typesupport_introspection_c.h"
#include "input_filenames_msg/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "input_filenames_msg/msg/detail/input_files_diffusion_data__functions.h"
#include "input_filenames_msg/msg/detail/input_files_diffusion_data__struct.h"


// Include directives for member types
// Member `rgb`
// Member `depth_map`
// Member `joints`
#include "rosidl_runtime_c/primitives_sequence_functions.h"
// Member `segmentation`
#include "sensor_msgs/msg/image.h"
// Member `segmentation`
#include "sensor_msgs/msg/detail/image__rosidl_typesupport_introspection_c.h"
// Member `demo_num`
// Member `traj_num`
#include "std_msgs/msg/int16.h"
// Member `demo_num`
// Member `traj_num`
#include "std_msgs/msg/detail/int16__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__InputFilesDiffusionData_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  input_filenames_msg__msg__InputFilesDiffusionData__init(message_memory);
}

void input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__InputFilesDiffusionData_fini_function(void * message_memory)
{
  input_filenames_msg__msg__InputFilesDiffusionData__fini(message_memory);
}

size_t input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__size_function__InputFilesDiffusionData__rgb(
  const void * untyped_member)
{
  const rosidl_runtime_c__uint8__Sequence * member =
    (const rosidl_runtime_c__uint8__Sequence *)(untyped_member);
  return member->size;
}

const void * input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__get_const_function__InputFilesDiffusionData__rgb(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__uint8__Sequence * member =
    (const rosidl_runtime_c__uint8__Sequence *)(untyped_member);
  return &member->data[index];
}

void * input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__get_function__InputFilesDiffusionData__rgb(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__uint8__Sequence * member =
    (rosidl_runtime_c__uint8__Sequence *)(untyped_member);
  return &member->data[index];
}

void input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__fetch_function__InputFilesDiffusionData__rgb(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const uint8_t * item =
    ((const uint8_t *)
    input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__get_const_function__InputFilesDiffusionData__rgb(untyped_member, index));
  uint8_t * value =
    (uint8_t *)(untyped_value);
  *value = *item;
}

void input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__assign_function__InputFilesDiffusionData__rgb(
  void * untyped_member, size_t index, const void * untyped_value)
{
  uint8_t * item =
    ((uint8_t *)
    input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__get_function__InputFilesDiffusionData__rgb(untyped_member, index));
  const uint8_t * value =
    (const uint8_t *)(untyped_value);
  *item = *value;
}

bool input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__resize_function__InputFilesDiffusionData__rgb(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__uint8__Sequence * member =
    (rosidl_runtime_c__uint8__Sequence *)(untyped_member);
  rosidl_runtime_c__uint8__Sequence__fini(member);
  return rosidl_runtime_c__uint8__Sequence__init(member, size);
}

size_t input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__size_function__InputFilesDiffusionData__depth_map(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__get_const_function__InputFilesDiffusionData__depth_map(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__get_function__InputFilesDiffusionData__depth_map(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__fetch_function__InputFilesDiffusionData__depth_map(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__get_const_function__InputFilesDiffusionData__depth_map(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__assign_function__InputFilesDiffusionData__depth_map(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__get_function__InputFilesDiffusionData__depth_map(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__resize_function__InputFilesDiffusionData__depth_map(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

size_t input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__size_function__InputFilesDiffusionData__joints(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__get_const_function__InputFilesDiffusionData__joints(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__get_function__InputFilesDiffusionData__joints(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__fetch_function__InputFilesDiffusionData__joints(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__get_const_function__InputFilesDiffusionData__joints(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__assign_function__InputFilesDiffusionData__joints(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__get_function__InputFilesDiffusionData__joints(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__resize_function__InputFilesDiffusionData__joints(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__InputFilesDiffusionData_message_member_array[6] = {
  {
    "rgb",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg__msg__InputFilesDiffusionData, rgb),  // bytes offset in struct
    NULL,  // default value
    input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__size_function__InputFilesDiffusionData__rgb,  // size() function pointer
    input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__get_const_function__InputFilesDiffusionData__rgb,  // get_const(index) function pointer
    input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__get_function__InputFilesDiffusionData__rgb,  // get(index) function pointer
    input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__fetch_function__InputFilesDiffusionData__rgb,  // fetch(index, &value) function pointer
    input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__assign_function__InputFilesDiffusionData__rgb,  // assign(index, value) function pointer
    input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__resize_function__InputFilesDiffusionData__rgb  // resize(index) function pointer
  },
  {
    "depth_map",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg__msg__InputFilesDiffusionData, depth_map),  // bytes offset in struct
    NULL,  // default value
    input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__size_function__InputFilesDiffusionData__depth_map,  // size() function pointer
    input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__get_const_function__InputFilesDiffusionData__depth_map,  // get_const(index) function pointer
    input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__get_function__InputFilesDiffusionData__depth_map,  // get(index) function pointer
    input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__fetch_function__InputFilesDiffusionData__depth_map,  // fetch(index, &value) function pointer
    input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__assign_function__InputFilesDiffusionData__depth_map,  // assign(index, value) function pointer
    input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__resize_function__InputFilesDiffusionData__depth_map  // resize(index) function pointer
  },
  {
    "segmentation",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg__msg__InputFilesDiffusionData, segmentation),  // bytes offset in struct
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
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg__msg__InputFilesDiffusionData, joints),  // bytes offset in struct
    NULL,  // default value
    input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__size_function__InputFilesDiffusionData__joints,  // size() function pointer
    input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__get_const_function__InputFilesDiffusionData__joints,  // get_const(index) function pointer
    input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__get_function__InputFilesDiffusionData__joints,  // get(index) function pointer
    input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__fetch_function__InputFilesDiffusionData__joints,  // fetch(index, &value) function pointer
    input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__assign_function__InputFilesDiffusionData__joints,  // assign(index, value) function pointer
    input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__resize_function__InputFilesDiffusionData__joints  // resize(index) function pointer
  },
  {
    "demo_num",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg__msg__InputFilesDiffusionData, demo_num),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "traj_num",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg__msg__InputFilesDiffusionData, traj_num),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__InputFilesDiffusionData_message_members = {
  "input_filenames_msg__msg",  // message namespace
  "InputFilesDiffusionData",  // message name
  6,  // number of fields
  sizeof(input_filenames_msg__msg__InputFilesDiffusionData),
  input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__InputFilesDiffusionData_message_member_array,  // message members
  input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__InputFilesDiffusionData_init_function,  // function to initialize message memory (memory has to be allocated)
  input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__InputFilesDiffusionData_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__InputFilesDiffusionData_message_type_support_handle = {
  0,
  &input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__InputFilesDiffusionData_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_input_filenames_msg
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, input_filenames_msg, msg, InputFilesDiffusionData)() {
  input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__InputFilesDiffusionData_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sensor_msgs, msg, Image)();
  input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__InputFilesDiffusionData_message_member_array[4].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Int16)();
  input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__InputFilesDiffusionData_message_member_array[5].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Int16)();
  if (!input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__InputFilesDiffusionData_message_type_support_handle.typesupport_identifier) {
    input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__InputFilesDiffusionData_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &input_filenames_msg__msg__InputFilesDiffusionData__rosidl_typesupport_introspection_c__InputFilesDiffusionData_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
