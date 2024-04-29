// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from input_filenames_msg:msg/InputFilesFrankaToFranka.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_FRANKA_TO_FRANKA__STRUCT_HPP_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_FRANKA_TO_FRANKA__STRUCT_HPP_

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
// Member 'demo_num'
// Member 'traj_num'
#include "std_msgs/msg/detail/int16__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__input_filenames_msg__msg__InputFilesFrankaToFranka __attribute__((deprecated))
#else
# define DEPRECATED__input_filenames_msg__msg__InputFilesFrankaToFranka __declspec(deprecated)
#endif

namespace input_filenames_msg
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct InputFilesFrankaToFranka_
{
  using Type = InputFilesFrankaToFranka_<ContainerAllocator>;

  explicit InputFilesFrankaToFranka_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : rgb(_init),
    demo_num(_init),
    traj_num(_init)
  {
    (void)_init;
  }

  explicit InputFilesFrankaToFranka_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : rgb(_alloc, _init),
    demo_num(_alloc, _init),
    traj_num(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _rgb_type =
    sensor_msgs::msg::Image_<ContainerAllocator>;
  _rgb_type rgb;
  using _joints_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _joints_type joints;
  using _demo_num_type =
    std_msgs::msg::Int16_<ContainerAllocator>;
  _demo_num_type demo_num;
  using _traj_num_type =
    std_msgs::msg::Int16_<ContainerAllocator>;
  _traj_num_type traj_num;

  // setters for named parameter idiom
  Type & set__rgb(
    const sensor_msgs::msg::Image_<ContainerAllocator> & _arg)
  {
    this->rgb = _arg;
    return *this;
  }
  Type & set__joints(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->joints = _arg;
    return *this;
  }
  Type & set__demo_num(
    const std_msgs::msg::Int16_<ContainerAllocator> & _arg)
  {
    this->demo_num = _arg;
    return *this;
  }
  Type & set__traj_num(
    const std_msgs::msg::Int16_<ContainerAllocator> & _arg)
  {
    this->traj_num = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    input_filenames_msg::msg::InputFilesFrankaToFranka_<ContainerAllocator> *;
  using ConstRawPtr =
    const input_filenames_msg::msg::InputFilesFrankaToFranka_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<input_filenames_msg::msg::InputFilesFrankaToFranka_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<input_filenames_msg::msg::InputFilesFrankaToFranka_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      input_filenames_msg::msg::InputFilesFrankaToFranka_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<input_filenames_msg::msg::InputFilesFrankaToFranka_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      input_filenames_msg::msg::InputFilesFrankaToFranka_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<input_filenames_msg::msg::InputFilesFrankaToFranka_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<input_filenames_msg::msg::InputFilesFrankaToFranka_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<input_filenames_msg::msg::InputFilesFrankaToFranka_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__input_filenames_msg__msg__InputFilesFrankaToFranka
    std::shared_ptr<input_filenames_msg::msg::InputFilesFrankaToFranka_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__input_filenames_msg__msg__InputFilesFrankaToFranka
    std::shared_ptr<input_filenames_msg::msg::InputFilesFrankaToFranka_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const InputFilesFrankaToFranka_ & other) const
  {
    if (this->rgb != other.rgb) {
      return false;
    }
    if (this->joints != other.joints) {
      return false;
    }
    if (this->demo_num != other.demo_num) {
      return false;
    }
    if (this->traj_num != other.traj_num) {
      return false;
    }
    return true;
  }
  bool operator!=(const InputFilesFrankaToFranka_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct InputFilesFrankaToFranka_

// alias to use template instance with default allocator
using InputFilesFrankaToFranka =
  input_filenames_msg::msg::InputFilesFrankaToFranka_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace input_filenames_msg

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_FRANKA_TO_FRANKA__STRUCT_HPP_
