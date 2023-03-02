import replicate
from settings import REPLICATE_API_TOKEN


def draw_picture(prompt: str,
                 width: int = 512,
                 height: int = 512,
                 num_outputs: int = 1,
                 num_interface_steps: int = 50,
                 guidance_scale: int = 6):
    replicate.Client(api_token=REPLICATE_API_TOKEN)
    model = replicate.models.get("prompthero/openjourney")
    version = model.versions.get("9936c2001faa2194a261c01381f90e65261879985476014a0a37a334593a05eb")

    inputs = {
        'prompt': prompt,
        'width': width,
        'height': height,
        'num_outputs': num_outputs,
        'num_inference_steps': num_interface_steps,
        'guidance_scale': guidance_scale,
    }

    output = version.predict(**inputs)

    return output
