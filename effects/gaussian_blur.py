import numpy as np

def apply_gaussian_blur(gray_image, kernel):
    if len(gray_image.shape) != 2:
        raise ValueError("image must be grayscaled")

    h, w = gray_image.shape
    k = kernel.shape[0]
    radius = k // 2

    result = np.zeros((h, w), dtype=np.float32)

    for y in range(radius, h - radius):
        for x in range(radius, w - radius):
            region = gray_image[y - radius:y + radius + 1,
                                x - radius:x + radius + 1]
            value = (region * kernel).sum()
            result[y, x] = value


    result = np.clip(result, 0, 255).astype(np.uint8)
    return result

def gaussian_kernel(kernel_size=3, sigma=1.0):

    if kernel_size % 2 == 0:
        raise ValueError("kernel_size must be odd")

    radius = kernel_size // 2
    ax = np.arange(-radius, radius + 1)
    xx, yy = np.meshgrid(ax, ax)

    exponent = -(xx**2 + yy**2) / (2 * sigma**2)
    kernel = np.exp(exponent)

    kernel /= kernel.sum()
    return kernel.astype(np.float32)
