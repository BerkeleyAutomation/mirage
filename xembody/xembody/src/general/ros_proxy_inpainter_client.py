from typing import Any
import numpy as np
import pickle
import socket
import struct
from xembody.src.general.xembody_publisher import XEmbodyPublisher

class ROSProxyInpainterClient(XEmbodyPublisher):
    """
    Proxy process that sends to another process which performs the ROS communication
    """

    def __init__(self, ip: str = "localhost", port: int = 31025) -> None:
        """
        Initializes the publisher code.
        """
        super().__init__()
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((ip, port))

    def publish_to_ros_node(self, data: Any) -> None:
        """
        Publishes the RGB image, segmentation mask, and joint angles to the ROS2 node.
        :param data: The data to be published in dictionary form.
        """
        serialized_data = pickle.dumps(data)
        num_bytes = len(serialized_data)
        byte_count = struct.pack("!I", num_bytes)
        print(f"Sending {num_bytes} bytes")
        self._socket.send(byte_count)
        self._socket.send(serialized_data)
    
    def _get_inpainted_image_impl(self) -> np.array:
        """
        The implementation of getting an inpainted image.
        :return: The inpainted image.
        """
        received_bytes = self._receive_all_bytes(4)
        num_bytes = struct.unpack("!I", received_bytes)[0]
        received_data = self._receive_all_bytes(num_bytes)
        data = pickle.loads(received_data)
        return data
    
    def _receive_all_bytes(self, num_bytes: int) -> bytes:
        """
        Receives all the bytes.
        :param num_bytes: The number of bytes.
        :return: The bytes.
        """
        data = bytearray(num_bytes)
        pos = 0
        while pos < num_bytes:
            cr = self._socket.recv_into(memoryview(data)[pos:])
            if cr == 0:
                continue
            pos += cr
        return data
    
    def _is_item_available(self) -> bool:
        """
        Whether an item is available.
        :return: Whether an item is available.
        """
        return True