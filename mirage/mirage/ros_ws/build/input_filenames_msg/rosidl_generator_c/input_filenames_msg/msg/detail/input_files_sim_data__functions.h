// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from input_filenames_msg:msg/InputFilesSimData.idl
// generated code does not contain a copyright notice

#ifndef INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_SIM_DATA__FUNCTIONS_H_
#define INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_SIM_DATA__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "input_filenames_msg/msg/rosidl_generator_c__visibility_control.h"

#include "input_filenames_msg/msg/detail/input_files_sim_data__struct.h"

/// Initialize msg/InputFilesSimData message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * input_filenames_msg__msg__InputFilesSimData
 * )) before or use
 * input_filenames_msg__msg__InputFilesSimData__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_input_filenames_msg
bool
input_filenames_msg__msg__InputFilesSimData__init(input_filenames_msg__msg__InputFilesSimData * msg);

/// Finalize msg/InputFilesSimData message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_input_filenames_msg
void
input_filenames_msg__msg__InputFilesSimData__fini(input_filenames_msg__msg__InputFilesSimData * msg);

/// Create msg/InputFilesSimData message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * input_filenames_msg__msg__InputFilesSimData__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_input_filenames_msg
input_filenames_msg__msg__InputFilesSimData *
input_filenames_msg__msg__InputFilesSimData__create();

/// Destroy msg/InputFilesSimData message.
/**
 * It calls
 * input_filenames_msg__msg__InputFilesSimData__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_input_filenames_msg
void
input_filenames_msg__msg__InputFilesSimData__destroy(input_filenames_msg__msg__InputFilesSimData * msg);

/// Check for msg/InputFilesSimData message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_input_filenames_msg
bool
input_filenames_msg__msg__InputFilesSimData__are_equal(const input_filenames_msg__msg__InputFilesSimData * lhs, const input_filenames_msg__msg__InputFilesSimData * rhs);

/// Copy a msg/InputFilesSimData message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_input_filenames_msg
bool
input_filenames_msg__msg__InputFilesSimData__copy(
  const input_filenames_msg__msg__InputFilesSimData * input,
  input_filenames_msg__msg__InputFilesSimData * output);

/// Initialize array of msg/InputFilesSimData messages.
/**
 * It allocates the memory for the number of elements and calls
 * input_filenames_msg__msg__InputFilesSimData__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_input_filenames_msg
bool
input_filenames_msg__msg__InputFilesSimData__Sequence__init(input_filenames_msg__msg__InputFilesSimData__Sequence * array, size_t size);

/// Finalize array of msg/InputFilesSimData messages.
/**
 * It calls
 * input_filenames_msg__msg__InputFilesSimData__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_input_filenames_msg
void
input_filenames_msg__msg__InputFilesSimData__Sequence__fini(input_filenames_msg__msg__InputFilesSimData__Sequence * array);

/// Create array of msg/InputFilesSimData messages.
/**
 * It allocates the memory for the array and calls
 * input_filenames_msg__msg__InputFilesSimData__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_input_filenames_msg
input_filenames_msg__msg__InputFilesSimData__Sequence *
input_filenames_msg__msg__InputFilesSimData__Sequence__create(size_t size);

/// Destroy array of msg/InputFilesSimData messages.
/**
 * It calls
 * input_filenames_msg__msg__InputFilesSimData__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_input_filenames_msg
void
input_filenames_msg__msg__InputFilesSimData__Sequence__destroy(input_filenames_msg__msg__InputFilesSimData__Sequence * array);

/// Check for msg/InputFilesSimData message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_input_filenames_msg
bool
input_filenames_msg__msg__InputFilesSimData__Sequence__are_equal(const input_filenames_msg__msg__InputFilesSimData__Sequence * lhs, const input_filenames_msg__msg__InputFilesSimData__Sequence * rhs);

/// Copy an array of msg/InputFilesSimData messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_input_filenames_msg
bool
input_filenames_msg__msg__InputFilesSimData__Sequence__copy(
  const input_filenames_msg__msg__InputFilesSimData__Sequence * input,
  input_filenames_msg__msg__InputFilesSimData__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // INPUT_FILENAMES_MSG__MSG__DETAIL__INPUT_FILES_SIM_DATA__FUNCTIONS_H_
