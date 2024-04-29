// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from input_filenames_msg:msg/InputFilesRobosuite.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_ROBOSUITE__STRUCT_H_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_ROBOSUITE__STRUCT_H_

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
// Member 'depth'
// Member 'segmentation'
// Member 'joints'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/InputFilesRobosuite in the package input_filenames_msg.
typedef struct input_filenames_msg__msg__InputFilesRobosuite
{
  rosidl_runtime_c__String rgb;
  rosidl_runtime_c__String depth;
  rosidl_runtime_c__String segmentation;
  rosidl_runtime_c__String joints;
} input_filenames_msg__msg__InputFilesRobosuite;

// Struct for a sequence of input_filenames_msg__msg__InputFilesRobosuite.
typedef struct input_filenames_msg__msg__InputFilesRobosuite__Sequence
{
  input_filenames_msg__msg__InputFilesRobosuite * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} input_filenames_msg__msg__InputFilesRobosuite__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_ROBOSUITE__STRUCT_H_
