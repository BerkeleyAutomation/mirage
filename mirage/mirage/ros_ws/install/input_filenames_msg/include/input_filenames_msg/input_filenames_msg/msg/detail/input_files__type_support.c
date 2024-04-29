// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from input_filenames_msg:msg/InputFiles.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "input_filenames_msg/msg/detail/input_files__rosidl_typesupport_introspection_c.h"
#include "input_filenames_msg/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "input_filenames_msg/msg/detail/input_files__functions.h"
#include "input_filenames_msg/msg/detail/input_files__struct.h"


// Include directives for member types
// Member `depth_file`
// Member `segmentation`
// Member `joints`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void input_filenames_msg__msg__InputFiles__rosidl_typesupport_introspection_c__InputFiles_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  input_filenames_msg__msg__InputFiles__init(message_memory);
}

void input_filenames_msg__msg__InputFiles__rosidl_typesupport_introspection_c__InputFiles_fini_function(void * message_memory)
{
  input_filenames_msg__msg__InputFiles__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember input_filenames_msg__msg__InputFiles__rosidl_typesupport_introspection_c__InputFiles_message_member_array[3] = {
  {
    "depth_file",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg__msg__InputFiles, depth_file),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "segmentation",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg__msg__InputFiles, segmentation),  // bytes offset in struct
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
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg__msg__InputFiles, joints),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers input_filenames_msg__msg__InputFiles__rosidl_typesupport_introspection_c__InputFiles_message_members = {
  "input_filenames_msg__msg",  // message namespace
  "InputFiles",  // message name
  3,  // number of fields
  sizeof(input_filenames_msg__msg__InputFiles),
  input_filenames_msg__msg__InputFiles__rosidl_typesupport_introspection_c__InputFiles_message_member_array,  // message members
  input_filenames_msg__msg__InputFiles__rosidl_typesupport_introspection_c__InputFiles_init_function,  // function to initialize message memory (memory has to be allocated)
  input_filenames_msg__msg__InputFiles__rosidl_typesupport_introspection_c__InputFiles_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t input_filenames_msg__msg__InputFiles__rosidl_typesupport_introspection_c__InputFiles_message_type_support_handle = {
  0,
  &input_filenames_msg__msg__InputFiles__rosidl_typesupport_introspection_c__InputFiles_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_input_filenames_msg
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, input_filenames_msg, msg, InputFiles)() {
  if (!input_filenames_msg__msg__InputFiles__rosidl_typesupport_introspection_c__InputFiles_message_type_support_handle.typesupport_identifier) {
    input_filenames_msg__msg__InputFiles__rosidl_typesupport_introspection_c__InputFiles_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &input_filenames_msg__msg__InputFiles__rosidl_typesupport_introspection_c__InputFiles_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
