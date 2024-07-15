import cv2
import numpy as np
import matplotlib.pyplot as plt

def colour(s):
    img = cv2.imread(s)
    img = cv2.resize(img,(600,400))
    cv2.imshow("image",img)

    # converting image to rgb
    img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    cv2.imshow("RGB",img_rgb)

    # setting the range of colours to be detected
    lower_bound = np.array([100,0,0], dtype=np.uint8)
    upper_bound = np.array([255,100,100], dtype=np.uint8)

    # using cv2.inRange to generated a binary colour mask
    color_mask = cv2.inRange(img_rgb, lower_bound, upper_bound)
    plt.imshow(color_mask, cmap='gray')
    plt.title('Color Mask for shades of red in original image')

    # list of contours
    contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    image_contours = img.copy()

    # marking contours with black
    cv2.drawContours(image_contours, contours, -1, (0, 0, 0), 3)
    cv2.imshow("detected",image_contours)
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

path = r"C:\Users\piyus\Desktop\images.png"
colour(path)
