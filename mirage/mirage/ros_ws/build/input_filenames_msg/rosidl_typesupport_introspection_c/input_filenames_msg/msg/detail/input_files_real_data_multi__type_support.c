// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from input_filenames_msg:msg/InputFilesRealDataMulti.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "input_filenames_msg/msg/detail/input_files_real_data_multi__rosidl_typesupport_introspection_c.h"
#include "input_filenames_msg/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "input_filenames_msg/msg/detail/input_files_real_data_multi__functions.h"
#include "input_filenames_msg/msg/detail/input_files_real_data_multi__struct.h"


// Include directives for member types
// Member `data_pieces`
#include "input_filenames_msg/msg/input_files_real_data.h"
// Member `data_pieces`
#include "input_filenames_msg/msg/detail/input_files_real_data__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void input_filenames_msg__msg__InputFilesRealDataMulti__rosidl_typesupport_introspection_c__InputFilesRealDataMulti_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  input_filenames_msg__msg__InputFilesRealDataMulti__init(message_memory);
}

void input_filenames_msg__msg__InputFilesRealDataMulti__rosidl_typesupport_introspection_c__InputFilesRealDataMulti_fini_function(void * message_memory)
{
  input_filenames_msg__msg__InputFilesRealDataMulti__fini(message_memory);
}

size_t input_filenames_msg__msg__InputFilesRealDataMulti__rosidl_typesupport_introspection_c__size_function__InputFilesRealDataMulti__data_pieces(
  const void * untyped_member)
{
  const input_filenames_msg__msg__InputFilesRealData__Sequence * member =
    (const input_filenames_msg__msg__InputFilesRealData__Sequence *)(untyped_member);
  return member->size;
}

const void * input_filenames_msg__msg__InputFilesRealDataMulti__rosidl_typesupport_introspection_c__get_const_function__InputFilesRealDataMulti__data_pieces(
  const void * untyped_member, size_t index)
{
  const input_filenames_msg__msg__InputFilesRealData__Sequence * member =
    (const input_filenames_msg__msg__InputFilesRealData__Sequence *)(untyped_member);
  return &member->data[index];
}

void * input_filenames_msg__msg__InputFilesRealDataMulti__rosidl_typesupport_introspection_c__get_function__InputFilesRealDataMulti__data_pieces(
  void * untyped_member, size_t index)
{
  input_filenames_msg__msg__InputFilesRealData__Sequence * member =
    (input_filenames_msg__msg__InputFilesRealData__Sequence *)(untyped_member);
  return &member->data[index];
}

void input_filenames_msg__msg__InputFilesRealDataMulti__rosidl_typesupport_introspection_c__fetch_function__InputFilesRealDataMulti__data_pieces(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const input_filenames_msg__msg__InputFilesRealData * item =
    ((const input_filenames_msg__msg__InputFilesRealData *)
    input_filenames_msg__msg__InputFilesRealDataMulti__rosidl_typesupport_introspection_c__get_const_function__InputFilesRealDataMulti__data_pieces(untyped_member, index));
  input_filenames_msg__msg__InputFilesRealData * value =
    (input_filenames_msg__msg__InputFilesRealData *)(untyped_value);
  *value = *item;
}

void input_filenames_msg__msg__InputFilesRealDataMulti__rosidl_typesupport_introspection_c__assign_function__InputFilesRealDataMulti__data_pieces(
  void * untyped_member, size_t index, const void * untyped_value)
{
  input_filenames_msg__msg__InputFilesRealData * item =
    ((input_filenames_msg__msg__InputFilesRealData *)
    input_filenames_msg__msg__InputFilesRealDataMulti__rosidl_typesupport_introspection_c__get_function__InputFilesRealDataMulti__data_pieces(untyped_member, index));
  const input_filenames_msg__msg__InputFilesRealData * value =
    (const input_filenames_msg__msg__InputFilesRealData *)(untyped_value);
  *item = *value;
}

