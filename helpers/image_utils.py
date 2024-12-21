from pathlib import Path

def save_temporary_image(file):
    image_path = f"temp_{file.filename}"
    file.save(image_path)
    return image_path

def delete_image(image_path):
    Path(image_path).unlink(missing_ok=True)