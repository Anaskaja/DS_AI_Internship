import cv2
import numpy as np
import os

print("Starting Day 59 OpenCV Pipeline...")

# Create an output directory to save our processed images
output_dir = 'outputs'
os.makedirs(output_dir, exist_ok=True)

# 1. Load Image
image = cv2.imread('sample.jpg')
if image is None:
    print("❌ Error: Could not find 'sample.jpg'. Please put an image in this folder!")
    exit()

print("1. Image loaded successfully.")

# 2. Grayscale Conversion
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite(f'{output_dir}/1_grayscale.jpg', gray_image)
print("2. Converted to Grayscale.")

# 3. Resizing
resized_image = cv2.resize(image, (300, 300))
cv2.imwrite(f'{output_dir}/2_resized.jpg', resized_image)
print("3. Resized image to 300x300.")

# 4. Blurring (Gaussian)
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
cv2.imwrite(f'{output_dir}/3_blurred.jpg', blurred_image)
print("4. Applied Gaussian Blur.")

# 5. Edge Detection (Canny)
edges = cv2.Canny(gray_image, 100, 200)
cv2.imwrite(f'{output_dir}/4_edges.jpg', edges)
print("5. Extracted edges using Canny Algorithm.")

# 6. Morphological Operations (Dilation on Edges)
kernel = np.ones((5,5), np.uint8)
dilated = cv2.dilate(edges, kernel, iterations=1)
cv2.imwrite(f'{output_dir}/5_dilated_edges.jpg', dilated)
print("6. Applied Dilation to thicken edges.")

# 7. Image Masking (Circular Focus)
mask = np.zeros(image.shape[:2], dtype="uint8")
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)
cv2.circle(mask, (cX, cY), int(image.shape[0]*0.4), 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imwrite(f'{output_dir}/6_circular_mask.jpg', masked)
print("7. Applied Bitwise Circular Mask.")

print(f"✅ Pipeline Complete! All processed images are saved in the '{output_dir}' folder.")