import cv2
# ImageEnhance from PIL library will make this filter work easily
import numpy as np

def ig_filter(s):

    img = cv2.imread(s)
    img = cv2.resize(img,(720,720))

    brightness_factor = 0.5
    contrast_factor = 1.5

    # Decrease brightness
    darkened_image = cv2.multiply(img, np.array([brightness_factor]))

    # Increase contrast
    c_b_alt = cv2.addWeighted(darkened_image, contrast_factor, np.zeros_like(img), 0, 0)


    # converting image BGR to HSV 
    hsv_img = cv2.cvtColor(c_b_alt,cv2.COLOR_BGR2HSV)
    # splitting colour channels
    h,s,v = cv2.split(hsv_img)
    # altering the Saturation channel
    s_alterted = np.clip(s * 1.5, 0, 255).astype(np.uint8)
    # merging back the h,s,v channels
    adjusted_image = cv2.merge([h, s_alterted, v])
    # final edited image
    edited = cv2.cvtColor(adjusted_image,cv2.COLOR_HSV2BGR)

    cv2.imshow("image",img)
    #cv2.imshow("c_b_alt",c_b_alt)
    #cv2.imshow("hsv_img",hsv_img)
    #cv2.imshow("h",h)
    #cv2.imshow("s",s)
    #cv2.imshow("v",v)
    #cv2.imshow("s_alt",s_altered)
    #cv2.imshow("adjusted",adjusted_image)
    cv2.imshow("edited",edited)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

img_path = r"C:\Users\piyus\Desktop\landscape.jpeg"
ig_filter(img_path)