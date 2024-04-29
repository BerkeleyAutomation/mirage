// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from input_filenames_msg:msg/InputFilesRealDataMulti.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "input_filenames_msg/msg/detail/input_files_real_data_multi__struct.hpp"
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

void InputFilesRealDataMulti_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) input_filenames_msg::msg::InputFilesRealDataMulti(_init);
}

void InputFilesRealDataMulti_fini_function(void * message_memory)
{
  auto typed_message = static_cast<input_filenames_msg::msg::InputFilesRealDataMulti *>(message_memory);
  typed_message->~InputFilesRealDataMulti();
}

size_t size_function__InputFilesRealDataMulti__data_pieces(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<input_filenames_msg::msg::InputFilesRealData> *>(untyped_member);
  return member->size();
}

const void * get_const_function__InputFilesRealDataMulti__data_pieces(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<input_filenames_msg::msg::InputFilesRealData> *>(untyped_member);
  return &member[index];
}

void * get_function__InputFilesRealDataMulti__data_pieces(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<input_filenames_msg::msg::InputFilesRealData> *>(untyped_member);
  return &member[index];
}

void fetch_function__InputFilesRealDataMulti__data_pieces(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const input_filenames_msg::msg::InputFilesRealData *>(
    get_const_function__InputFilesRealDataMulti__data_pieces(untyped_member, index));
  auto & value = *reinterpret_cast<input_filenames_msg::msg::InputFilesRealData *>(untyped_value);
  value = item;
}

void assign_function__InputFilesRealDataMulti__data_pieces(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<input_filenames_msg::msg::InputFilesRealData *>(
    get_function__InputFilesRealDataMulti__data_pieces(untyped_member, index));
  const auto & value = *reinterpret_cast<const input_filenames_msg::msg::InputFilesRealData *>(untyped_value);
  item = value;
}

void resize_function__InputFilesRealDataMulti__data_pieces(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<input_filenames_msg::msg::InputFilesRealData> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember InputFilesRealDataMulti_message_member_array[1] = {
  {
    "data_pieces",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<input_filenames_msg::msg::InputFilesRealData>(),  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg::msg::InputFilesRealDataMulti, data_pieces),  // bytes offset in struct
    nullptr,  // default value
    size_function__InputFilesRealDataMulti__data_pieces,  // size() function pointer
    get_const_function__InputFilesRealDataMulti__data_pieces,  // get_const(index) function pointer
    get_function__InputFilesRealDataMulti__data_pieces,  // get(index) function pointer
    fetch_function__InputFilesRealDataMulti__data_pieces,  // fetch(index, &value) function pointer
    assign_function__InputFilesRealDataMulti__data_pieces,  // assign(index, value) function pointer
    resize_function__InputFilesRealDataMulti__data_pieces  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers InputFilesRealDataMulti_message_members = {
  "input_filenames_msg::msg",  // message namespace
  "InputFilesRealDataMulti",  // message name
  1,  // number of fields
  sizeof(input_filenames_msg::msg::InputFilesRealDataMulti),
  InputFilesRealDataMulti_message_member_array,  // message members
  InputFilesRealDataMulti_init_function,  // function to initialize message memory (memory has to be allocated)
  InputFilesRealDataMulti_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t InputFilesRealDataMulti_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &InputFilesRealDataMulti_message_members,
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
get_message_type_support_handle<input_filenames_msg::msg::InputFilesRealDataMulti>()
{
  return &::input_filenames_msg::msg::rosidl_typesupport_introspection_cpp::InputFilesRealDataMulti_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, input_filenames_msg, msg, InputFilesRealDataMulti)() {
  return &::input_filenames_msg::msg::rosidl_typesupport_introspection_cpp::InputFilesRealDataMulti_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
