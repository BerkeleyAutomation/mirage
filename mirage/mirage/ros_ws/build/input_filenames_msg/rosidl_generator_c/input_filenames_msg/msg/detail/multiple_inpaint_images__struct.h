// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from input_filenames_msg:msg/MultipleInpaintImages.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__MULTIPLE_INPAINT_IMAGES__STRUCT_H_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__MULTIPLE_INPAINT_IMAGES__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'images'
#include "sensor_msgs/msg/detail/image__struct.h"

/// Struct defined in msg/MultipleInpaintImages in the package input_filenames_msg.
typedef struct input_filenames_msg__msg__MultipleInpaintImages
{
  sensor_msgs__msg__Image__Sequence images;
} input_filenames_msg__msg__MultipleInpaintImages;

// Struct for a sequence of input_filenames_msg__msg__MultipleInpaintImages.
typedef struct input_filenames_msg__msg__MultipleInpaintImages__Sequence
{
  input_filenames_msg__msg__MultipleInpaintImages * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} input_filenames_msg__msg__MultipleInpaintImages__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__MULTIPLE_INPAINT_IMAGES__STRUCT_H_
