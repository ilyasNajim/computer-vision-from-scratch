import numpy as np
from PIL import Image

def detect_contours(pil_img):
    img_gray = pil_img.convert("L")
    img_array = np.array(img_gray, dtype=float)
    kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    kernel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    gx = convolution_3x3(img_array, kernel_x)
    gy = convolution_3x3(img_array, kernel_y)
    
    magnitude = np.sqrt(gx**2 + gy**2)
    angle = np.arctan2(gy, gx) * 180 / np.pi
    angle[angle < 0] += 180  
    
    h, w = magnitude.shape
    nms_output = np.zeros((h, w), dtype=float)
    
    for i in range(1, h-1):
        for j in range(1, w-1):
            v1, v2 = 255, 255
            curr_angle = angle[i, j]

            if (0 <= curr_angle < 22.5) or (157.5 <= curr_angle <= 180): 
                v1, v2 = magnitude[i, j+1], magnitude[i, j-1]
            elif (22.5 <= curr_angle < 67.5): 
                v1, v2 = magnitude[i+1, j-1], magnitude[i-1, j+1]
            elif (67.5 <= curr_angle < 112.5): 
                v1, v2 = magnitude[i+1, j], magnitude[i-1, j]
            elif (112.5 <= curr_angle < 157.5): 
                v1, v2 = magnitude[i-1, j-1], magnitude[i+1, j+1]

            if magnitude[i, j] >= v1 and magnitude[i, j] >= v2:
                nms_output[i, j] = magnitude[i, j]
            else:
                nms_output[i, j] = 0
                
    max_val = nms_output.max()
    if max_val > 0:
        nms_output = (nms_output / max_val) * 255
    
    return Image.fromarray(nms_output.astype(np.uint8))

def convolution_3x3(image, kernel):

    img_h, img_w = image.shape
    output = np.zeros((img_h, img_w), dtype=float)
    
    padded = np.pad(image, ((1,1),(1,1)), mode='constant')
    
    for i in range(img_h):
        for j in range(img_w):
            window = padded[i:i+3, j:j+3]
            output[i, j] = np.sum(window * kernel)
            
    return output