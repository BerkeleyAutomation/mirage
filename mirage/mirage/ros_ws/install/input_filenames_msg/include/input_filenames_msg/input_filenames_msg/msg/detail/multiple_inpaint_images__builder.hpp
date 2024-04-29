// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from input_filenames_msg:msg/MultipleInpaintImages.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__MULTIPLE_INPAINT_IMAGES__BUILDER_HPP_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__MULTIPLE_INPAINT_IMAGES__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "input_filenames_msg/msg/detail/multiple_inpaint_images__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace input_filenames_msg
{

namespace msg
{

namespace builder
{

class Init_MultipleInpaintImages_images
{
public:
  Init_MultipleInpaintImages_images()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::input_filenames_msg::msg::MultipleInpaintImages images(::input_filenames_msg::msg::MultipleInpaintImages::_images_type arg)
  {
    msg_.images = std::move(arg);
    return std::move(msg_);
  }

private:
  ::input_filenames_msg::msg::MultipleInpaintImages msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::input_filenames_msg::msg::MultipleInpaintImages>()
{
  return input_filenames_msg::msg::builder::Init_MultipleInpaintImages_images();
}

}  // namespace input_filenames_msg

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__MULTIPLE_INPAINT_IMAGES__BUILDER_HPP_
