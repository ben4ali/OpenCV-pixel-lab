import cv2

def apply_canny(image):
	if len(image.shape)>2:
		raise ValueError("image must be grayscaled")
	blur = cv2.GaussianBlur(image, (5, 5), 1.0)

	low_thresh = 50
	high_thresh = 150

	edges = cv2.Canny(blur, low_thresh, high_thresh)

	return edges