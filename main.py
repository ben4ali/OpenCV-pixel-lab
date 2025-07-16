# main.py

import cv2
from effects.glitch_spread_effect import glitch_spread_effect
from effects.grayscale_converter import convert_grayscale
from effects.blur_effect import blur_image
if __name__ == "__main__":

    image = cv2.imread("images/Knight_cat.jpg")

    if image is not None:
        # glitch_spread_effect(image, step=30, delay=1)
        # convert_grayscale(image)
        processed_image = blur_image(image,25)
        
        cv2.imshow("Processed image", processed_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        is_already_saved = cv2.imread("outputs/blurred.png")
        if is_already_saved is None:
          cv2.imwrite("outputs/blurred.png",image)

