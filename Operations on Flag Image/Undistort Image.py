import cv2
import numpy as np
from matplotlib import pyplot as plt

def undistort(s):

    img = cv2.imread(s)
    mtx = np.array(((560.26831365, 0., 651.26205498),( 0., 561.31870941 ,499.05498086),(0,0,1)))
    dist = np.array(( -2.32876385e-01  ,6.16788766e-02, -1.40234765e-05,  3.81911252e-05,-7.54075162e-03))

    dst = cv2.undistort(img, mtx, dist, None, mtx)
    plt.figure(figsize=(8,4))

    # Plotting original image 1
    plt.subplot(1, 2, 1), plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    plt.title('original'), plt.xticks([]), plt.yticks([])

    # Plotting Fourier transform image 1
    plt.subplot(1, 2, 2), plt.imshow(cv2.cvtColor(dst,cv2.COLOR_BGR2RGB))
    plt.title('undistorted'), plt.xticks([]), plt.yticks([])
    plt.show()

undistorted_image = undistort(r"C:\Users\piyus\Desktop\caliber\camera-calibration-opencv\calibration_wide\GOPR0059.jpg")