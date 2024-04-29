// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from input_filenames_msg:msg/InputFilesFrankaToFranka.idl
// generated code does not contain a copyright notice
#include "input_filenames_msg/msg/detail/input_files_franka_to_franka__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `rgb`
#include "sensor_msgs/msg/detail/image__functions.h"
// Member `joints`
#include "rosidl_runtime_c/primitives_sequence_functions.h"
// Member `demo_num`
// Member `traj_num`
#include "std_msgs/msg/detail/int16__functions.h"

bool
input_filenames_msg__msg__InputFilesFrankaToFranka__init(input_filenames_msg__msg__InputFilesFrankaToFranka * msg)
{
  if (!msg) {
    return false;
  }
  // rgb
  if (!sensor_msgs__msg__Image__init(&msg->rgb)) {
    input_filenames_msg__msg__InputFilesFrankaToFranka__fini(msg);
    return false;
  }
  // joints
  if (!rosidl_runtime_c__double__Sequence__init(&msg->joints, 0)) {
    input_filenames_msg__msg__InputFilesFrankaToFranka__fini(msg);
    return false;
  }
  // demo_num
  if (!std_msgs__msg__Int16__init(&msg->demo_num)) {
    input_filenames_msg__msg__InputFilesFrankaToFranka__fini(msg);
    return false;
  }
  // traj_num
  if (!std_msgs__msg__Int16__init(&msg->traj_num)) {
    input_filenames_msg__msg__InputFilesFrankaToFranka__fini(msg);
    return false;
  }
  return true;
}

void
input_filenames_msg__msg__InputFilesFrankaToFranka__fini(input_filenames_msg__msg__InputFilesFrankaToFranka * msg)
{
  if (!msg) {
    return;
  }
  // rgb
  sensor_msgs__msg__Image__fini(&msg->rgb);
  // joints
  rosidl_runtime_c__double__Sequence__fini(&msg->joints);
  // demo_num
  std_msgs__msg__Int16__fini(&msg->demo_num);
  // traj_num
  std_msgs__msg__Int16__fini(&msg->traj_num);
}

bool
input_filenames_msg__msg__InputFilesFrankaToFranka__are_equal(const input_filenames_msg__msg__InputFilesFrankaToFranka * lhs, const input_filenames_msg__msg__InputFilesFrankaToFranka * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // rgb
  if (!sensor_msgs__msg__Image__are_equal(
      &(lhs->rgb), &(rhs->rgb)))
  {
    return false;
  }
  // joints
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->joints), &(rhs->joints)))
  {
    return false;
  }
  // demo_num
  if (!std_msgs__msg__Int16__are_equal(
      &(lhs->demo_num), &(rhs->demo_num)))
  {
    return false;
  }
  // traj_num
  if (!std_msgs__msg__Int16__are_equal(
      &(lhs->traj_num), &(rhs->traj_num)))
  {
    return false;
  }
  return true;
}

bool
input_filenames_msg__msg__InputFilesFrankaToFranka__copy(
  const input_filenames_msg__msg__InputFilesFrankaToFranka * input,
  input_filenames_msg__msg__InputFilesFrankaToFranka * output)
{
  if (!input || !output) {
    return false;
  }
  // rgb
  if (!sensor_msgs__msg__Image__copy(
      &(input->rgb), &(output->rgb)))
  {
    return false;
  }
  // joints
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->joints), &(output->joints)))
  {
    return false;
  }
  // demo_num
  if (!std_msgs__msg__Int16__copy(
      &(input->demo_num), &(output->demo_num)))
  {
    return false;
  }
  // traj_num
  if (!std_msgs__msg__Int16__copy(
      &(input->traj_num), &(output->traj_num)))
  {
    return false;
  }
  return true;
}

input_filenames_msg__msg__InputFilesFrankaToFranka *
input_filenames_msg__msg__InputFilesFrankaToFranka__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  input_filenames_msg__msg__InputFilesFrankaToFranka * msg = (input_filenames_msg__msg__InputFilesFrankaToFranka *)allocator.allocate(sizeof(input_filenames_msg__msg__InputFilesFrankaToFranka), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(input_filenames_msg__msg__InputFilesFrankaToFranka));
  bool success = input_filenames_msg__msg__InputFilesFrankaToFranka__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
input_filenames_msg__msg__InputFilesFrankaToFranka__destroy(input_filenames_msg__msg__InputFilesFrankaToFranka * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    input_filenames_msg__msg__InputFilesFrankaToFranka__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
input_filenames_msg__msg__InputFilesFrankaToFranka__Sequence__init(input_filenames_msg__msg__InputFilesFrankaToFranka__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  input_filenames_msg__msg__InputFilesFrankaToFranka * data = NULL;

  if (size) {
    data = (input_filenames_msg__msg__InputFilesFrankaToFranka *)allocator.zero_allocate(size, sizeof(input_filenames_msg__msg__InputFilesFrankaToFranka), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = input_filenames_msg__msg__InputFilesFrankaToFranka__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        input_filenames_msg__msg__InputFilesFrankaToFranka__fini(&data[i - 1]);
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
input_filenames_msg__msg__InputFilesFrankaToFranka__Sequence__fini(input_filenames_msg__msg__InputFilesFrankaToFranka__Sequence * array)
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
      input_filenames_msg__msg__InputFilesFrankaToFranka__fini(&array->data[i]);
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

input_filenames_msg__msg__InputFilesFrankaToFranka__Sequence *
input_filenames_msg__msg__InputFilesFrankaToFranka__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  input_filenames_msg__msg__InputFilesFrankaToFranka__Sequence * array = (input_filenames_msg__msg__InputFilesFrankaToFranka__Sequence *)allocator.allocate(sizeof(input_filenames_msg__msg__InputFilesFrankaToFranka__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = input_filenames_msg__msg__InputFilesFrankaToFranka__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
input_filenames_msg__msg__InputFilesFrankaToFranka__Sequence__destroy(input_filenames_msg__msg__InputFilesFrankaToFranka__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    input_filenames_msg__msg__InputFilesFrankaToFranka__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
input_filenames_msg__msg__InputFilesFrankaToFranka__Sequence__are_equal(const input_filenames_msg__msg__InputFilesFrankaToFranka__Sequence * lhs, const input_filenames_msg__msg__InputFilesFrankaToFranka__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!input_filenames_msg__msg__InputFilesFrankaToFranka__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
input_filenames_msg__msg__InputFilesFrankaToFranka__Sequence__copy(
  const input_filenames_msg__msg__InputFilesFrankaToFranka__Sequence * input,
  input_filenames_msg__msg__InputFilesFrankaToFranka__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(input_filenames_msg__msg__InputFilesFrankaToFranka);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    input_filenames_msg__msg__InputFilesFrankaToFranka * data =
      (input_filenames_msg__msg__InputFilesFrankaToFranka *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!input_filenames_msg__msg__InputFilesFrankaToFranka__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          input_filenames_msg__msg__InputFilesFrankaToFranka__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!input_filenames_msg__msg__InputFilesFrankaToFranka__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
