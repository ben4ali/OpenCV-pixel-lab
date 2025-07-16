import cv2
import random

def glitch_spread_effect(image, step=30, delay=1):
    """Creates a glitch spread effect"""
    height, width, _ = image.shape

    for x in range(0, height, step):
        for y in range(0, width, step):
            color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
            image[x:x+step, y:y+step] = color
            cv2.imshow("Virus Spread", image)
            cv2.waitKey(delay)
