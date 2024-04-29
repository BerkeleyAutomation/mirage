// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from input_filenames_msg:msg/InputFilesData.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_DATA__STRUCT_HPP_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_DATA__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'segmentation_data'
#include "sensor_msgs/msg/detail/image__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__input_filenames_msg__msg__InputFilesData __attribute__((deprecated))
#else
# define DEPRECATED__input_filenames_msg__msg__InputFilesData __declspec(deprecated)
#endif

namespace input_filenames_msg
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct InputFilesData_
{
  using Type = InputFilesData_<ContainerAllocator>;

  explicit InputFilesData_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : segmentation_data(_init)
  {
    (void)_init;
  }

  explicit InputFilesData_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : segmentation_data(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _depth_data_type =
    std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>>;
  _depth_data_type depth_data;
  using _segmentation_data_type =
    sensor_msgs::msg::Image_<ContainerAllocator>;
  _segmentation_data_type segmentation_data;
  using _joints_type =
    std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>>;
  _joints_type joints;

  // setters for named parameter idiom
  Type & set__depth_data(
    const std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> & _arg)
  {
    this->depth_data = _arg;
    return *this;
  }
  Type & set__segmentation_data(
    const sensor_msgs::msg::Image_<ContainerAllocator> & _arg)
  {
    this->segmentation_data = _arg;
    return *this;
  }
  Type & set__joints(
    const std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> & _arg)
  {
    this->joints = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    input_filenames_msg::msg::InputFilesData_<ContainerAllocator> *;
  using ConstRawPtr =
    const input_filenames_msg::msg::InputFilesData_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<input_filenames_msg::msg::InputFilesData_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<input_filenames_msg::msg::InputFilesData_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      input_filenames_msg::msg::InputFilesData_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<input_filenames_msg::msg::InputFilesData_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      input_filenames_msg::msg::InputFilesData_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<input_filenames_msg::msg::InputFilesData_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<input_filenames_msg::msg::InputFilesData_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<input_filenames_msg::msg::InputFilesData_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__input_filenames_msg__msg__InputFilesData
    std::shared_ptr<input_filenames_msg::msg::InputFilesData_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__input_filenames_msg__msg__InputFilesData
    std::shared_ptr<input_filenames_msg::msg::InputFilesData_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const InputFilesData_ & other) const
  {
    if (this->depth_data != other.depth_data) {
      return false;
    }
    if (this->segmentation_data != other.segmentation_data) {
      return false;
    }
    if (this->joints != other.joints) {
      return false;
    }
    return true;
  }
  bool operator!=(const InputFilesData_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct InputFilesData_

// alias to use template instance with default allocator
using InputFilesData =
  input_filenames_msg::msg::InputFilesData_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace input_filenames_msg

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_DATA__STRUCT_HPP_
