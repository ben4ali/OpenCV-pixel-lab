# main.py

import cv2
from effects.glitch_spread_effect import glitch_spread_effect
from effects.grayscale_converter import convert_grayscale
from effects.blur_effect import blur_image
from effects.gaussian_blur import gaussian_kernel
from effects.gaussian_blur import apply_gaussian_blur
from effects.sobel_filter import apply_sobel_filter


if __name__ == "__main__":

    image = cv2.imread("images/Knight_cat.jpg")

    if image is not None:
        # glitch_spread_effect(image, step=30, delay=1)
        # convert_grayscale(image)
        # processed_image = blur_image(image,15)
        
        image = cv2.imread("images/Knight_cat.jpg")
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sobel_image = apply_sobel_filter(gray_image)
        # kernel = gaussian_kernel(kernel_size=65, sigma=1.0)
        # blurred = apply_gaussian_blur(gray_image, kernel)

        cv2.imshow("Processed sobel", sobel_image)
        cv2.imshow("Origina grayscale", gray_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        is_already_saved = cv2.imread("outputs/sobeled.png")
        if is_already_saved is None:
          cv2.imwrite("outputs/sobeled.png",sobel_image)

