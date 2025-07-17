import cv2
import numpy as np

def get_hand_mask(img_bgr):
    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

    lower_skin = np.array([0, 30, 80], dtype=np.uint8)
    upper_skin = np.array([50, 150, 255], dtype=np.uint8)

    mask = cv2.inRange(img_hsv, lower_skin, upper_skin)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    mask = cv2.erode(mask, kernel, iterations=2)
    mask = cv2.dilate(mask, kernel, iterations=2)

    mask = cv2.GaussianBlur(mask, (5,5), 0)

    return mask
