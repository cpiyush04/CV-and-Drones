import cv2
import numpy as np

# Read the image
image_path = r"C:\Users\piyus\Desktop\lion.jpg"
img = cv2.imread(image_path)
img = cv2.resize(img,(500,500))

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding or edge detection
# Choose one of the following methods:

# Method 1: Thresholding
_, thresholded = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Method 2: Edge Detection (using Canny)
edges = cv2.Canny(gray, 50, 150)

# Find contours in the thresholded or edge-detected image
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Choose the index of the contour you want to output
chosen_contour_index = 220  # Change this index as needed

# Create an empty image to draw the chosen contour
output_img = np.zeros_like(img)

# Draw the chosen contour on the empty image
cv2.drawContours(output_img, contours, 221, (0, 255, 0), 2)

# Display the original image and the image with the chosen contour
cv2.imshow('Original Image', img)
cv2.imshow('Chosen Contour', output_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
