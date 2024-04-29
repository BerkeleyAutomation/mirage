// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from input_filenames_msg:msg/InputFilesRealData.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_REAL_DATA__STRUCT_H_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_REAL_DATA__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'rgb'
#include "sensor_msgs/msg/detail/image__struct.h"
// Member 'depth_map'
// Member 'joints'
#include "rosidl_runtime_c/primitives_sequence.h"
// Member 'camera_name'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/InputFilesRealData in the package input_filenames_msg.
typedef struct input_filenames_msg__msg__InputFilesRealData
{
  sensor_msgs__msg__Image rgb;
  rosidl_runtime_c__double__Sequence depth_map;
  rosidl_runtime_c__double__Sequence joints;
  rosidl_runtime_c__String camera_name;
} input_filenames_msg__msg__InputFilesRealData;

// Struct for a sequence of input_filenames_msg__msg__InputFilesRealData.
typedef struct input_filenames_msg__msg__InputFilesRealData__Sequence
{
  input_filenames_msg__msg__InputFilesRealData * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} input_filenames_msg__msg__InputFilesRealData__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_REAL_DATA__STRUCT_H_
