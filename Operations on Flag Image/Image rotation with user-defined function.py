import cv2
import numpy as np
import matplotlib.pyplot as plt

# Global variables to store rotated images
rotated_0_deg = None
rotated_90_deg = None
rotated_180_deg = None
rotated_270_deg = None

# function for arbitary rotation
def rotate(img, y):

    # Get image shape and center
    rows, cols, _ = img.shape
    center = (cols // 2, rows // 2)

    # Rotation matrix
    matrix = cv2.getRotationMatrix2D(center, y, 1.0)

    # Apply rotation
    rotated_img = cv2.warpAffine(img, matrix, (cols, rows))
    return rotated_img

def rotatedFlags():
    global rotated_0_deg, rotated_90_deg, rotated_180_deg, rotated_270_deg

    # Load the Indian Flag image generated in code1
    original_image = cv2.imread('generated_code1.png')

    # Rotate the image at 0,90,180 and 270 deg
    rotated_0_deg = rotate(original_image, 0)
    rotated_90_deg = rotate(original_image, 90)
    rotated_180_deg = rotate(original_image, 180)
    rotated_270_deg = rotate(original_image, 270)

    # Displaying the rotated images as needed
    cv2.imshow('Rotated 0 degrees', rotated_0_deg)
    cv2.imshow('Rotated 90 degrees', rotated_90_deg)
    cv2.imshow('Rotated 180 degrees', rotated_180_deg)
    cv2.imshow('Rotated 270 degrees', rotated_270_deg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# function call for displaying the rotated images of the indian flag image saved in code1.
rotatedFlags()

