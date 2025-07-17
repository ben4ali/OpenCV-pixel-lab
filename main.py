import cv2
from effects.hand_mask import get_hand_mask

if __name__ == "__main__":
    img = cv2.imread("images/hand.png")
    if img is None:
        raise FileNotFoundError("image not found")

    mask = get_hand_mask(img)

    cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Original", 600, 400)
    cv2.imshow("Original", img)

    cv2.namedWindow("Hand Mask", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Hand Mask", 600, 400)
    cv2.imshow("Hand Mask", mask)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
