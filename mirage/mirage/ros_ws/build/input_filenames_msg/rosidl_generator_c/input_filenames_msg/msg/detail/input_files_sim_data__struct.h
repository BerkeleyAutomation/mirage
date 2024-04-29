// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from input_filenames_msg:msg/InputFilesSimData.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_SIM_DATA__STRUCT_H_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_SIM_DATA__STRUCT_H_

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
// Member 'segmentation'
// Member 'ee_pose'
// Member 'interpolated_gripper'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in msg/InputFilesSimData in the package input_filenames_msg.
typedef struct input_filenames_msg__msg__InputFilesSimData
{
  sensor_msgs__msg__Image rgb;
  rosidl_runtime_c__double__Sequence depth_map;
  rosidl_runtime_c__uint8__Sequence segmentation;
  rosidl_runtime_c__double__Sequence ee_pose;
  rosidl_runtime_c__double__Sequence interpolated_gripper;
} input_filenames_msg__msg__InputFilesSimData;

// Struct for a sequence of input_filenames_msg__msg__InputFilesSimData.
typedef struct input_filenames_msg__msg__InputFilesSimData__Sequence
{
  input_filenames_msg__msg__InputFilesSimData * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} input_filenames_msg__msg__InputFilesSimData__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_SIM_DATA__STRUCT_H_
