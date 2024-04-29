// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from input_filenames_msg:msg/InputFilesRobosuiteData.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_ROBOSUITE_DATA__STRUCT_H_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_ROBOSUITE_DATA__STRUCT_H_

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
// Member 'depth_map'
// Member 'joints'
#include "rosidl_runtime_c/primitives_sequence.h"
// Member 'segmentation'
#include "sensor_msgs/msg/detail/image__struct.h"

/// Struct defined in msg/InputFilesRobosuiteData in the package input_filenames_msg.
typedef struct input_filenames_msg__msg__InputFilesRobosuiteData
{
  rosidl_runtime_c__uint8__Sequence rgb;
  rosidl_runtime_c__double__Sequence depth_map;
  sensor_msgs__msg__Image segmentation;
  rosidl_runtime_c__double__Sequence joints;
} input_filenames_msg__msg__InputFilesRobosuiteData;

// Struct for a sequence of input_filenames_msg__msg__InputFilesRobosuiteData.
typedef struct input_filenames_msg__msg__InputFilesRobosuiteData__Sequence
{
  input_filenames_msg__msg__InputFilesRobosuiteData * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} input_filenames_msg__msg__InputFilesRobosuiteData__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_ROBOSUITE_DATA__STRUCT_H_
