import numpy as np
from utilis import pil_to_array, array_to_pil 

def gaussian_blur(pil_img, kernel_size=3, sigma=1.0):
    ax = np.arange(-(kernel_size // 2), kernel_size // 2 + 1)
    xx, yy = np.meshgrid(ax, ax)
    kernel = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
    kernel = kernel / np.sum(kernel)

    img_array = pil_to_array(pil_img).astype(float)
    
    pad = kernel_size // 2
    padded = np.pad(img_array, ((pad, pad), (pad, pad)), mode='edge')
    
    h, w = img_array.shape
    output = np.zeros_like(img_array)
    
    for i in range(h):
        for j in range(w):
            window = padded[i:i+kernel_size, j:j+kernel_size]
            output[i, j] = np.sum(window * kernel)
    
    output = np.clip(output, 0, 255)
    return array_to_pil(output)

def median_filter(pil_img, kernel_size=3):
    img_array = pil_to_array(pil_img).astype(float)

    if img_array.ndim == 3:
        img_array = img_array.mean(axis=2)  
    
    pad = kernel_size // 2
    padded = np.pad(img_array, ((pad, pad), (pad, pad)), mode='edge')
    
    h, w = img_array.shape
    output = np.zeros_like(img_array)
    
    for i in range(h):
        for j in range(w):
            window = padded[i:i+kernel_size, j:j+kernel_size]
            output[i, j] = np.median(window)
    
    return array_to_pil(output)
