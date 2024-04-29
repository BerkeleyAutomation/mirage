// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from input_filenames_msg:msg/InputFilesDiffusionData.idl
// generated code does not contain a copyright notice
#include "input_filenames_msg/msg/detail/input_files_diffusion_data__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `rgb`
// Member `depth_map`
// Member `joints`
#include "rosidl_runtime_c/primitives_sequence_functions.h"
// Member `segmentation`
#include "sensor_msgs/msg/detail/image__functions.h"
// Member `demo_num`
// Member `traj_num`
#include "std_msgs/msg/detail/int16__functions.h"

bool
input_filenames_msg__msg__InputFilesDiffusionData__init(input_filenames_msg__msg__InputFilesDiffusionData * msg)
{
  if (!msg) {
    return false;
  }
  // rgb
  if (!rosidl_runtime_c__uint8__Sequence__init(&msg->rgb, 0)) {
    input_filenames_msg__msg__InputFilesDiffusionData__fini(msg);
    return false;
  }
  // depth_map
  if (!rosidl_runtime_c__double__Sequence__init(&msg->depth_map, 0)) {
    input_filenames_msg__msg__InputFilesDiffusionData__fini(msg);
    return false;
  }
  // segmentation
  if (!sensor_msgs__msg__Image__init(&msg->segmentation)) {
    input_filenames_msg__msg__InputFilesDiffusionData__fini(msg);
    return false;
  }
  // joints
  if (!rosidl_runtime_c__double__Sequence__init(&msg->joints, 0)) {
    input_filenames_msg__msg__InputFilesDiffusionData__fini(msg);
    return false;
  }
  // demo_num
  if (!std_msgs__msg__Int16__init(&msg->demo_num)) {
    input_filenames_msg__msg__InputFilesDiffusionData__fini(msg);
    return false;
  }
  // traj_num
  if (!std_msgs__msg__Int16__init(&msg->traj_num)) {
    input_filenames_msg__msg__InputFilesDiffusionData__fini(msg);
    return false;
  }
  return true;
}

void
input_filenames_msg__msg__InputFilesDiffusionData__fini(input_filenames_msg__msg__InputFilesDiffusionData * msg)
{
  if (!msg) {
    return;
  }
  // rgb
  rosidl_runtime_c__uint8__Sequence__fini(&msg->rgb);
  // depth_map
  rosidl_runtime_c__double__Sequence__fini(&msg->depth_map);
  // segmentation
  sensor_msgs__msg__Image__fini(&msg->segmentation);
  // joints
  rosidl_runtime_c__double__Sequence__fini(&msg->joints);
  // demo_num
  std_msgs__msg__Int16__fini(&msg->demo_num);
  // traj_num
  std_msgs__msg__Int16__fini(&msg->traj_num);
}

bool
input_filenames_msg__msg__InputFilesDiffusionData__are_equal(const input_filenames_msg__msg__InputFilesDiffusionData * lhs, const input_filenames_msg__msg__InputFilesDiffusionData * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // rgb
  if (!rosidl_runtime_c__uint8__Sequence__are_equal(
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
  if (!sensor_msgs__msg__Image__are_equal(
      &(lhs->segmentation), &(rhs->segmentation)))
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
input_filenames_msg__msg__InputFilesDiffusionData__copy(
  const input_filenames_msg__msg__InputFilesDiffusionData * input,
  input_filenames_msg__msg__InputFilesDiffusionData * output)
{
  if (!input || !output) {
    return false;
  }
  // rgb
  if (!rosidl_runtime_c__uint8__Sequence__copy(
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
  if (!sensor_msgs__msg__Image__copy(
      &(input->segmentation), &(output->segmentation)))
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

input_filenames_msg__msg__InputFilesDiffusionData *
input_filenames_msg__msg__InputFilesDiffusionData__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  input_filenames_msg__msg__InputFilesDiffusionData * msg = (input_filenames_msg__msg__InputFilesDiffusionData *)allocator.allocate(sizeof(input_filenames_msg__msg__InputFilesDiffusionData), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(input_filenames_msg__msg__InputFilesDiffusionData));
  bool success = input_filenames_msg__msg__InputFilesDiffusionData__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
input_filenames_msg__msg__InputFilesDiffusionData__destroy(input_filenames_msg__msg__InputFilesDiffusionData * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    input_filenames_msg__msg__InputFilesDiffusionData__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
input_filenames_msg__msg__InputFilesDiffusionData__Sequence__init(input_filenames_msg__msg__InputFilesDiffusionData__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  input_filenames_msg__msg__InputFilesDiffusionData * data = NULL;

  if (size) {
    data = (input_filenames_msg__msg__InputFilesDiffusionData *)allocator.zero_allocate(size, sizeof(input_filenames_msg__msg__InputFilesDiffusionData), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = input_filenames_msg__msg__InputFilesDiffusionData__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        input_filenames_msg__msg__InputFilesDiffusionData__fini(&data[i - 1]);
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
input_filenames_msg__msg__InputFilesDiffusionData__Sequence__fini(input_filenames_msg__msg__InputFilesDiffusionData__Sequence * array)
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
      input_filenames_msg__msg__InputFilesDiffusionData__fini(&array->data[i]);
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

input_filenames_msg__msg__InputFilesDiffusionData__Sequence *
input_filenames_msg__msg__InputFilesDiffusionData__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  input_filenames_msg__msg__InputFilesDiffusionData__Sequence * array = (input_filenames_msg__msg__InputFilesDiffusionData__Sequence *)allocator.allocate(sizeof(input_filenames_msg__msg__InputFilesDiffusionData__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = input_filenames_msg__msg__InputFilesDiffusionData__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
input_filenames_msg__msg__InputFilesDiffusionData__Sequence__destroy(input_filenames_msg__msg__InputFilesDiffusionData__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    input_filenames_msg__msg__InputFilesDiffusionData__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
input_filenames_msg__msg__InputFilesDiffusionData__Sequence__are_equal(const input_filenames_msg__msg__InputFilesDiffusionData__Sequence * lhs, const input_filenames_msg__msg__InputFilesDiffusionData__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!input_filenames_msg__msg__InputFilesDiffusionData__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
input_filenames_msg__msg__InputFilesDiffusionData__Sequence__copy(
  const input_filenames_msg__msg__InputFilesDiffusionData__Sequence * input,
  input_filenames_msg__msg__InputFilesDiffusionData__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(input_filenames_msg__msg__InputFilesDiffusionData);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    input_filenames_msg__msg__InputFilesDiffusionData * data =
      (input_filenames_msg__msg__InputFilesDiffusionData *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!input_filenames_msg__msg__InputFilesDiffusionData__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          input_filenames_msg__msg__InputFilesDiffusionData__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!input_filenames_msg__msg__InputFilesDiffusionData__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
