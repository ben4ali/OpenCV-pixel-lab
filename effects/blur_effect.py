import cv2
import numpy as np

def apply_blur(gray_image, kernel_size=3):
	if kernel_size % 2 == 0:
		print(kernel_size)
		raise ValueError("must be odd")
	
	h, w = gray_image.shape
	result = np.zeros_like(gray_image)
	radius = kernel_size // 2

	for y in range(radius, h - radius):
		for x in range(radius, w - radius):
			region = gray_image[y - radius:y + radius + 1, x - radius:x + radius + 1]
			result[y, x] = int(region.sum() / (kernel_size * kernel_size))

	return result
		

def blur_image(image,kernel_size):
	gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blank_image = apply_blur(gray_image,kernel_size)
	return blank_image