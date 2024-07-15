import cv2
import numpy as np

def hough_line(s):
    img = cv2.imread(s)
    img = cv2.resize(img,(500,500))
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("original",img)
    cv2.imshow("gray",gray)

    # using canny for detecting edges
    edges = cv2.Canny(gray, 50, 100, None, 3)
    cv2.imshow("edges",edges)

    # applying hough Transform
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 150, None, 0, 0)
    copy_img = img.copy()
    print(np.shape(lines))

    # drawing lines from point obtained in matrix 'lines'
    for i in range(0, len(lines)):
            rho,theta = lines[i][0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv2.line(copy_img, pt1, pt2, (0,0,255), 1, cv2.LINE_AA)
    
    cv2.imshow("Lines detected",copy_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

path = r"C:\Users\piyus\Desktop\pad.jpg"
hough_line(path)