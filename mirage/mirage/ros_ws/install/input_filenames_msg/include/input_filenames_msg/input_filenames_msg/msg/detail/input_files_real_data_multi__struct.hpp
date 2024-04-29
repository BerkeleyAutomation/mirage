// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from input_filenames_msg:msg/InputFilesRealDataMulti.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_REAL_DATA_MULTI__STRUCT_HPP_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_REAL_DATA_MULTI__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'data_pieces'
#include "input_filenames_msg/msg/detail/input_files_real_data__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__input_filenames_msg__msg__InputFilesRealDataMulti __attribute__((deprecated))
#else
# define DEPRECATED__input_filenames_msg__msg__InputFilesRealDataMulti __declspec(deprecated)
#endif

namespace input_filenames_msg
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct InputFilesRealDataMulti_
{
  using Type = InputFilesRealDataMulti_<ContainerAllocator>;

  explicit InputFilesRealDataMulti_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit InputFilesRealDataMulti_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _data_pieces_type =
    std::vector<input_filenames_msg::msg::InputFilesRealData_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<input_filenames_msg::msg::InputFilesRealData_<ContainerAllocator>>>;
  _data_pieces_type data_pieces;

  // setters for named parameter idiom
  Type & set__data_pieces(
    const std::vector<input_filenames_msg::msg::InputFilesRealData_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<input_filenames_msg::msg::InputFilesRealData_<ContainerAllocator>>> & _arg)
  {
    this->data_pieces = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    input_filenames_msg::msg::InputFilesRealDataMulti_<ContainerAllocator> *;
  using ConstRawPtr =
    const input_filenames_msg::msg::InputFilesRealDataMulti_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<input_filenames_msg::msg::InputFilesRealDataMulti_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<input_filenames_msg::msg::InputFilesRealDataMulti_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      input_filenames_msg::msg::InputFilesRealDataMulti_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<input_filenames_msg::msg::InputFilesRealDataMulti_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      input_filenames_msg::msg::InputFilesRealDataMulti_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<input_filenames_msg::msg::InputFilesRealDataMulti_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<input_filenames_msg::msg::InputFilesRealDataMulti_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<input_filenames_msg::msg::InputFilesRealDataMulti_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__input_filenames_msg__msg__InputFilesRealDataMulti
    std::shared_ptr<input_filenames_msg::msg::InputFilesRealDataMulti_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__input_filenames_msg__msg__InputFilesRealDataMulti
    std::shared_ptr<input_filenames_msg::msg::InputFilesRealDataMulti_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const InputFilesRealDataMulti_ & other) const
  {
    if (this->data_pieces != other.data_pieces) {
      return false;
    }
    return true;
  }
  bool operator!=(const InputFilesRealDataMulti_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct InputFilesRealDataMulti_

// alias to use template instance with default allocator
using InputFilesRealDataMulti =
  input_filenames_msg::msg::InputFilesRealDataMulti_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace input_filenames_msg

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_REAL_DATA_MULTI__STRUCT_HPP_
