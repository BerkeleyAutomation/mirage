// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from input_filenames_msg:msg/InputFilesRealDataMulti.idl
// generated code does not contain a copyright notice
#include "input_filenames_msg/msg/detail/input_files_real_data_multi__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `data_pieces`
#include "input_filenames_msg/msg/detail/input_files_real_data__functions.h"

bool
input_filenames_msg__msg__InputFilesRealDataMulti__init(input_filenames_msg__msg__InputFilesRealDataMulti * msg)
{
  if (!msg) {
    return false;
  }
  // data_pieces
  if (!input_filenames_msg__msg__InputFilesRealData__Sequence__init(&msg->data_pieces, 0)) {
    input_filenames_msg__msg__InputFilesRealDataMulti__fini(msg);
    return false;
  }
  return true;
}

void
input_filenames_msg__msg__InputFilesRealDataMulti__fini(input_filenames_msg__msg__InputFilesRealDataMulti * msg)
{
  if (!msg) {
    return;
  }
  // data_pieces
  input_filenames_msg__msg__InputFilesRealData__Sequence__fini(&msg->data_pieces);
}

bool
input_filenames_msg__msg__InputFilesRealDataMulti__are_equal(const input_filenames_msg__msg__InputFilesRealDataMulti * lhs, const input_filenames_msg__msg__InputFilesRealDataMulti * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // data_pieces
  if (!input_filenames_msg__msg__InputFilesRealData__Sequence__are_equal(
      &(lhs->data_pieces), &(rhs->data_pieces)))
  {
    return false;
  }
  return true;
}

bool
input_filenames_msg__msg__InputFilesRealDataMulti__copy(
  const input_filenames_msg__msg__InputFilesRealDataMulti * input,
  input_filenames_msg__msg__InputFilesRealDataMulti * output)
{
  if (!input || !output) {
    return false;
  }
  // data_pieces
  if (!input_filenames_msg__msg__InputFilesRealData__Sequence__copy(
      &(input->data_pieces), &(output->data_pieces)))
  {
    return false;
  }
  return true;
}

input_filenames_msg__msg__InputFilesRealDataMulti *
input_filenames_msg__msg__InputFilesRealDataMulti__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  input_filenames_msg__msg__InputFilesRealDataMulti * msg = (input_filenames_msg__msg__InputFilesRealDataMulti *)allocator.allocate(sizeof(input_filenames_msg__msg__InputFilesRealDataMulti), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(input_filenames_msg__msg__InputFilesRealDataMulti));
  bool success = input_filenames_msg__msg__InputFilesRealDataMulti__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
input_filenames_msg__msg__InputFilesRealDataMulti__destroy(input_filenames_msg__msg__InputFilesRealDataMulti * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    input_filenames_msg__msg__InputFilesRealDataMulti__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
input_filenames_msg__msg__InputFilesRealDataMulti__Sequence__init(input_filenames_msg__msg__InputFilesRealDataMulti__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  input_filenames_msg__msg__InputFilesRealDataMulti * data = NULL;

  if (size) {
    data = (input_filenames_msg__msg__InputFilesRealDataMulti *)allocator.zero_allocate(size, sizeof(input_filenames_msg__msg__InputFilesRealDataMulti), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = input_filenames_msg__msg__InputFilesRealDataMulti__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        input_filenames_msg__msg__InputFilesRealDataMulti__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
input_filenames_msg__msg__InputFilesRealDataMulti__Sequence__fini(input_filenames_msg__msg__InputFilesRealDataMulti__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      input_filenames_msg__msg__InputFilesRealDataMulti__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

input_filenames_msg__msg__InputFilesRealDataMulti__Sequence *
input_filenames_msg__msg__InputFilesRealDataMulti__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  input_filenames_msg__msg__InputFilesRealDataMulti__Sequence * array = (input_filenames_msg__msg__InputFilesRealDataMulti__Sequence *)allocator.allocate(sizeof(input_filenames_msg__msg__InputFilesRealDataMulti__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = input_filenames_msg__msg__InputFilesRealDataMulti__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
input_filenames_msg__msg__InputFilesRealDataMulti__Sequence__destroy(input_filenames_msg__msg__InputFilesRealDataMulti__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    input_filenames_msg__msg__InputFilesRealDataMulti__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
input_filenames_msg__msg__InputFilesRealDataMulti__Sequence__are_equal(const input_filenames_msg__msg__InputFilesRealDataMulti__Sequence * lhs, const input_filenames_msg__msg__InputFilesRealDataMulti__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!input_filenames_msg__msg__InputFilesRealDataMulti__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
input_filenames_msg__msg__InputFilesRealDataMulti__Sequence__copy(
  const input_filenames_msg__msg__InputFilesRealDataMulti__Sequence * input,
  input_filenames_msg__msg__InputFilesRealDataMulti__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(input_filenames_msg__msg__InputFilesRealDataMulti);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    input_filenames_msg__msg__InputFilesRealDataMulti * data =
      (input_filenames_msg__msg__InputFilesRealDataMulti *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!input_filenames_msg__msg__InputFilesRealDataMulti__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          input_filenames_msg__msg__InputFilesRealDataMulti__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!input_filenames_msg__msg__InputFilesRealDataMulti__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
