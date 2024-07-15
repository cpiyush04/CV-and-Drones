import cv2
import numpy as np

def ig_filter(s):
    # Step 1: Read the image
    original_image = cv2.imread(s)

    if original_image is None:
        print("Error: Could not read the image.")
        return

    # Step 2: Reduce brightness to 0.5 of its initial value
    brightened_image = cv2.convertScaleAbs(original_image, alpha=0, beta=0.5)

    # Step 3: Increase contrast to 1.5 of its initial value
    high_contrast_image = cv2.convertScaleAbs(brightened_image, alpha=1.5, beta=0)

    # Step 4: Convert image to float32 for saturation adjustment
    high_contrast_float = high_contrast_image.astype(np.float32) / 255.0

    # Increase saturation to 1.5 of its initial value
    hsv = cv2.cvtColor(high_contrast_float, cv2.COLOR_BGR2HSV)
    hsv[:, :, 1] *= 1.5
    hsv[hsv > 255] = 255

    # Convert the image back to uint8
    final_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    cv2.imshow("filt",final_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage:
input_image_path =r"C:\Users\piyus\Desktop\landscape.jpeg"
ig_filter(input_image_path)

