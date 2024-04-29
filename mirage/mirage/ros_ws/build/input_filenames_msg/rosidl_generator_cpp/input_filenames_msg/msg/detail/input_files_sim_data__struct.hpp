// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from input_filenames_msg:msg/InputFilesSimData.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_SIM_DATA__STRUCT_HPP_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_SIM_DATA__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'rgb'
#include "sensor_msgs/msg/detail/image__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__input_filenames_msg__msg__InputFilesSimData __attribute__((deprecated))
#else
# define DEPRECATED__input_filenames_msg__msg__InputFilesSimData __declspec(deprecated)
#endif

namespace input_filenames_msg
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct InputFilesSimData_
{
  using Type = InputFilesSimData_<ContainerAllocator>;

  explicit InputFilesSimData_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : rgb(_init)
  {
    (void)_init;
  }

  explicit InputFilesSimData_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : rgb(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _rgb_type =
    sensor_msgs::msg::Image_<ContainerAllocator>;
  _rgb_type rgb;
  using _depth_map_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _depth_map_type depth_map;
  using _segmentation_type =
    std::vector<uint8_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<uint8_t>>;
  _segmentation_type segmentation;
  using _ee_pose_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _ee_pose_type ee_pose;
  using _interpolated_gripper_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _interpolated_gripper_type interpolated_gripper;

  // setters for named parameter idiom
  Type & set__rgb(
    const sensor_msgs::msg::Image_<ContainerAllocator> & _arg)
  {
    this->rgb = _arg;
    return *this;
  }
  Type & set__depth_map(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->depth_map = _arg;
    return *this;
  }
  Type & set__segmentation(
    const std::vector<uint8_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<uint8_t>> & _arg)
  {
    this->segmentation = _arg;
    return *this;
  }
  Type & set__ee_pose(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->ee_pose = _arg;
    return *this;
  }
  Type & set__interpolated_gripper(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->interpolated_gripper = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    input_filenames_msg::msg::InputFilesSimData_<ContainerAllocator> *;
  using ConstRawPtr =
    const input_filenames_msg::msg::InputFilesSimData_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<input_filenames_msg::msg::InputFilesSimData_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<input_filenames_msg::msg::InputFilesSimData_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      input_filenames_msg::msg::InputFilesSimData_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<input_filenames_msg::msg::InputFilesSimData_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      input_filenames_msg::msg::InputFilesSimData_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<input_filenames_msg::msg::InputFilesSimData_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<input_filenames_msg::msg::InputFilesSimData_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<input_filenames_msg::msg::InputFilesSimData_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__input_filenames_msg__msg__InputFilesSimData
    std::shared_ptr<input_filenames_msg::msg::InputFilesSimData_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__input_filenames_msg__msg__InputFilesSimData
    std::shared_ptr<input_filenames_msg::msg::InputFilesSimData_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const InputFilesSimData_ & other) const
  {
    if (this->rgb != other.rgb) {
      return false;
    }
    if (this->depth_map != other.depth_map) {
      return false;
    }
    if (this->segmentation != other.segmentation) {
      return false;
    }
    if (this->ee_pose != other.ee_pose) {
      return false;
    }
    if (this->interpolated_gripper != other.interpolated_gripper) {
      return false;
    }
    return true;
  }
  bool operator!=(const InputFilesSimData_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct InputFilesSimData_

// alias to use template instance with default allocator
using InputFilesSimData =
  input_filenames_msg::msg::InputFilesSimData_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace input_filenames_msg

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_SIM_DATA__STRUCT_HPP_
