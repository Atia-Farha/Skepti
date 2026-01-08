from PIL import Image
import torch
from torchvision import transforms
import torch.nn as nn
import torchvision.models as models
from torch import Tensor
from torchvision.models import ResNet18_Weights

from .database import store_prediction

# Torch-native preprocessing
preprocess = transforms.Compose([
    transforms.Resize((224, 224)),       # match your model input
    transforms.ToTensor(),               # converts to [0,1]
    transforms.Normalize(                # match model normalization
        mean=[0.485, 0.456, 0.406], 
        std=[0.229, 0.224, 0.225]
    ),
]) 

# Updated label mapping
id2label = {
    "0": "Fake",
    "1": "Real"
}

weights = ResNet18_Weights.DEFAULT
model = models.resnet18(weights=weights)
model.fc = nn.Linear(model.fc.in_features, 2)
model.eval()

def detect_imagefake_torch(filepath):
    image = Image.open(filepath).convert("RGB")
    #input_tensor = preprocess(image).unsqueeze(0)  # add batch dim

    # Preprocess → tensor

    # shape: [C, H, W]
    input_tensor = preprocess(image)           
    # add batch dim → [1, C, H, W]
    input_tensor = input_tensor.unsqueeze(0)  # type: ignore 


    with torch.no_grad():
        logits = model(input_tensor)
        probs = torch.nn.functional.softmax(logits, dim=1).squeeze().tolist()

    prediction = {
        id2label[str(i)]: round(probs[i], 3) for i in range(len(probs))
    }

    real = round(prediction["Real"] * 100, 2)
    fake = round(prediction["Fake"] * 100, 2)

    print(f"Image: {filepath} | Fake: {fake} | Real: {real}")
    store_prediction(filepath, real, fake)

    return [real, fake]


# print(detect_imagefake_torch('/home/pancake/Downloads/dhaka.jpg'))