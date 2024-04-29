// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from input_filenames_msg:msg/InputFiles.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES__STRUCT_HPP_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__input_filenames_msg__msg__InputFiles __attribute__((deprecated))
#else
# define DEPRECATED__input_filenames_msg__msg__InputFiles __declspec(deprecated)
#endif

namespace input_filenames_msg
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct InputFiles_
{
  using Type = InputFiles_<ContainerAllocator>;

  explicit InputFiles_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->depth_file = "";
      this->segmentation = "";
      this->joints = "";
    }
  }

  explicit InputFiles_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : depth_file(_alloc),
    segmentation(_alloc),
    joints(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->depth_file = "";
      this->segmentation = "";
      this->joints = "";
    }
  }

  // field types and members
  using _depth_file_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _depth_file_type depth_file;
  using _segmentation_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _segmentation_type segmentation;
  using _joints_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _joints_type joints;

  // setters for named parameter idiom
  Type & set__depth_file(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->depth_file = _arg;
    return *this;
  }
  Type & set__segmentation(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->segmentation = _arg;
    return *this;
  }
  Type & set__joints(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->joints = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    input_filenames_msg::msg::InputFiles_<ContainerAllocator> *;
  using ConstRawPtr =
    const input_filenames_msg::msg::InputFiles_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<input_filenames_msg::msg::InputFiles_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<input_filenames_msg::msg::InputFiles_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      input_filenames_msg::msg::InputFiles_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<input_filenames_msg::msg::InputFiles_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      input_filenames_msg::msg::InputFiles_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<input_filenames_msg::msg::InputFiles_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<input_filenames_msg::msg::InputFiles_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<input_filenames_msg::msg::InputFiles_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__input_filenames_msg__msg__InputFiles
    std::shared_ptr<input_filenames_msg::msg::InputFiles_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__input_filenames_msg__msg__InputFiles
    std::shared_ptr<input_filenames_msg::msg::InputFiles_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const InputFiles_ & other) const
  {
    if (this->depth_file != other.depth_file) {
      return false;
    }
    if (this->segmentation != other.segmentation) {
      return false;
    }
    if (this->joints != other.joints) {
      return false;
    }
    return true;
  }
  bool operator!=(const InputFiles_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct InputFiles_

// alias to use template instance with default allocator
using InputFiles =
  input_filenames_msg::msg::InputFiles_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace input_filenames_msg

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES__STRUCT_HPP_
