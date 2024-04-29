// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from input_filenames_msg:msg/InputFilesSimData.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "input_filenames_msg/msg/detail/input_files_sim_data__struct.hpp"
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

void InputFilesSimData_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) input_filenames_msg::msg::InputFilesSimData(_init);
}

void InputFilesSimData_fini_function(void * message_memory)
{
  auto typed_message = static_cast<input_filenames_msg::msg::InputFilesSimData *>(message_memory);
  typed_message->~InputFilesSimData();
}

size_t size_function__InputFilesSimData__depth_map(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<double> *>(untyped_member);
  return member->size();
}

const void * get_const_function__InputFilesSimData__depth_map(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<double> *>(untyped_member);
  return &member[index];
}

void * get_function__InputFilesSimData__depth_map(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<double> *>(untyped_member);
  return &member[index];
}

void fetch_function__InputFilesSimData__depth_map(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const double *>(
    get_const_function__InputFilesSimData__depth_map(untyped_member, index));
  auto & value = *reinterpret_cast<double *>(untyped_value);
  value = item;
}

void assign_function__InputFilesSimData__depth_map(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<double *>(
    get_function__InputFilesSimData__depth_map(untyped_member, index));
  const auto & value = *reinterpret_cast<const double *>(untyped_value);
  item = value;
}

void resize_function__InputFilesSimData__depth_map(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<double> *>(untyped_member);
  member->resize(size);
}

size_t size_function__InputFilesSimData__segmentation(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<uint8_t> *>(untyped_member);
  return member->size();
}

const void * get_const_function__InputFilesSimData__segmentation(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<uint8_t> *>(untyped_member);
  return &member[index];
}

void * get_function__InputFilesSimData__segmentation(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<uint8_t> *>(untyped_member);
  return &member[index];
}

void fetch_function__InputFilesSimData__segmentation(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const uint8_t *>(
    get_const_function__InputFilesSimData__segmentation(untyped_member, index));
  auto & value = *reinterpret_cast<uint8_t *>(untyped_value);
  value = item;
}

void assign_function__InputFilesSimData__segmentation(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<uint8_t *>(
    get_function__InputFilesSimData__segmentation(untyped_member, index));
  const auto & value = *reinterpret_cast<const uint8_t *>(untyped_value);
  item = value;
}

void resize_function__InputFilesSimData__segmentation(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<uint8_t> *>(untyped_member);
  member->resize(size);
}

size_t size_function__InputFilesSimData__ee_pose(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<double> *>(untyped_member);
  return member->size();
}

const void * get_const_function__InputFilesSimData__ee_pose(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<double> *>(untyped_member);
  return &member[index];
}

void * get_function__InputFilesSimData__ee_pose(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<double> *>(untyped_member);
  return &member[index];
}

void fetch_function__InputFilesSimData__ee_pose(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const double *>(
    get_const_function__InputFilesSimData__ee_pose(untyped_member, index));
  auto & value = *reinterpret_cast<double *>(untyped_value);
  value = item;
}

void assign_function__InputFilesSimData__ee_pose(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<double *>(
    get_function__InputFilesSimData__ee_pose(untyped_member, index));
  const auto & value = *reinterpret_cast<const double *>(untyped_value);
  item = value;
}

void resize_function__InputFilesSimData__ee_pose(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<double> *>(untyped_member);
  member->resize(size);
}

size_t size_function__InputFilesSimData__interpolated_gripper(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<double> *>(untyped_member);
  return member->size();
}

const void * get_const_function__InputFilesSimData__interpolated_gripper(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<double> *>(untyped_member);
  return &member[index];
}

void * get_function__InputFilesSimData__interpolated_gripper(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<double> *>(untyped_member);
  return &member[index];
}

void fetch_function__InputFilesSimData__interpolated_gripper(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const double *>(
    get_const_function__InputFilesSimData__interpolated_gripper(untyped_member, index));
  auto & value = *reinterpret_cast<double *>(untyped_value);
  value = item;
}

