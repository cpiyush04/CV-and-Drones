import cv2
import numpy as np
from matplotlib import pyplot as plt

def hybrid_images(s1, s2):

    # Read images
    img1 = cv2.imread(s1)
    img2 = cv2.imread(s2)

    # Resizing images
    img1 = cv2.resize(img1, (256, 256), interpolation=cv2.INTER_AREA)
    img2 = cv2.resize(img2, (256, 256), interpolation=cv2.INTER_AREA)

    # Converting to Grayscale
    gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # defining filters using center of the images
    center = (256 // 2, 256 // 2)

    # low pass filter
    lpf = np.zeros_like(gray_img1)
    lpf[center[0]-30:center[0]+30, center[1]-30:center[1]+30] = 1

    # high pass filter
    hpf= np.ones_like(gray_img1)
    hpf[center[0]-30:center[0]+30, center[1]-30:center[1]+30] = 0

    # Fourier Transform for Image 1
    ftransform1 = np.fft.fft2(gray_img1)
    fshift1 = np.fft.fftshift(ftransform1)
    FT1 = 20*np.log(1+np.abs(fshift1))

    # Fourier transform for Image 2
    ftransform2 = np.fft.fft2(gray_img2)
    fshift2 = np.fft.fftshift(ftransform2)
    FT2 = 20*np.log(1+np.abs(fshift2))

    # Applying filters
    ftransform_filtered1 = fshift1 * lpf
    FTfiltered1 = 20*np.log(1+np.abs(ftransform_filtered1))

    ftransform_filtered2 = fshift2 * hpf
    FTfiltered2 = 20*np.log(1+np.abs(ftransform_filtered2))

    # calculating Inverse of filtered transforms to obtain filtered images
    filtered_img1 = np.fft.ifft2(np.fft.ifftshift(ftransform_filtered1)).real
    filtered_img2 = np.fft.ifft2(np.fft.ifftshift(ftransform_filtered2)).real

    # Average the filtered images
    average_image = cv2.add(filtered_img1,filtered_img2) / 2

    # Plot for results
    plt.figure(figsize=(15,15))

    # Plotting original image 1
    plt.subplot(3, 5, 1), plt.imshow(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
    plt.title('Image 1'), plt.xticks([]), plt.yticks([])

    # Plotting Fourier transform image 1
    plt.subplot(3, 5, 2), plt.imshow(FT1,cmap='gray')
    plt.title('FT Image 1'), plt.xticks([]), plt.yticks([])

    # displaying filter used
    plt.subplot(3, 5, 3), plt.imshow(lpf, cmap='gray')
    plt.title('Filetr = LPF'), plt.xticks([]), plt.yticks([])

    # Plotting filtered image 1
    plt.subplot(3, 5, 4), plt.imshow(filtered_img1, cmap='gray')
    plt.title('LPF image1'), plt.xticks([]), plt.yticks([])

    # Plotting Fourier transform image 1 after filter
    plt.subplot(3, 5, 5), plt.imshow(FTfiltered1, cmap='gray')
    plt.title('FT after LPF'), plt.xticks([]), plt.yticks([])

    # Plotting original image 2
    plt.subplot(3, 5, 6), plt.imshow(cv2.cvtColor(img2,cv2.COLOR_BGR2RGB))
    plt.title('Image 2'), plt.xticks([]), plt.yticks([])

    # Plotting Fourier transform image 1
    plt.subplot(3, 5, 7), plt.imshow(FT2, cmap='gray')
    plt.title('FT Image 2'), plt.xticks([]), plt.yticks([])
    
    # displaying filter used
    plt.subplot(3, 5, 8), plt.imshow(hpf, cmap='gray')
    plt.title(' Filter = HPF'), plt.xticks([]), plt.yticks([])

     # Plotting filtered image 1
    plt.subplot(3, 5, 9), plt.imshow(filtered_img2, cmap='gray')
    plt.title('HPF image2'), plt.xticks([]), plt.yticks([])

    # Plotting Fourier transform image 1 after filter
    plt.subplot(3, 5, 10), plt.imshow(FTfiltered2, cmap='gray')
    plt.title('Fourier after HPF'), plt.xticks([]), plt.yticks([])

    # Plotting hybrid image
    plt.subplot(3, 5, 13), plt.imshow(average_image, cmap='gray')
    plt.title('Hybrid Image'), plt.xticks([]), plt.yticks([])
    plt.show()

# Function call for two images
s1 = "face-facial-hair-fine-looking-guy-614810-2048x1749.jpg"
s2 = "OIP (2).jpeg"
hybrid_images(s1,s2)
