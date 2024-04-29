# generated from rosidl_generator_py/resource/_idl.py.em
# with input from input_filenames_msg:msg/InputFiles.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_InputFiles(type):
    """Metaclass of message 'InputFiles'."""

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
                'input_filenames_msg.msg.InputFiles')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__input_files
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__input_files
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__input_files
            cls._TYPE_SUPPORT = module.type_support_msg__msg__input_files
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__input_files

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class InputFiles(metaclass=Metaclass_InputFiles):
    """Message class 'InputFiles'."""

    __slots__ = [
        '_depth_file',
        '_segmentation',
        '_joints',
    ]

    _fields_and_field_types = {
        'depth_file': 'string',
        'segmentation': 'string',
        'joints': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.depth_file = kwargs.get('depth_file', str())
        self.segmentation = kwargs.get('segmentation', str())
        self.joints = kwargs.get('joints', str())

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
        if self.depth_file != other.depth_file:
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
    def depth_file(self):
        """Message field 'depth_file'."""
        return self._depth_file

    @depth_file.setter
    def depth_file(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'depth_file' field must be of type 'str'"
        self._depth_file = value

    @builtins.property
    def segmentation(self):
        """Message field 'segmentation'."""
        return self._segmentation

    @segmentation.setter
    def segmentation(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'segmentation' field must be of type 'str'"
        self._segmentation = value

    @builtins.property
    def joints(self):
        """Message field 'joints'."""
        return self._joints

    @joints.setter
    def joints(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'joints' field must be of type 'str'"
        self._joints = value
