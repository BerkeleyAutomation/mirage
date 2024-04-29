// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from input_filenames_msg:msg/InputFilesData.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_DATA__STRUCT_H_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_DATA__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'depth_data'
// Member 'joints'
#include "rosidl_runtime_c/primitives_sequence.h"
// Member 'segmentation_data'
#include "sensor_msgs/msg/detail/image__struct.h"

/// Struct defined in msg/InputFilesData in the package input_filenames_msg.
typedef struct input_filenames_msg__msg__InputFilesData
{
  rosidl_runtime_c__float__Sequence depth_data;
  sensor_msgs__msg__Image segmentation_data;
  rosidl_runtime_c__float__Sequence joints;
} input_filenames_msg__msg__InputFilesData;

// Struct for a sequence of input_filenames_msg__msg__InputFilesData.
typedef struct input_filenames_msg__msg__InputFilesData__Sequence
{
  input_filenames_msg__msg__InputFilesData * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} input_filenames_msg__msg__InputFilesData__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_DATA__STRUCT_H_
