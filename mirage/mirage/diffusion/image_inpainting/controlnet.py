# https://github.com/huggingface/diffusers/tree/main/examples/controlnet
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel, UniPCMultistepScheduler
from diffusers.utils import load_image
import torch
from torchvision import transforms
from PIL import Image
import numpy as np
# base_model_path = "stabilityai/stable-diffusion-2-1"
base_model_path = "runwayml/stable-diffusion-v1-5"
controlnet_path = "/home/lawrence/xembody/diffusers/outputs/ur5_franka_256_nonorm_largedata/checkpoint-1450/controlnet"

class ControlNet(ControlNetModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        controlnet = ControlNetModel.from_pretrained(controlnet_path, torch_dtype=torch.float16)
        self.pipe = StableDiffusionControlNetPipeline.from_pretrained(
            base_model_path, controlnet=controlnet, torch_dtype=torch.float16
        )
        self.pipe.scheduler = UniPCMultistepScheduler.from_config(self.pipe.scheduler.config)
        self.pipe.safety_checker = None
        self.pipe.requires_safety_checker = False

        self.pipe.enable_model_cpu_offload()
        # self.pipe.enable_sequential_cpu_offload()

        # control_image = load_image("/home/lawrence/diffusers/data/success_trajs_withpose_512/ur5e_rgb/0/34.jpg")
        # control_image = load_image("/home/lawrence/diffusers/data/success_trajs_withpose_512/franka_rgb/496/25.jpg")
        self.prompt = "replace the UR5 robot and its gripper with a Franka Panda robot and gripper at the exact same position and orientation"
        self.prompt = "create a high quality image with a Franka Panda robot, a table, and a red cube on the table"

        self.image_transforms = transforms.Compose(
                [
                    transforms.Resize(256, interpolation=transforms.InterpolationMode.BILINEAR),
                    transforms.CenterCrop(256),
                    transforms.ToTensor(),
                    # transforms.Normalize([0.5], [0.5]),
                ]
            )
        # generate image
        self.generator = torch.manual_seed(1)

    def inpaint(self, control_image):

        # image = self.image_transforms(control_image)
        # control_image = control_image.resize((256, 256))
        # control_image = np.array(control_image) / 255.0
        control_image = control_image[None, ...]

        image = self.pipe(self.prompt, num_inference_steps=20, generator=self.generator, image=control_image).images[0]
        image = (image).clamp(0, 1).squeeze()
        image = (image.permute(1, 2, 0) * 255).round().to(torch.uint8).cpu().numpy()
        image_84 = Image.fromarray(image).resize((84, 84))
        image = np.array(image).astype(np.float32) / 255.0
        image_84 = np.array(image_84).astype(np.float32) / 255.0
        # image = Image.fromarray(image)
        return image, image_84