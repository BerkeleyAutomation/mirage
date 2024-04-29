// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from input_filenames_msg:msg/MultipleInpaintImages.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__MULTIPLE_INPAINT_IMAGES__STRUCT_HPP_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__MULTIPLE_INPAINT_IMAGES__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'images'
#include "sensor_msgs/msg/detail/image__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__input_filenames_msg__msg__MultipleInpaintImages __attribute__((deprecated))
#else
# define DEPRECATED__input_filenames_msg__msg__MultipleInpaintImages __declspec(deprecated)
#endif

namespace input_filenames_msg
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct MultipleInpaintImages_
{
  using Type = MultipleInpaintImages_<ContainerAllocator>;

  explicit MultipleInpaintImages_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit MultipleInpaintImages_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _images_type =
    std::vector<sensor_msgs::msg::Image_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<sensor_msgs::msg::Image_<ContainerAllocator>>>;
  _images_type images;

  // setters for named parameter idiom
  Type & set__images(
    const std::vector<sensor_msgs::msg::Image_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<sensor_msgs::msg::Image_<ContainerAllocator>>> & _arg)
  {
    this->images = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    input_filenames_msg::msg::MultipleInpaintImages_<ContainerAllocator> *;
  using ConstRawPtr =
    const input_filenames_msg::msg::MultipleInpaintImages_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<input_filenames_msg::msg::MultipleInpaintImages_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<input_filenames_msg::msg::MultipleInpaintImages_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      input_filenames_msg::msg::MultipleInpaintImages_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<input_filenames_msg::msg::MultipleInpaintImages_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      input_filenames_msg::msg::MultipleInpaintImages_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<input_filenames_msg::msg::MultipleInpaintImages_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<input_filenames_msg::msg::MultipleInpaintImages_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<input_filenames_msg::msg::MultipleInpaintImages_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__input_filenames_msg__msg__MultipleInpaintImages
    std::shared_ptr<input_filenames_msg::msg::MultipleInpaintImages_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__input_filenames_msg__msg__MultipleInpaintImages
    std::shared_ptr<input_filenames_msg::msg::MultipleInpaintImages_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MultipleInpaintImages_ & other) const
  {
    if (this->images != other.images) {
      return false;
    }
    return true;
  }
  bool operator!=(const MultipleInpaintImages_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MultipleInpaintImages_

// alias to use template instance with default allocator
using MultipleInpaintImages =
  input_filenames_msg::msg::MultipleInpaintImages_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace input_filenames_msg

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__MULTIPLE_INPAINT_IMAGES__STRUCT_HPP_
