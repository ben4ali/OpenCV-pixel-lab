# main.py

import cv2
from effects.glitch_spread_effect import glitch_spread_effect
from effects.grayscale_converter import convert_grayscale
from effects.blur_effect import blur_image
from effects.gaussian_blur import gaussian_kernel
from effects.gaussian_blur import apply_gaussian_blur
from effects.sobel_filter import apply_sobel_filter
from effects.canny_filter import apply_canny


if __name__ == "__main__":

    image = cv2.imread("images/Knight_cat.jpg")

    if image is not None:
        
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = apply_canny(img_gray)

        cv2.imshow("Processed image", edges)
        cv2.imshow("Original image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        is_already_saved = cv2.imread("outputs/canny.png")
        if is_already_saved is None:
          cv2.imwrite("outputs/canny.png",edges)

