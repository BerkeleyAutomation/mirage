// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from input_filenames_msg:msg/MultipleInpaintImages.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "input_filenames_msg/msg/detail/multiple_inpaint_images__struct.hpp"
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

void MultipleInpaintImages_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) input_filenames_msg::msg::MultipleInpaintImages(_init);
}

void MultipleInpaintImages_fini_function(void * message_memory)
{
  auto typed_message = static_cast<input_filenames_msg::msg::MultipleInpaintImages *>(message_memory);
  typed_message->~MultipleInpaintImages();
}

size_t size_function__MultipleInpaintImages__images(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<sensor_msgs::msg::Image> *>(untyped_member);
  return member->size();
}

const void * get_const_function__MultipleInpaintImages__images(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<sensor_msgs::msg::Image> *>(untyped_member);
  return &member[index];
}

void * get_function__MultipleInpaintImages__images(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<sensor_msgs::msg::Image> *>(untyped_member);
  return &member[index];
}

void fetch_function__MultipleInpaintImages__images(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const sensor_msgs::msg::Image *>(
    get_const_function__MultipleInpaintImages__images(untyped_member, index));
  auto & value = *reinterpret_cast<sensor_msgs::msg::Image *>(untyped_value);
  value = item;
}

void assign_function__MultipleInpaintImages__images(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<sensor_msgs::msg::Image *>(
    get_function__MultipleInpaintImages__images(untyped_member, index));
  const auto & value = *reinterpret_cast<const sensor_msgs::msg::Image *>(untyped_value);
  item = value;
}

void resize_function__MultipleInpaintImages__images(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<sensor_msgs::msg::Image> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember MultipleInpaintImages_message_member_array[1] = {
  {
    "images",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<sensor_msgs::msg::Image>(),  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(input_filenames_msg::msg::MultipleInpaintImages, images),  // bytes offset in struct
    nullptr,  // default value
    size_function__MultipleInpaintImages__images,  // size() function pointer
    get_const_function__MultipleInpaintImages__images,  // get_const(index) function pointer
    get_function__MultipleInpaintImages__images,  // get(index) function pointer
    fetch_function__MultipleInpaintImages__images,  // fetch(index, &value) function pointer
    assign_function__MultipleInpaintImages__images,  // assign(index, value) function pointer
    resize_function__MultipleInpaintImages__images  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers MultipleInpaintImages_message_members = {
  "input_filenames_msg::msg",  // message namespace
  "MultipleInpaintImages",  // message name
  1,  // number of fields
  sizeof(input_filenames_msg::msg::MultipleInpaintImages),
  MultipleInpaintImages_message_member_array,  // message members
  MultipleInpaintImages_init_function,  // function to initialize message memory (memory has to be allocated)
  MultipleInpaintImages_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t MultipleInpaintImages_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &MultipleInpaintImages_message_members,
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
get_message_type_support_handle<input_filenames_msg::msg::MultipleInpaintImages>()
{
  return &::input_filenames_msg::msg::rosidl_typesupport_introspection_cpp::MultipleInpaintImages_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, input_filenames_msg, msg, MultipleInpaintImages)() {
  return &::input_filenames_msg::msg::rosidl_typesupport_introspection_cpp::MultipleInpaintImages_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
