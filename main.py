# main.py

import cv2
from effects.glitch_spread_effect import glitch_spread_effect
from effects.grayscale_converter import convert_grayscale
from effects.blur_effect import blur_image
from effects.gaussian_blur import gaussian_kernel
from effects.gaussian_blur import apply_gaussian_blur
from effects.sobel_filter import apply_sobel_filter
from effects.canny_filter import apply_canny
from effects.tresholding import threshold_adaptive, threshold_global, threshold_otsu


if __name__ == "__main__":

    image = cv2.imread("images/Knight_cat.jpg")

    if image is not None:
        
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # global
        bin_global = threshold_global(img_gray, thresh=127)

        # 2. otsu
        bin_otsu = threshold_otsu(img_gray)

        # 3. adaptive
        bin_adapt = threshold_adaptive(img_gray, block_size=11, C=2, method='gaussian')

        cv2.imshow("Original", image)
        cv2.imshow("Grayscale", img_gray)
        cv2.imshow("Global (127)", bin_global)
        cv2.imshow("Otsu", bin_otsu)
        cv2.imshow("Adaptive Gaussian", bin_adapt)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        is_already_saved = cv2.imread("outputs/adaptive_tresholding.png")
        if is_already_saved is None:
          cv2.imwrite("outputs/canny.png",bin_adapt)

