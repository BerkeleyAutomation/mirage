from typing import Any
import numpy as np
import pickle
import socket
import struct
import threading
from xembody.src.general.ros_inpaint_publisher_real import ROSInpaintRealData, ROSInpaintPublisherReal

class ROSProxyInpaintServer:
    """
    Proxy process that sends to another process which performs the ROS communication
    """

    def __init__(self, ip: str = "169.254.91.160", port: int = 31035) -> None:
        """
        Initializes the publisher code.
        """
        super().__init__()
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind((ip, port))
        self._socket.listen(1)
        self.ros_inpaint_publisher_real = ROSInpaintPublisherReal()
    
    def listen_for_connections(self) -> None:
        while True:
            conn, address = self._socket.accept()
            threading.Thread(target=self.handle_inpainting_info, args=(conn,)).start()

    def handle_inpainting_info(self, socket) -> None:
        """
        Handles the inpainting info.
        :param inpainting_info: The inpainting info.
        """
        print("Server is up and running!")
        while True:
            try:
                received_bytes = self._receive_all_bytes(4, socket)
                num_bytes = struct.unpack("!I", received_bytes)[0]
                received_data = self._receive_all_bytes(num_bytes, socket)
                data = pickle.loads(received_data)
                print("Received data from client")

                list_of_ros_inpaint_data = []
                for dict_info in data:
                    ros_inpaint_data = ROSInpaintRealData(
                        rgb=dict_info["rgb"],
                        depth_map=dict_info["depth_map"],
                        joints=dict_info["joints"],
                        camera_name=dict_info["camera_name"]
                    )
                    list_of_ros_inpaint_data.append(ros_inpaint_data)

                self.ros_inpaint_publisher_real.publish_to_ros_node(list_of_ros_inpaint_data)
                print("Sending data to ROS")

                inpainted_img = self.ros_inpaint_publisher_real.get_inpainted_image(blocking=True)
                print("Received inpainted data from ROS, sending back to client")

                serialized_data = pickle.dumps(inpainted_img)
                num_bytes = len(serialized_data)
                byte_count = struct.pack("!I", num_bytes)
                socket.send(byte_count)
                socket.send(serialized_data)
            except:
                return

    def _receive_all_bytes(self, num_bytes: int, socket) -> bytes:
        """
        Receives all the bytes.
        :param num_bytes: The number of bytes.
        :return: The bytes.
        """
        data = bytearray(num_bytes)
        pos = 0
        while pos < num_bytes:
            cr = socket.recv_into(memoryview(data)[pos:])
            if cr == 0:
                raise EOFError()
            pos += cr
        return data

if __name__ == "__main__":
    ros_proxy_inpaint_server = ROSProxyInpaintServer()
    ros_proxy_inpaint_server.listen_for_connections()
