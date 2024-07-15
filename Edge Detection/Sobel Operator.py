import cv2
import numpy as np
from matplotlib import pyplot as plt

def Sobel(s):
    img = cv2.imread(s)

    #BGR to Grayscale
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 

    # Sobel Filter for Horizontal Edges
    sobelx=cv2.Sobel(gray_img,cv2.CV_64F,1,0, ksize=3)
    # Sobel Filter for Vertical Edges
    sobely=cv2.Sobel(gray_img,cv2.CV_64F,0,1, ksize=3)

    # Combine results to obtain magnitude of gradient
    magnitude = np.sqrt(sobelx**2 + sobely**2)

    # Adjust intensity using cv2.normalize
    magnitude_normalized = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)
    
    plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])

    plt.subplot(122), plt.imshow(magnitude_normalized, cmap='gray')
    plt.title(' Edge-Detected Image'), plt.xticks([]), plt.yticks([])
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()

s= r"live class assignments\photo-1533450718592-29d45635f0a9.jpeg"
Sobel(s)