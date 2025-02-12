import torch
from diffusers import StableDiffusionPipeline

def load_model():
    model_id = "CompVis/stable-diffusion-v1-4"
    pipe = StableDiffusionPipeline.from_pretrained(model_id)
    pipe.to("cuda" if torch.cuda.is_available() else "cpu")
    return pipe

def generate_image(pipe, prompt):
    image = pipe(prompt).images[0]
    return image
