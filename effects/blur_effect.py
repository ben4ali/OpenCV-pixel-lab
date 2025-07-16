import cv2
import numpy as np

def apply_blur(gray_image):
    h, w = gray_image.shape
    result = np.zeros_like(gray_image)

    # check all pixels (we avoid corners to avoid out of bounds errors)
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            # get a 3x3 kernel and apply average of gray_scale value of each pixel around to the current pixel
            region = gray_image[y - 1:y + 2, x - 1:x + 2]
            result[y, x] = int(region.sum() / 9)
    return result

def blur_image(image):
	gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blank_image = apply_blur(gray_image)
	return blank_image