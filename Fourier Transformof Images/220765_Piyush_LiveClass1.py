import cv2
import numpy as np
from matplotlib import pyplot as plt

def solve(s):

#image path is given in the form a string s
    img = cv2.imread(s)
    cv2.imshow('image',img)

#for finding fourier transform
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('image',img)

    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    img2= 20*np.log(np.abs(fshift))
    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])

    plt.subplot(122), plt.imshow(img2, cmap='gray')
    plt.title('Fourier Transform'), plt.xticks([]), plt.yticks([])

    plt.show()

solve(r"live class assignments\photo-1533450718592-29d45635f0a9.jpeg")
