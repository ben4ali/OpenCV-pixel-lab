import cv2

def reduce_light(B,G,R):
  gray = int(0.114 * B + 0.587 * G + 0.299 * R)
  return [gray, gray, gray]

def convert_grayscale(image):
	height, width, _ = image.shape
	for x in range(width):
		for y in range(height):
			image[y,x] = reduce_light(image[y,x][0],image[y,x][1],image[y,x][2])

	cv2.imshow("Grayscaled image", image)

