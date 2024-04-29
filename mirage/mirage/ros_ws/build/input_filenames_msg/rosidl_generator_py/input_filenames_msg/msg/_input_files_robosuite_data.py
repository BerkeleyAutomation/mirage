# generated from rosidl_generator_py/resource/_idl.py.em
# with input from input_filenames_msg:msg/InputFilesRobosuiteData.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'rgb'
# Member 'depth_map'
# Member 'joints'
import array  # noqa: E402, I100

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_InputFilesRobosuiteData(type):
    """Metaclass of message 'InputFilesRobosuiteData'."""

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
                'input_filenames_msg.msg.InputFilesRobosuiteData')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__input_files_robosuite_data
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__input_files_robosuite_data
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__input_files_robosuite_data
            cls._TYPE_SUPPORT = module.type_support_msg__msg__input_files_robosuite_data
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__input_files_robosuite_data

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


class InputFilesRobosuiteData(metaclass=Metaclass_InputFilesRobosuiteData):
    """Message class 'InputFilesRobosuiteData'."""

    __slots__ = [
        '_rgb',
        '_depth_map',
        '_segmentation',
        '_joints',
    ]

    _fields_and_field_types = {
        'rgb': 'sequence<uint8>',
        'depth_map': 'sequence<double>',
        'segmentation': 'sensor_msgs/Image',
        'joints': 'sequence<double>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('uint8')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['sensor_msgs', 'msg'], 'Image'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.rgb = array.array('B', kwargs.get('rgb', []))
        self.depth_map = array.array('d', kwargs.get('depth_map', []))
        from sensor_msgs.msg import Image
        self.segmentation = kwargs.get('segmentation', Image())
        self.joints = array.array('d', kwargs.get('joints', []))

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
        if self.rgb != other.rgb:
            return False
        if self.depth_map != other.depth_map:
            return False
        if self.segmentation != other.segmentation:
            return False
        if self.joints != other.joints:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def rgb(self):
        """Message field 'rgb'."""
        return self._rgb

    @rgb.setter
    def rgb(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'B', \
                "The 'rgb' array.array() must have the type code of 'B'"
            self._rgb = value
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
                 all(isinstance(v, int) for v in value) and
                 all(val >= 0 and val < 256 for val in value)), \
                "The 'rgb' field must be a set or sequence and each value of type 'int' and each unsigned integer in [0, 255]"
        self._rgb = array.array('B', value)

    @builtins.property
    def depth_map(self):
        """Message field 'depth_map'."""
        return self._depth_map

    @depth_map.setter
    def depth_map(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'depth_map' array.array() must have the type code of 'd'"
            self._depth_map = value
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
                 all(not (val < -1.7976931348623157e+308 or val > 1.7976931348623157e+308) or math.isinf(val) for val in value)), \
                "The 'depth_map' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._depth_map = array.array('d', value)

    @builtins.property
    def segmentation(self):
        """Message field 'segmentation'."""
        return self._segmentation

    @segmentation.setter
    def segmentation(self, value):
        if __debug__:
            from sensor_msgs.msg import Image
            assert \
                isinstance(value, Image), \
                "The 'segmentation' field must be a sub message of type 'Image'"
        self._segmentation = value

    @builtins.property
    def joints(self):
        """Message field 'joints'."""
        return self._joints

    @joints.setter
    def joints(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'joints' array.array() must have the type code of 'd'"
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
                 all(not (val < -1.7976931348623157e+308 or val > 1.7976931348623157e+308) or math.isinf(val) for val in value)), \
                "The 'joints' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._joints = array.array('d', value)
