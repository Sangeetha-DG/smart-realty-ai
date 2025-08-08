from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

# Load processor and model from HuggingFace (not GitHub)
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image_path):
    image = Image.open(image_path).convert('RGB')
    inputs = processor(image, return_tensors="pt")
    
    with torch.no_grad():
        output = model.generate(**inputs)
    
    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption
