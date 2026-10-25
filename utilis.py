import numpy as np
from PIL import Image

def rgb_to_grayscale(pil_img):

    img_array = np.array(pil_img, dtype=float)
    if img_array.ndim == 2:  
        return pil_img.copy()

    R = img_array[:, :, 0]
    G = img_array[:, :, 1]
    B = img_array[:, :, 2]
    
    gray_array = 0.299 * R + 0.587 * G + 0.114 * B
    gray_array = np.clip(gray_array, 0, 255).astype(np.uint8)
    
    return Image.fromarray(gray_array)

def normalize_image(pil_img):
    img_array = np.array(pil_img, dtype=float)
    min_val = img_array.min()
    max_val = img_array.max()
    
    if max_val - min_val == 0:
        norm_array = np.zeros_like(img_array)
    else:
        norm_array = (img_array - min_val) / (max_val - min_val) * 255
    
    return Image.fromarray(norm_array.astype(np.uint8))

def pil_to_array(pil_img):
    return np.array(pil_img)

def array_to_pil(np_array):
    return Image.fromarray(np_array.astype(np.uint8))
