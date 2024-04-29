// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from input_filenames_msg:msg/InputFilesDiffusionData.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "input_filenames_msg/msg/detail/input_files_diffusion_data__struct.hpp"
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

void InputFilesDiffusionData_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) input_filenames_msg::msg::InputFilesDiffusionData(_init);
}

void InputFilesDiffusionData_fini_function(void * message_memory)
{
  auto typed_message = static_cast<input_filenames_msg::msg::InputFilesDiffusionData *>(message_memory);
  typed_message->~InputFilesDiffusionData();
}

size_t size_function__InputFilesDiffusionData__rgb(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<uint8_t> *>(untyped_member);
  return member->size();
}

const void * get_const_function__InputFilesDiffusionData__rgb(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<uint8_t> *>(untyped_member);
  return &member[index];
}

void * get_function__InputFilesDiffusionData__rgb(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<uint8_t> *>(untyped_member);
  return &member[index];
}

void fetch_function__InputFilesDiffusionData__rgb(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const uint8_t *>(
    get_const_function__InputFilesDiffusionData__rgb(untyped_member, index));
  auto & value = *reinterpret_cast<uint8_t *>(untyped_value);
  value = item;
}

void assign_function__InputFilesDiffusionData__rgb(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<uint8_t *>(
    get_function__InputFilesDiffusionData__rgb(untyped_member, index));
  const auto & value = *reinterpret_cast<const uint8_t *>(untyped_value);
  item = value;
}

void resize_function__InputFilesDiffusionData__rgb(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<uint8_t> *>(untyped_member);
  member->resize(size);
}

size_t size_function__InputFilesDiffusionData__depth_map(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<double> *>(untyped_member);
  return member->size();
}

const void * get_const_function__InputFilesDiffusionData__depth_map(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<double> *>(untyped_member);
  return &member[index];
}

void * get_function__InputFilesDiffusionData__depth_map(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<double> *>(untyped_member);
  return &member[index];
}

void fetch_function__InputFilesDiffusionData__depth_map(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const double *>(
    get_const_function__InputFilesDiffusionData__depth_map(untyped_member, index));
  auto & value = *reinterpret_cast<double *>(untyped_value);
  value = item;
}

void assign_function__InputFilesDiffusionData__depth_map(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<double *>(
    get_function__InputFilesDiffusionData__depth_map(untyped_member, index));
  const auto & value = *reinterpret_cast<const double *>(untyped_value);
  item = value;
}

void resize_function__InputFilesDiffusionData__depth_map(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<double> *>(untyped_member);
  member->resize(size);
}

size_t size_function__InputFilesDiffusionData__joints(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<double> *>(untyped_member);
  return member->size();
}

const void * get_const_function__InputFilesDiffusionData__joints(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<double> *>(untyped_member);
  return &member[index];
}

void * get_function__InputFilesDiffusionData__joints(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<double> *>(untyped_member);
  return &member[index];
}

void fetch_function__InputFilesDiffusionData__joints(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const double *>(
    get_const_function__InputFilesDiffusionData__joints(untyped_member, index));
  auto & value = *reinterpret_cast<double *>(untyped_value);
  value = item;
}

void assign_function__InputFilesDiffusionData__joints(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<double *>(
    get_function__InputFilesDiffusionData__joints(untyped_member, index));
  const auto & value = *reinterpret_cast<const double *>(untyped_value);
  item = value;
}

void resize_function__InputFilesDiffusionData__joints(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<double> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember InputFilesDiffusionData_message_member_array[6] = {
  {
    "rgb",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg::msg::InputFilesDiffusionData, rgb),  // bytes offset in struct
    nullptr,  // default value
    size_function__InputFilesDiffusionData__rgb,  // size() function pointer
    get_const_function__InputFilesDiffusionData__rgb,  // get_const(index) function pointer
    get_function__InputFilesDiffusionData__rgb,  // get(index) function pointer
    fetch_function__InputFilesDiffusionData__rgb,  // fetch(index, &value) function pointer
    assign_function__InputFilesDiffusionData__rgb,  // assign(index, value) function pointer
    resize_function__InputFilesDiffusionData__rgb  // resize(index) function pointer
  },
  {
    "depth_map",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg::msg::InputFilesDiffusionData, depth_map),  // bytes offset in struct
    nullptr,  // default value
    size_function__InputFilesDiffusionData__depth_map,  // size() function pointer
    get_const_function__InputFilesDiffusionData__depth_map,  // get_const(index) function pointer
    get_function__InputFilesDiffusionData__depth_map,  // get(index) function pointer
    fetch_function__InputFilesDiffusionData__depth_map,  // fetch(index, &value) function pointer
    assign_function__InputFilesDiffusionData__depth_map,  // assign(index, value) function pointer
    resize_function__InputFilesDiffusionData__depth_map  // resize(index) function pointer
  },
  {
    "segmentation",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<sensor_msgs::msg::Image>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg::msg::InputFilesDiffusionData, segmentation),  // bytes offset in struct
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
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg::msg::InputFilesDiffusionData, joints),  // bytes offset in struct
    nullptr,  // default value
    size_function__InputFilesDiffusionData__joints,  // size() function pointer
    get_const_function__InputFilesDiffusionData__joints,  // get_const(index) function pointer
    get_function__InputFilesDiffusionData__joints,  // get(index) function pointer
    fetch_function__InputFilesDiffusionData__joints,  // fetch(index, &value) function pointer
    assign_function__InputFilesDiffusionData__joints,  // assign(index, value) function pointer
    resize_function__InputFilesDiffusionData__joints  // resize(index) function pointer
  },
  {
    "demo_num",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<std_msgs::msg::Int16>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg::msg::InputFilesDiffusionData, demo_num),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "traj_num",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<std_msgs::msg::Int16>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg::msg::InputFilesDiffusionData, traj_num),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers InputFilesDiffusionData_message_members = {
  "input_filenames_msg::msg",  // message namespace
  "InputFilesDiffusionData",  // message name
  6,  // number of fields
  sizeof(input_filenames_msg::msg::InputFilesDiffusionData),
  InputFilesDiffusionData_message_member_array,  // message members
  InputFilesDiffusionData_init_function,  // function to initialize message memory (memory has to be allocated)
  InputFilesDiffusionData_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t InputFilesDiffusionData_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &InputFilesDiffusionData_message_members,
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
get_message_type_support_handle<input_filenames_msg::msg::InputFilesDiffusionData>()
{
  return &::input_filenames_msg::msg::rosidl_typesupport_introspection_cpp::InputFilesDiffusionData_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, input_filenames_msg, msg, InputFilesDiffusionData)() {
  return &::input_filenames_msg::msg::rosidl_typesupport_introspection_cpp::InputFilesDiffusionData_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
