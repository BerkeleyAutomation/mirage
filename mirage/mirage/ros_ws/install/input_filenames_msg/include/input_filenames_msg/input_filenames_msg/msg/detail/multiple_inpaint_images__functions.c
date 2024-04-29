// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from input_filenames_msg:msg/MultipleInpaintImages.idl
// generated code does not contain a copyright notice
#include "input_filenames_msg/msg/detail/multiple_inpaint_images__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `images`
#include "sensor_msgs/msg/detail/image__functions.h"

bool
input_filenames_msg__msg__MultipleInpaintImages__init(input_filenames_msg__msg__MultipleInpaintImages * msg)
{
  if (!msg) {
    return false;
  }
  // images
  if (!sensor_msgs__msg__Image__Sequence__init(&msg->images, 0)) {
    input_filenames_msg__msg__MultipleInpaintImages__fini(msg);
    return false;
  }
  return true;
}

void
input_filenames_msg__msg__MultipleInpaintImages__fini(input_filenames_msg__msg__MultipleInpaintImages * msg)
{
  if (!msg) {
    return;
  }
  // images
  sensor_msgs__msg__Image__Sequence__fini(&msg->images);
}

bool
input_filenames_msg__msg__MultipleInpaintImages__are_equal(const input_filenames_msg__msg__MultipleInpaintImages * lhs, const input_filenames_msg__msg__MultipleInpaintImages * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // images
  if (!sensor_msgs__msg__Image__Sequence__are_equal(
      &(lhs->images), &(rhs->images)))
  {
    return false;
  }
  return true;
}

bool
input_filenames_msg__msg__MultipleInpaintImages__copy(
  const input_filenames_msg__msg__MultipleInpaintImages * input,
  input_filenames_msg__msg__MultipleInpaintImages * output)
{
  if (!input || !output) {
    return false;
  }
  // images
  if (!sensor_msgs__msg__Image__Sequence__copy(
      &(input->images), &(output->images)))
  {
    return false;
  }
  return true;
}

input_filenames_msg__msg__MultipleInpaintImages *
input_filenames_msg__msg__MultipleInpaintImages__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  input_filenames_msg__msg__MultipleInpaintImages * msg = (input_filenames_msg__msg__MultipleInpaintImages *)allocator.allocate(sizeof(input_filenames_msg__msg__MultipleInpaintImages), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(input_filenames_msg__msg__MultipleInpaintImages));
  bool success = input_filenames_msg__msg__MultipleInpaintImages__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
input_filenames_msg__msg__MultipleInpaintImages__destroy(input_filenames_msg__msg__MultipleInpaintImages * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    input_filenames_msg__msg__MultipleInpaintImages__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
input_filenames_msg__msg__MultipleInpaintImages__Sequence__init(input_filenames_msg__msg__MultipleInpaintImages__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  input_filenames_msg__msg__MultipleInpaintImages * data = NULL;

  if (size) {
    data = (input_filenames_msg__msg__MultipleInpaintImages *)allocator.zero_allocate(size, sizeof(input_filenames_msg__msg__MultipleInpaintImages), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = input_filenames_msg__msg__MultipleInpaintImages__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        input_filenames_msg__msg__MultipleInpaintImages__fini(&data[i - 1]);
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
input_filenames_msg__msg__MultipleInpaintImages__Sequence__fini(input_filenames_msg__msg__MultipleInpaintImages__Sequence * array)
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
      input_filenames_msg__msg__MultipleInpaintImages__fini(&array->data[i]);
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

input_filenames_msg__msg__MultipleInpaintImages__Sequence *
input_filenames_msg__msg__MultipleInpaintImages__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  input_filenames_msg__msg__MultipleInpaintImages__Sequence * array = (input_filenames_msg__msg__MultipleInpaintImages__Sequence *)allocator.allocate(sizeof(input_filenames_msg__msg__MultipleInpaintImages__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = input_filenames_msg__msg__MultipleInpaintImages__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
input_filenames_msg__msg__MultipleInpaintImages__Sequence__destroy(input_filenames_msg__msg__MultipleInpaintImages__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    input_filenames_msg__msg__MultipleInpaintImages__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
input_filenames_msg__msg__MultipleInpaintImages__Sequence__are_equal(const input_filenames_msg__msg__MultipleInpaintImages__Sequence * lhs, const input_filenames_msg__msg__MultipleInpaintImages__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!input_filenames_msg__msg__MultipleInpaintImages__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
input_filenames_msg__msg__MultipleInpaintImages__Sequence__copy(
  const input_filenames_msg__msg__MultipleInpaintImages__Sequence * input,
  input_filenames_msg__msg__MultipleInpaintImages__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(input_filenames_msg__msg__MultipleInpaintImages);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    input_filenames_msg__msg__MultipleInpaintImages * data =
      (input_filenames_msg__msg__MultipleInpaintImages *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!input_filenames_msg__msg__MultipleInpaintImages__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          input_filenames_msg__msg__MultipleInpaintImages__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!input_filenames_msg__msg__MultipleInpaintImages__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
