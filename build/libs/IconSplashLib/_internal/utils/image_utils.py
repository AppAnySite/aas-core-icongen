import os
from PIL import Image
import hashlib

def verify_image_exists(image_path):
    return os.path.isfile(image_path)

def verify_image_size(image_path, size):
    with Image.open(image_path) as img:
        return img.size == size

def compute_file_hash(filepath):
    with open(filepath, 'rb') as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)
    return file_hash.hexdigest()
