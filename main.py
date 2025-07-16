# main.py

import cv2
from effects.glitch_spread_effect import glitch_spread_effect
from effects.grayscale_converter import convert_grayscale

if __name__ == "__main__":

    image = cv2.imread("images/Knight_cat.jpg")

    if image is not None:
        # glitch_spread_effect(image, step=30, delay=1)
        convert_grayscale(image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # is_already_saved = cv2.imread("outputs/grayscaled.png")
        # if is_already_saved is None:
        #   cv2.imwrite("outputs/grayscaled.png",image)

