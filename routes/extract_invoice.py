from flask import Blueprint, request, jsonify
from pathlib import Path
from helpers.gemini_utils import gemini_output
from helpers.image_utils import save_temporary_image, delete_image

extract_invoice_bp = Blueprint('extract_invoice', __name__)

@extract_invoice_bp.route('/', methods=['POST'])
def extract_invoice():
    try:
        # Get the uploaded image
        file = request.files.get('file')
        if not file:
            return jsonify({"error": "File is required"}), 400

        # Save the uploaded image temporarily
        image_path = save_temporary_image(file)

        # Process the image through Gemini
        response_text = gemini_output(image_path)

        # Clean up the temporary file
        delete_image(image_path)

        return jsonify({"result": response_text}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500