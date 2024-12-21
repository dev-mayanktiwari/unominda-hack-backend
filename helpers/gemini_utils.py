from pathlib import Path
import json
import os
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_CONFIG = {
    "temperature": 0.2,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096,
}
SAFETY_SETTINGS = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

# model = genai.(
#     model_name="gemini-1.5-flash",
#     generation_config=MODEL_CONFIG,
#     safety_settings=SAFETY_SETTINGS,
# )

model = genai.GenerativeModel("gemini-1.5-flash", generation_config=MODEL_CONFIG, safety_settings=SAFETY_SETTINGS)

def gemini_output(image_path):
    system_prompt = """
        You are a specialist in comprehending receipts.
        Input images in the form of receipts will be provided to you,
        and your task is to respond to questions based on the content of the input image.
    """
    user_prompt = "Convert Invoice data into JSON format with appropriate JSON tags as required for the data in the image."

    img = Path(image_path)
    if not img.exists():
        raise FileNotFoundError(f"Could not find image: {img}")
    image_info = [{"mime_type": "image/png", "data": img.read_bytes()}]

    input_prompt = [system_prompt, image_info[0], user_prompt]
    response = model.generate_content(input_prompt)

    try:
        return json.loads(response.text.strip().replace("```json", "").replace("```", "").strip())
    except json.JSONDecodeError:
        return {"error": "Failed to parse JSON from the response"}