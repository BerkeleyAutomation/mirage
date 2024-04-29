// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from input_filenames_msg:msg/InputFilesRealDataMulti.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_REAL_DATA_MULTI__BUILDER_HPP_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_REAL_DATA_MULTI__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "input_filenames_msg/msg/detail/input_files_real_data_multi__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace input_filenames_msg
{

namespace msg
{

namespace builder
{

class Init_InputFilesRealDataMulti_data_pieces
{
public:
  Init_InputFilesRealDataMulti_data_pieces()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::input_filenames_msg::msg::InputFilesRealDataMulti data_pieces(::input_filenames_msg::msg::InputFilesRealDataMulti::_data_pieces_type arg)
  {
    msg_.data_pieces = std::move(arg);
    return std::move(msg_);
  }

private:
  ::input_filenames_msg::msg::InputFilesRealDataMulti msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::input_filenames_msg::msg::InputFilesRealDataMulti>()
{
  return input_filenames_msg::msg::builder::Init_InputFilesRealDataMulti_data_pieces();
}

}  // namespace input_filenames_msg

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_REAL_DATA_MULTI__BUILDER_HPP_
