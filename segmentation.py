import numpy as np
from PIL import Image

def simple_segmentation(pil_img):
    img_gray = pil_img.convert("L")
    img_array = np.array(img_gray, dtype=np.uint8)

    hist, _ = np.histogram(img_array, bins=256, range=(0, 256))
    total_pixels = img_array.size
    
    sum_total = np.dot(np.arange(256), hist)
    
    current_max_variance = -1
    threshold = 0
    
    sum_background = 0
    weight_background = 0

    for t in range(256):
        
        weight_background += hist[t] 
        if weight_background == 0:
            continue
            
        weight_foreground = total_pixels - weight_background
        if weight_foreground == 0:
            break 
            
        sum_background += t * hist[t]
        mean_background = sum_background / weight_background
        mean_foreground = (sum_total - sum_background) / weight_foreground
        var_between = weight_background * weight_foreground * (mean_background - mean_foreground)**2
        
        if var_between > current_max_variance:
            current_max_variance = var_between
            threshold = t
            
    binary_array = np.where(img_array > threshold, 255, 0).astype(np.uint8)
    
    return Image.fromarray(binary_array)