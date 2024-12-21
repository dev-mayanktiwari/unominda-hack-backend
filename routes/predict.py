from flask import Blueprint, request, jsonify
from PIL import Image
import io
from helpers.model_utils import predict_image
from models.vgg16_model import model, transform, device

predict_bp = Blueprint('predict', __name__)

@predict_bp.route('/', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        # Load the image
        img = Image.open(io.BytesIO(file.read()))
        
        # Predict image defect
        predicted_class = predict_image(img, model, transform, device)

        return jsonify({'message': 'Prediction successful', 'predicted_class': predicted_class}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500