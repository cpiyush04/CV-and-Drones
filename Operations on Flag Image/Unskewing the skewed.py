import cv2
import numpy as np
import matplotlib.pyplot as plt

# variables to store rotated images
rotated_0_deg = None
rotated_90_deg = None
rotated_180_deg = None
rotated_270_deg = None

# Rotation Function taken from code2
def rotate(img, y):
    rows, cols, _ = img.shape
    center = (cols // 2, rows // 2)
    matrix = cv2.getRotationMatrix2D(center, y, 1.0)
    # Apply rotation
    rotated_img = cv2.warpAffine(img, matrix, (cols, rows))
    return rotated_img

# Rotated flag function from code2
def rotatedFlags():
    global rotated_0_deg, rotated_90_deg, rotated_180_deg, rotated_270_deg
    # Load the Indian Flag image generated in code1
    original_image = cv2.imread("generated_code1.png")
    # Storing Rotate images for use later
    rotated_0_deg = rotate(original_image, 0)
    rotated_90_deg = rotate(original_image, 90)
    rotated_180_deg = rotate(original_image, 180)
    rotated_270_deg = rotate(original_image, 270)

# Fucntion for traversing horizontally to pick out the color from image in order to obtain orientaion of image
def horizontal_traversal(image):

    midline_index = image.shape[0] // 2

    for i in range(image.shape[1]):
        pixel_color = image[midline_index,i]
        if np.array_equal(pixel_color, [255,62,62]) and np.array_equal(pixel_color, [0,0,0]):
            continue
        else:
            if np.array_equal(pixel_color, [52, 153, 255]):
                hor_orientation = "90deg"
                break
            elif np.array_equal(pixel_color,[1, 128, 0]):
                hor_orientation = "270deg"
                break    
    return hor_orientation

# Function for traversing vertically to pick out the color from image in order to obtain orientaion of image
def vertical_traversal(image):

    midline_index = image.shape[1] // 2

    for i in range(image.shape[0]):
        pixel_color = image[i, midline_index]
        if np.array_equal(pixel_color, [255,62,62]) and np.array_equal(pixel_color, [0,0,0]):
            continue

        else:
            if np.array_equal(pixel_color,[52, 153, 255]):
                ver_orientation = "0deg"
                break
            elif np.array_equal(pixel_color,[1, 128, 0]):
                ver_orientation = "180deg"
                break
            elif np.array_equal(pixel_color, [255,255,255]):
                ver_orientation = horizontal_traversal(image)
                break
    
    return ver_orientation

# Defining Function for generating unskewed image
def unskew(s):
    
    img = cv2.imread(s)
    img = cv2.resize(img,(600,600))
    # calling the rotatedflag function to obtain refernce images for unskewing.
    rotatedFlags()
    # this saves the refernces in global images and will be used later.
    
    # calling function to know orientation of skewed image, what it looks like
    orientation = vertical_traversal(img)
    print("skewed image orietation resembles " + orientation + " of the reference image")
    if orientation == "0deg":
        cv2.imshow("unskewed",rotated_0_deg)
    elif orientation == "90deg":
        cv2.imshow("unskewed",rotated_90_deg)
    elif orientation == "180deg":
        cv2.imshow("unskewed",rotated_180_deg)
    elif orientation == "270deg":
        cv2.imshow("unskewed",rotated_270_deg)
    cv2.imshow("skewed input",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

s = r"C:\Users\piyus\Desktop\test3.jpg"
unskew(s)
