from transformers import AutoImageProcessor, SiglipForImageClassification
from PIL import Image
import torch

from .database import store_prediction

# Load model and processor
model_name = "prithivMLmods/open-deepfake-detection"  # Updated model name
model = SiglipForImageClassification.from_pretrained(model_name)
processor = AutoImageProcessor.from_pretrained(model_name)

# Updated label mapping
id2label = {
    "0": "Fake",
    "1": "Real"
}

def detect_imagefake(filepath):
    image = Image.open(filepath).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probs = torch.nn.functional.softmax(logits, dim=1).squeeze().tolist()

    prediction = {
        id2label[str(i)]: round(probs[i], 3) for i in range(len(probs))
    }

    real = round(prediction["Real"] * 100, 2)
    fake = round(prediction["Fake"] * 100, 2)

    print(f"Image: {filepath} | Fake: {fake} | Real: {real}")
    store_prediction(filepath, real, fake)

    return [real, fake]

# detect_imagefake('/home/pancake/Downloads/gemini_dhaka_night.png')