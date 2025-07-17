import cv2

#pick the treshold ex: any pixel under 127 is set to 0 else 255 (used when image is uniform and clear)
def threshold_global(image_gray, thresh=127, maxval=255, invert=False):
    flag = cv2.THRESH_BINARY_INV if invert else cv2.THRESH_BINARY
    _, binary = cv2.threshold(image_gray, thresh, maxval, flag)
    return binary

#automatic treshold, ideally after applying a blur to reduce noise (used when image is uniform but you don't know the treshold)
def threshold_otsu(image_gray, blur_ksize=(5,5)):
    if blur_ksize is not None:
        image_gray = cv2.GaussianBlur(image_gray, blur_ksize, 0)
    _, binary = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return binary

#used when the lighthing is not uniform
def threshold_adaptive(image_gray, block_size=11, C=2, method='gaussian', invert=False):
    adaptive_method = cv2.ADAPTIVE_THRESH_GAUSSIAN_C if method == 'gaussian' else cv2.ADAPTIVE_THRESH_MEAN_C
    thresh_type = cv2.THRESH_BINARY_INV if invert else cv2.THRESH_BINARY
    binary = cv2.adaptiveThreshold(image_gray, 255, adaptive_method, thresh_type, block_size, C)
    return binary