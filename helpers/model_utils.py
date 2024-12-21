import torch.nn.functional as F
import torch

def predict_image(image, model, transform, device, threshold=0.7):
    print("Inside print image")
    if image.mode != 'RGB':
        image = image.convert('RGB')

    image = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(image)
        probabilities = F.softmax(output, dim=1)

        predicted_class_idx = torch.argmax(probabilities, dim=1).item()
        predicted_probability = probabilities[0, predicted_class_idx].item()

        if predicted_probability < threshold:
            return "Perfect"
        else:
            defect_classes = ['crescent_gap', 'inclusion', 'inclusion', 'punching_hole', 
                              'silk_spot', 'waist_folding', 'water_spot', 'welding_line']
            return f"Defected: {defect_classes[predicted_class_idx]}"