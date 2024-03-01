# import sys
# sys.path.insert(0, "/home/r2d2/R2D2/diffusers")
# https://github.com/huggingface/diffusers/tree/main/examples/controlnet
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel, UniPCMultistepScheduler, StableDiffusionControlNetImg2ImgPipeline
from diffusers.utils import load_image
import torch
from torchvision import transforms
from PIL import Image
import socket
import threading
import struct
import pickle

class DiffusionModel:
    def __init__(self, controlnet_path):
        # base_model_path = "stabilityai/stable-diffusion-2-1"
        base_model_path = "runwayml/stable-diffusion-v1-5"
        self.controlnet = ControlNetModel.from_pretrained(controlnet_path, torch_dtype=torch.float16)
        self.pipe = StableDiffusionControlNetPipeline.from_pretrained(
            base_model_path, controlnet=self.controlnet, torch_dtype=torch.float16, use_safetensors=True
        )       

        self.pipe.scheduler = UniPCMultistepScheduler.from_config(self.pipe.scheduler.config)
        self.pipe.safety_checker = None
        self.pipe.requires_safety_checker = False
        self.pipe.enable_model_cpu_offload()
        # self.pipe.enable_sequential_cpu_offload()

    def forward(self, prompt, control_image):
        # assume control_image is a PIL image
        
        # prompt = "create a high quality image with a Franka Panda robot, a green table with a stuffed animal tiger and black bowl, and a portrait painting in the background"
        # prompt = ""

        control_image = control_image.resize((256, 256))

        # generate image
        generator = torch.manual_seed(1)
        image = self.pipe(prompt, 
                          control_image_masked=20, 
                          generator=generator, 
                          image=control_image, 
                          control_image=control_image).images[0]
        return image
    
class DiffusionServer:
    def __init__(self, diffusion_model, port, ip="localhost"):
        self.diffusion_model = diffusion_model
        self.port = port
        # Create a socket object
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to a specific address and port
        self.server_socket.bind((ip, self.port))

        # Listen for incoming connections
        self.server_socket.listen(1)
        self.listening_thread = threading.Thread(target=self.start, daemon=True)
        self.listening_thread.start()
        self.client_socket = None
        self.server_notifier = threading.Condition()

    def receive_all_bytes(self, num_bytes: int):
        """
        Receives all the bytes.
        """
        data = bytearray(num_bytes)
        pos = 0
        while pos < num_bytes:
            cr = self.client_socket.recv_into(memoryview(data)[pos:])
            if cr == 0:
                raise EOFError("Socket closed")
            pos += cr
        return data

    def start(self):
        while True:
            # Accept a client connection
            client_socket, client_address = self.server_socket.accept()
            print(f"Accepted connection from {client_address}")
            self.client_socket = client_socket
            with self.server_notifier:
                self.server_notifier.notify()

    def serve_diffusion_model(self):
        while True:
            with self.server_notifier:
                self.server_notifier.wait_for(lambda: self.client_socket is not None)

            try:
                # Receive data from the client
                received_bytes = self.receive_all_bytes(4)
                num_bytes = struct.unpack("!I", received_bytes)[0]
                received_data = self.receive_all_bytes(num_bytes)
                data = pickle.loads(received_data)
                prompt = data["prompt"]
                control_image = data["control_image"]
                image = self.diffusion_model.forward(prompt, control_image)
                # Send data to the client
                serialized_data = pickle.dumps(image)
                num_bytes = len(serialized_data)
                byte_count = struct.pack("!I", num_bytes)
                print(f"Sending {num_bytes} bytes")
                self.client_socket.send(byte_count)
                self.client_socket.send(serialized_data)
            except EOFError:
                print("Client disconnected")
                self.client_socket = None

if __name__ == '__main__':
    # all tasks black background
    # controlnet_path = "/home/lawrence/xembody/diffusion/checkpoint-2000/controlnet"
    # tiger green background
    controlnet_path = "/home/lawrence/xembody/diffusion/checkpoint-3000/controlnet"
    # cup green background
    # controlnet_path = "/home/lawrence/xembody/diffusion/checkpoint-2300/controlnet"
    diffusion_model = DiffusionModel(controlnet_path)
    
    # ATHENA_2_IP = '169.254.91.160'
    ATHENA_2_IP = 'localhost'

    diffusion_server = DiffusionServer(diffusion_model, 32003, ATHENA_2_IP)
    diffusion_server.serve_diffusion_model()