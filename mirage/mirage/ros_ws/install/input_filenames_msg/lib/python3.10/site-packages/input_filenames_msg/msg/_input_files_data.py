# generated from rosidl_generator_py/resource/_idl.py.em
# with input from input_filenames_msg:msg/InputFilesData.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'depth_data'
# Member 'joints'
import array  # noqa: E402, I100

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_InputFilesData(type):
    """Metaclass of message 'InputFilesData'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('input_filenames_msg')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'input_filenames_msg.msg.InputFilesData')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__input_files_data
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__input_files_data
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__input_files_data
            cls._TYPE_SUPPORT = module.type_support_msg__msg__input_files_data
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__input_files_data

            from sensor_msgs.msg import Image
            if Image.__class__._TYPE_SUPPORT is None:
                Image.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class InputFilesData(metaclass=Metaclass_InputFilesData):
    """Message class 'InputFilesData'."""

    __slots__ = [
        '_depth_data',
        '_segmentation_data',
        '_joints',
    ]

    _fields_and_field_types = {
        'depth_data': 'sequence<float>',
        'segmentation_data': 'sensor_msgs/Image',
        'joints': 'sequence<float>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('float')),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['sensor_msgs', 'msg'], 'Image'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('float')),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.depth_data = array.array('f', kwargs.get('depth_data', []))
        from sensor_msgs.msg import Image
        self.segmentation_data = kwargs.get('segmentation_data', Image())
        self.joints = array.array('f', kwargs.get('joints', []))

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.depth_data != other.depth_data:
            return False
        if self.segmentation_data != other.segmentation_data:
            return False
        if self.joints != other.joints:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def depth_data(self):
        """Message field 'depth_data'."""
        return self._depth_data

    @depth_data.setter
    def depth_data(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'f', \
                "The 'depth_data' array.array() must have the type code of 'f'"
            self._depth_data = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -3.402823466e+38 or val > 3.402823466e+38) or math.isinf(val) for val in value)), \
                "The 'depth_data' field must be a set or sequence and each value of type 'float' and each float in [-340282346600000016151267322115014000640.000000, 340282346600000016151267322115014000640.000000]"
        self._depth_data = array.array('f', value)

    @builtins.property
    def segmentation_data(self):
        """Message field 'segmentation_data'."""
        return self._segmentation_data

    @segmentation_data.setter
    def segmentation_data(self, value):
        if __debug__:
            from sensor_msgs.msg import Image
            assert \
                isinstance(value, Image), \
                "The 'segmentation_data' field must be a sub message of type 'Image'"
        self._segmentation_data = value

    @builtins.property
    def joints(self):
        """Message field 'joints'."""
        return self._joints

    @joints.setter
    def joints(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'f', \
                "The 'joints' array.array() must have the type code of 'f'"
            self._joints = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -3.402823466e+38 or val > 3.402823466e+38) or math.isinf(val) for val in value)), \
                "The 'joints' field must be a set or sequence and each value of type 'float' and each float in [-340282346600000016151267322115014000640.000000, 340282346600000016151267322115014000640.000000]"
        self._joints = array.array('f', value)
