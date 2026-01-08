from transformers import AutoImageProcessor, SiglipForImageClassification
from PIL import Image
import torch


# Load model and processor
model_name = "prithivMLmods/open-deepfake-detection"  # Updated model name
model = SiglipForImageClassification.from_pretrained(model_name)
processor = AutoImageProcessor.from_pretrained(model_name)

# Updated label mapping
id2label = {
    "0": "Fake",
    "1": "Real"
}

def detect_imagefake(image):
    image = Image.open(image).convert("RGB")
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

    return [real, fake]

