// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from input_filenames_msg:msg/InputFilesSimData.idl
// generated code does not contain a copyright notice
#include "input_filenames_msg/msg/detail/input_files_sim_data__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `rgb`
#include "sensor_msgs/msg/detail/image__functions.h"
// Member `depth_map`
// Member `segmentation`
// Member `ee_pose`
// Member `interpolated_gripper`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
input_filenames_msg__msg__InputFilesSimData__init(input_filenames_msg__msg__InputFilesSimData * msg)
{
  if (!msg) {
    return false;
  }
  // rgb
  if (!sensor_msgs__msg__Image__init(&msg->rgb)) {
    input_filenames_msg__msg__InputFilesSimData__fini(msg);
    return false;
  }
  // depth_map
  if (!rosidl_runtime_c__double__Sequence__init(&msg->depth_map, 0)) {
    input_filenames_msg__msg__InputFilesSimData__fini(msg);
    return false;
  }
  // segmentation
  if (!rosidl_runtime_c__uint8__Sequence__init(&msg->segmentation, 0)) {
    input_filenames_msg__msg__InputFilesSimData__fini(msg);
    return false;
  }
  // ee_pose
  if (!rosidl_runtime_c__double__Sequence__init(&msg->ee_pose, 0)) {
    input_filenames_msg__msg__InputFilesSimData__fini(msg);
    return false;
  }
  // interpolated_gripper
  if (!rosidl_runtime_c__double__Sequence__init(&msg->interpolated_gripper, 0)) {
    input_filenames_msg__msg__InputFilesSimData__fini(msg);
    return false;
  }
  return true;
}

void
input_filenames_msg__msg__InputFilesSimData__fini(input_filenames_msg__msg__InputFilesSimData * msg)
{
  if (!msg) {
    return;
  }
  // rgb
  sensor_msgs__msg__Image__fini(&msg->rgb);
  // depth_map
  rosidl_runtime_c__double__Sequence__fini(&msg->depth_map);
  // segmentation
  rosidl_runtime_c__uint8__Sequence__fini(&msg->segmentation);
  // ee_pose
  rosidl_runtime_c__double__Sequence__fini(&msg->ee_pose);
  // interpolated_gripper
  rosidl_runtime_c__double__Sequence__fini(&msg->interpolated_gripper);
}

bool
input_filenames_msg__msg__InputFilesSimData__are_equal(const input_filenames_msg__msg__InputFilesSimData * lhs, const input_filenames_msg__msg__InputFilesSimData * rhs)
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
  // depth_map
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->depth_map), &(rhs->depth_map)))
  {
    return false;
  }
  // segmentation
  if (!rosidl_runtime_c__uint8__Sequence__are_equal(
      &(lhs->segmentation), &(rhs->segmentation)))
  {
    return false;
  }
  // ee_pose
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->ee_pose), &(rhs->ee_pose)))
  {
    return false;
  }
  // interpolated_gripper
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->interpolated_gripper), &(rhs->interpolated_gripper)))
  {
    return false;
  }
  return true;
}

bool
input_filenames_msg__msg__InputFilesSimData__copy(
  const input_filenames_msg__msg__InputFilesSimData * input,
  input_filenames_msg__msg__InputFilesSimData * output)
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
  // depth_map
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->depth_map), &(output->depth_map)))
  {
    return false;
  }
  // segmentation
  if (!rosidl_runtime_c__uint8__Sequence__copy(
      &(input->segmentation), &(output->segmentation)))
  {
    return false;
  }
  // ee_pose
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->ee_pose), &(output->ee_pose)))
  {
    return false;
  }
  // interpolated_gripper
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->interpolated_gripper), &(output->interpolated_gripper)))
  {
    return false;
  }
  return true;
}

input_filenames_msg__msg__InputFilesSimData *
input_filenames_msg__msg__InputFilesSimData__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  input_filenames_msg__msg__InputFilesSimData * msg = (input_filenames_msg__msg__InputFilesSimData *)allocator.allocate(sizeof(input_filenames_msg__msg__InputFilesSimData), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(input_filenames_msg__msg__InputFilesSimData));
  bool success = input_filenames_msg__msg__InputFilesSimData__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
input_filenames_msg__msg__InputFilesSimData__destroy(input_filenames_msg__msg__InputFilesSimData * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    input_filenames_msg__msg__InputFilesSimData__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
input_filenames_msg__msg__InputFilesSimData__Sequence__init(input_filenames_msg__msg__InputFilesSimData__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  input_filenames_msg__msg__InputFilesSimData * data = NULL;

  if (size) {
    data = (input_filenames_msg__msg__InputFilesSimData *)allocator.zero_allocate(size, sizeof(input_filenames_msg__msg__InputFilesSimData), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = input_filenames_msg__msg__InputFilesSimData__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        input_filenames_msg__msg__InputFilesSimData__fini(&data[i - 1]);
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
input_filenames_msg__msg__InputFilesSimData__Sequence__fini(input_filenames_msg__msg__InputFilesSimData__Sequence * array)
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
      input_filenames_msg__msg__InputFilesSimData__fini(&array->data[i]);
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

input_filenames_msg__msg__InputFilesSimData__Sequence *
input_filenames_msg__msg__InputFilesSimData__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  input_filenames_msg__msg__InputFilesSimData__Sequence * array = (input_filenames_msg__msg__InputFilesSimData__Sequence *)allocator.allocate(sizeof(input_filenames_msg__msg__InputFilesSimData__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = input_filenames_msg__msg__InputFilesSimData__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
input_filenames_msg__msg__InputFilesSimData__Sequence__destroy(input_filenames_msg__msg__InputFilesSimData__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    input_filenames_msg__msg__InputFilesSimData__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
input_filenames_msg__msg__InputFilesSimData__Sequence__are_equal(const input_filenames_msg__msg__InputFilesSimData__Sequence * lhs, const input_filenames_msg__msg__InputFilesSimData__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!input_filenames_msg__msg__InputFilesSimData__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
input_filenames_msg__msg__InputFilesSimData__Sequence__copy(
  const input_filenames_msg__msg__InputFilesSimData__Sequence * input,
  input_filenames_msg__msg__InputFilesSimData__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(input_filenames_msg__msg__InputFilesSimData);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    input_filenames_msg__msg__InputFilesSimData * data =
      (input_filenames_msg__msg__InputFilesSimData *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!input_filenames_msg__msg__InputFilesSimData__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          input_filenames_msg__msg__InputFilesSimData__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!input_filenames_msg__msg__InputFilesSimData__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
