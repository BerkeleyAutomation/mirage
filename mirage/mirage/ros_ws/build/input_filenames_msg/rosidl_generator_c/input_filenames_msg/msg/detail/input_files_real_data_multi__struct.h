// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from input_filenames_msg:msg/InputFilesRealDataMulti.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_REAL_DATA_MULTI__STRUCT_H_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_REAL_DATA_MULTI__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'data_pieces'
#include "input_filenames_msg/msg/detail/input_files_real_data__struct.h"

/// Struct defined in msg/InputFilesRealDataMulti in the package input_filenames_msg.
typedef struct input_filenames_msg__msg__InputFilesRealDataMulti
{
  input_filenames_msg__msg__InputFilesRealData__Sequence data_pieces;
} input_filenames_msg__msg__InputFilesRealDataMulti;

// Struct for a sequence of input_filenames_msg__msg__InputFilesRealDataMulti.
typedef struct input_filenames_msg__msg__InputFilesRealDataMulti__Sequence
{
  input_filenames_msg__msg__InputFilesRealDataMulti * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} input_filenames_msg__msg__InputFilesRealDataMulti__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_REAL_DATA_MULTI__STRUCT_H_
