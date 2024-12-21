import torch
from torchvision import models
import torch.nn as nn
from torchvision import transforms

device = "cuda" if torch.cuda.is_available() else "cpu"

model = models.vgg16(pretrained=False)
model.classifier = nn.Sequential(
    nn.Linear(25088, 4096),
    nn.ReLU(),
    nn.Dropout(p=0.5),
    nn.Linear(4096, 512),
    nn.ReLU(),
    nn.Dropout(p=0.5),
    nn.Linear(512, 8),
)

model.load_state_dict(torch.load("vgg16_benchmark10.pth", map_location=device))
model = model.to(device)
model.eval()

transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
])