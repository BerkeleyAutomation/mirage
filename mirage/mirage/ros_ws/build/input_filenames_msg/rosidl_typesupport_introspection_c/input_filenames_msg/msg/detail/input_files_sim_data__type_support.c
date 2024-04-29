// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from input_filenames_msg:msg/InputFilesSimData.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "input_filenames_msg/msg/detail/input_files_sim_data__rosidl_typesupport_introspection_c.h"
#include "input_filenames_msg/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "input_filenames_msg/msg/detail/input_files_sim_data__functions.h"
#include "input_filenames_msg/msg/detail/input_files_sim_data__struct.h"


// Include directives for member types
// Member `rgb`
#include "sensor_msgs/msg/image.h"
// Member `rgb`
#include "sensor_msgs/msg/detail/image__rosidl_typesupport_introspection_c.h"
// Member `depth_map`
// Member `segmentation`
// Member `ee_pose`
// Member `interpolated_gripper`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__InputFilesSimData_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  input_filenames_msg__msg__InputFilesSimData__init(message_memory);
}

void input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__InputFilesSimData_fini_function(void * message_memory)
{
  input_filenames_msg__msg__InputFilesSimData__fini(message_memory);
}

size_t input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__size_function__InputFilesSimData__depth_map(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__get_const_function__InputFilesSimData__depth_map(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__get_function__InputFilesSimData__depth_map(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__fetch_function__InputFilesSimData__depth_map(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__get_const_function__InputFilesSimData__depth_map(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__assign_function__InputFilesSimData__depth_map(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__get_function__InputFilesSimData__depth_map(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__resize_function__InputFilesSimData__depth_map(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

size_t input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__size_function__InputFilesSimData__segmentation(
  const void * untyped_member)
{
  const rosidl_runtime_c__uint8__Sequence * member =
    (const rosidl_runtime_c__uint8__Sequence *)(untyped_member);
  return member->size;
}

const void * input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__get_const_function__InputFilesSimData__segmentation(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__uint8__Sequence * member =
    (const rosidl_runtime_c__uint8__Sequence *)(untyped_member);
  return &member->data[index];
}

void * input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__get_function__InputFilesSimData__segmentation(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__uint8__Sequence * member =
    (rosidl_runtime_c__uint8__Sequence *)(untyped_member);
  return &member->data[index];
}

void input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__fetch_function__InputFilesSimData__segmentation(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const uint8_t * item =
    ((const uint8_t *)
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__get_const_function__InputFilesSimData__segmentation(untyped_member, index));
  uint8_t * value =
    (uint8_t *)(untyped_value);
  *value = *item;
}

void input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__assign_function__InputFilesSimData__segmentation(
  void * untyped_member, size_t index, const void * untyped_value)
{
  uint8_t * item =
    ((uint8_t *)
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__get_function__InputFilesSimData__segmentation(untyped_member, index));
  const uint8_t * value =
    (const uint8_t *)(untyped_value);
  *item = *value;
}

bool input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__resize_function__InputFilesSimData__segmentation(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__uint8__Sequence * member =
    (rosidl_runtime_c__uint8__Sequence *)(untyped_member);
  rosidl_runtime_c__uint8__Sequence__fini(member);
  return rosidl_runtime_c__uint8__Sequence__init(member, size);
}

size_t input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__size_function__InputFilesSimData__ee_pose(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__get_const_function__InputFilesSimData__ee_pose(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__get_function__InputFilesSimData__ee_pose(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__fetch_function__InputFilesSimData__ee_pose(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__get_const_function__InputFilesSimData__ee_pose(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__assign_function__InputFilesSimData__ee_pose(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__get_function__InputFilesSimData__ee_pose(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__resize_function__InputFilesSimData__ee_pose(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

size_t input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__size_function__InputFilesSimData__interpolated_gripper(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__get_const_function__InputFilesSimData__interpolated_gripper(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__get_function__InputFilesSimData__interpolated_gripper(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__fetch_function__InputFilesSimData__interpolated_gripper(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__get_const_function__InputFilesSimData__interpolated_gripper(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__assign_function__InputFilesSimData__interpolated_gripper(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__get_function__InputFilesSimData__interpolated_gripper(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__resize_function__InputFilesSimData__interpolated_gripper(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__InputFilesSimData_message_member_array[5] = {
  {
    "rgb",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg__msg__InputFilesSimData, rgb),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "depth_map",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg__msg__InputFilesSimData, depth_map),  // bytes offset in struct
    NULL,  // default value
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__size_function__InputFilesSimData__depth_map,  // size() function pointer
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__get_const_function__InputFilesSimData__depth_map,  // get_const(index) function pointer
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__get_function__InputFilesSimData__depth_map,  // get(index) function pointer
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__fetch_function__InputFilesSimData__depth_map,  // fetch(index, &value) function pointer
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__assign_function__InputFilesSimData__depth_map,  // assign(index, value) function pointer
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__resize_function__InputFilesSimData__depth_map  // resize(index) function pointer
  },
  {
    "segmentation",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg__msg__InputFilesSimData, segmentation),  // bytes offset in struct
    NULL,  // default value
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__size_function__InputFilesSimData__segmentation,  // size() function pointer
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__get_const_function__InputFilesSimData__segmentation,  // get_const(index) function pointer
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__get_function__InputFilesSimData__segmentation,  // get(index) function pointer
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__fetch_function__InputFilesSimData__segmentation,  // fetch(index, &value) function pointer
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__assign_function__InputFilesSimData__segmentation,  // assign(index, value) function pointer
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__resize_function__InputFilesSimData__segmentation  // resize(index) function pointer
  },
  {
    "ee_pose",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg__msg__InputFilesSimData, ee_pose),  // bytes offset in struct
    NULL,  // default value
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__size_function__InputFilesSimData__ee_pose,  // size() function pointer
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__get_const_function__InputFilesSimData__ee_pose,  // get_const(index) function pointer
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__get_function__InputFilesSimData__ee_pose,  // get(index) function pointer
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__fetch_function__InputFilesSimData__ee_pose,  // fetch(index, &value) function pointer
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__assign_function__InputFilesSimData__ee_pose,  // assign(index, value) function pointer
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__resize_function__InputFilesSimData__ee_pose  // resize(index) function pointer
  },
  {
    "interpolated_gripper",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg__msg__InputFilesSimData, interpolated_gripper),  // bytes offset in struct
    NULL,  // default value
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__size_function__InputFilesSimData__interpolated_gripper,  // size() function pointer
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__get_const_function__InputFilesSimData__interpolated_gripper,  // get_const(index) function pointer
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__get_function__InputFilesSimData__interpolated_gripper,  // get(index) function pointer
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__fetch_function__InputFilesSimData__interpolated_gripper,  // fetch(index, &value) function pointer
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__assign_function__InputFilesSimData__interpolated_gripper,  // assign(index, value) function pointer
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__resize_function__InputFilesSimData__interpolated_gripper  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__InputFilesSimData_message_members = {
  "input_filenames_msg__msg",  // message namespace
  "InputFilesSimData",  // message name
  5,  // number of fields
  sizeof(input_filenames_msg__msg__InputFilesSimData),
  input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__InputFilesSimData_message_member_array,  // message members
  input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__InputFilesSimData_init_function,  // function to initialize message memory (memory has to be allocated)
  input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__InputFilesSimData_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__InputFilesSimData_message_type_support_handle = {
  0,
  &input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__InputFilesSimData_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_input_filenames_msg
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, input_filenames_msg, msg, InputFilesSimData)() {
  input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__InputFilesSimData_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sensor_msgs, msg, Image)();
  if (!input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__InputFilesSimData_message_type_support_handle.typesupport_identifier) {
    input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__InputFilesSimData_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &input_filenames_msg__msg__InputFilesSimData__rosidl_typesupport_introspection_c__InputFilesSimData_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
