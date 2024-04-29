// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from input_filenames_msg:msg/InputFiles.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "input_filenames_msg/msg/detail/input_files__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace input_filenames_msg
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void InputFiles_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) input_filenames_msg::msg::InputFiles(_init);
}

void InputFiles_fini_function(void * message_memory)
{
  auto typed_message = static_cast<input_filenames_msg::msg::InputFiles *>(message_memory);
  typed_message->~InputFiles();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember InputFiles_message_member_array[3] = {
  {
    "depth_file",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg::msg::InputFiles, depth_file),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "segmentation",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg::msg::InputFiles, segmentation),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "joints",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg::msg::InputFiles, joints),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers InputFiles_message_members = {
  "input_filenames_msg::msg",  // message namespace
  "InputFiles",  // message name
  3,  // number of fields
  sizeof(input_filenames_msg::msg::InputFiles),
  InputFiles_message_member_array,  // message members
  InputFiles_init_function,  // function to initialize message memory (memory has to be allocated)
  InputFiles_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t InputFiles_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &InputFiles_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace input_filenames_msg


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<input_filenames_msg::msg::InputFiles>()
{
  return &::input_filenames_msg::msg::rosidl_typesupport_introspection_cpp::InputFiles_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, input_filenames_msg, msg, InputFiles)() {
  return &::input_filenames_msg::msg::rosidl_typesupport_introspection_cpp::InputFiles_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
