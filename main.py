import cv2
from effects.hand_mask import get_hand_mask

if __name__ == "__main__":
    img = cv2.imread("images/hand.png")
    if img is None:
        raise FileNotFoundError("image not found")

    mask = get_hand_mask(img)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        print(f"Bounding box: x={x}, y={y}, w={w}, h={h}")
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    else:
        print("No contours found")
    cv2.drawContours(img, contours, -1, (255, 255, 0), 3)
    cv2.namedWindow("Original with Bounding Box", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Original with Bounding Box", 600, 400)
    cv2.imshow("Original with Bounding Box", img)

    cv2.namedWindow("Hand Mask", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Hand Mask", 600, 400)
    cv2.imshow("Hand Mask", mask)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
