import numpy as np
import cv2
import matplotlib.pyplot as plt

SOBEL_X = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

SOBEL_Y = np.array([
    [-1, -2, -1],
    [0,  0,  0],
    [1,  2,  1]
])
def apply_sobel_filter(image):
	if len(image.shape) != 2:
		raise ValueError("image must be grayscaled")
	
	height, width = image.shape

	matrice_x = np.zeros_like(image, dtype=float)
	matrice_y = np.zeros_like(image, dtype=float)

	for y in range(1, height-1):
		for x in range(1, width-1):

			region = image[y-1:y+2, x-1:x+2]
			val_x = np.sum(region * SOBEL_X)
			val_y = np.sum(region * SOBEL_Y)

			matrice_x[y, x] = val_x
			matrice_y[y, x] = val_y
	
	magnitude = np.sqrt(matrice_x**2 + matrice_y**2)

	# put between 0 & 255
	magnitude = (magnitude / magnitude.max()) * 255
	magnitude = magnitude.astype(np.uint8)

	return magnitude