bool input_filenames_msg__msg__InputFilesRealDataMulti__rosidl_typesupport_introspection_c__resize_function__InputFilesRealDataMulti__data_pieces(
  void * untyped_member, size_t size)
{
  input_filenames_msg__msg__InputFilesRealData__Sequence * member =
    (input_filenames_msg__msg__InputFilesRealData__Sequence *)(untyped_member);
  input_filenames_msg__msg__InputFilesRealData__Sequence__fini(member);
  return input_filenames_msg__msg__InputFilesRealData__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember input_filenames_msg__msg__InputFilesRealDataMulti__rosidl_typesupport_introspection_c__InputFilesRealDataMulti_message_member_array[1] = {
  {
    "data_pieces",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg__msg__InputFilesRealDataMulti, data_pieces),  // bytes offset in struct
    NULL,  // default value
    input_filenames_msg__msg__InputFilesRealDataMulti__rosidl_typesupport_introspection_c__size_function__InputFilesRealDataMulti__data_pieces,  // size() function pointer
    input_filenames_msg__msg__InputFilesRealDataMulti__rosidl_typesupport_introspection_c__get_const_function__InputFilesRealDataMulti__data_pieces,  // get_const(index) function pointer
    input_filenames_msg__msg__InputFilesRealDataMulti__rosidl_typesupport_introspection_c__get_function__InputFilesRealDataMulti__data_pieces,  // get(index) function pointer
    input_filenames_msg__msg__InputFilesRealDataMulti__rosidl_typesupport_introspection_c__fetch_function__InputFilesRealDataMulti__data_pieces,  // fetch(index, &value) function pointer
    input_filenames_msg__msg__InputFilesRealDataMulti__rosidl_typesupport_introspection_c__assign_function__InputFilesRealDataMulti__data_pieces,  // assign(index, value) function pointer
    input_filenames_msg__msg__InputFilesRealDataMulti__rosidl_typesupport_introspection_c__resize_function__InputFilesRealDataMulti__data_pieces  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers input_filenames_msg__msg__InputFilesRealDataMulti__rosidl_typesupport_introspection_c__InputFilesRealDataMulti_message_members = {
  "input_filenames_msg__msg",  // message namespace
  "InputFilesRealDataMulti",  // message name
  1,  // number of fields
  sizeof(input_filenames_msg__msg__InputFilesRealDataMulti),
  input_filenames_msg__msg__InputFilesRealDataMulti__rosidl_typesupport_introspection_c__InputFilesRealDataMulti_message_member_array,  // message members
  input_filenames_msg__msg__InputFilesRealDataMulti__rosidl_typesupport_introspection_c__InputFilesRealDataMulti_init_function,  // function to initialize message memory (memory has to be allocated)
  input_filenames_msg__msg__InputFilesRealDataMulti__rosidl_typesupport_introspection_c__InputFilesRealDataMulti_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t input_filenames_msg__msg__InputFilesRealDataMulti__rosidl_typesupport_introspection_c__InputFilesRealDataMulti_message_type_support_handle = {
  0,
  &input_filenames_msg__msg__InputFilesRealDataMulti__rosidl_typesupport_introspection_c__InputFilesRealDataMulti_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_input_filenames_msg
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, input_filenames_msg, msg, InputFilesRealDataMulti)() {
  input_filenames_msg__msg__InputFilesRealDataMulti__rosidl_typesupport_introspection_c__InputFilesRealDataMulti_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, input_filenames_msg, msg, InputFilesRealData)();
  if (!input_filenames_msg__msg__InputFilesRealDataMulti__rosidl_typesupport_introspection_c__InputFilesRealDataMulti_message_type_support_handle.typesupport_identifier) {
    input_filenames_msg__msg__InputFilesRealDataMulti__rosidl_typesupport_introspection_c__InputFilesRealDataMulti_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &input_filenames_msg__msg__InputFilesRealDataMulti__rosidl_typesupport_introspection_c__InputFilesRealDataMulti_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