void assign_function__InputFilesSimData__interpolated_gripper(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<double *>(
    get_function__InputFilesSimData__interpolated_gripper(untyped_member, index));
  const auto & value = *reinterpret_cast<const double *>(untyped_value);
  item = value;
}

void resize_function__InputFilesSimData__interpolated_gripper(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<double> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember InputFilesSimData_message_member_array[5] = {
  {
    "rgb",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<sensor_msgs::msg::Image>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg::msg::InputFilesSimData, rgb),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "depth_map",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg::msg::InputFilesSimData, depth_map),  // bytes offset in struct
    nullptr,  // default value
    size_function__InputFilesSimData__depth_map,  // size() function pointer
    get_const_function__InputFilesSimData__depth_map,  // get_const(index) function pointer
    get_function__InputFilesSimData__depth_map,  // get(index) function pointer
    fetch_function__InputFilesSimData__depth_map,  // fetch(index, &value) function pointer
    assign_function__InputFilesSimData__depth_map,  // assign(index, value) function pointer
    resize_function__InputFilesSimData__depth_map  // resize(index) function pointer
  },
  {
    "segmentation",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg::msg::InputFilesSimData, segmentation),  // bytes offset in struct
    nullptr,  // default value
    size_function__InputFilesSimData__segmentation,  // size() function pointer
    get_const_function__InputFilesSimData__segmentation,  // get_const(index) function pointer
    get_function__InputFilesSimData__segmentation,  // get(index) function pointer
    fetch_function__InputFilesSimData__segmentation,  // fetch(index, &value) function pointer
    assign_function__InputFilesSimData__segmentation,  // assign(index, value) function pointer
    resize_function__InputFilesSimData__segmentation  // resize(index) function pointer
  },
  {
    "ee_pose",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg::msg::InputFilesSimData, ee_pose),  // bytes offset in struct
    nullptr,  // default value
    size_function__InputFilesSimData__ee_pose,  // size() function pointer
    get_const_function__InputFilesSimData__ee_pose,  // get_const(index) function pointer
    get_function__InputFilesSimData__ee_pose,  // get(index) function pointer
    fetch_function__InputFilesSimData__ee_pose,  // fetch(index, &value) function pointer
    assign_function__InputFilesSimData__ee_pose,  // assign(index, value) function pointer
    resize_function__InputFilesSimData__ee_pose  // resize(index) function pointer
  },
  {
    "interpolated_gripper",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg::msg::InputFilesSimData, interpolated_gripper),  // bytes offset in struct
    nullptr,  // default value
    size_function__InputFilesSimData__interpolated_gripper,  // size() function pointer
    get_const_function__InputFilesSimData__interpolated_gripper,  // get_const(index) function pointer
    get_function__InputFilesSimData__interpolated_gripper,  // get(index) function pointer
    fetch_function__InputFilesSimData__interpolated_gripper,  // fetch(index, &value) function pointer
    assign_function__InputFilesSimData__interpolated_gripper,  // assign(index, value) function pointer
    resize_function__InputFilesSimData__interpolated_gripper  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers InputFilesSimData_message_members = {
  "input_filenames_msg::msg",  // message namespace
  "InputFilesSimData",  // message name
  5,  // number of fields
  sizeof(input_filenames_msg::msg::InputFilesSimData),
  InputFilesSimData_message_member_array,  // message members
  InputFilesSimData_init_function,  // function to initialize message memory (memory has to be allocated)
  InputFilesSimData_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t InputFilesSimData_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &InputFilesSimData_message_members,
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
get_message_type_support_handle<input_filenames_msg::msg::InputFilesSimData>()
{
  return &::input_filenames_msg::msg::rosidl_typesupport_introspection_cpp::InputFilesSimData_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, input_filenames_msg, msg, InputFilesSimData)() {
  return &::input_filenames_msg::msg::rosidl_typesupport_introspection_cpp::InputFilesSimData_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
