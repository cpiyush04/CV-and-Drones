import cv2
import numpy as np

def shape(s):
    img = cv2.imread(s)
    img = cv2.resize(img,(720,720))
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_img,50,100)
    cv2.imshow("image",img)
    cv2.imshow("gray",gray_img)
    cv2.imshow("edge",edges)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    img_cop = img.copy()

    for contour in contours:
        app = cv2.approxPolyDP(contour,0.01 * cv2.arcLength(contour, True), True )
        vertices = len(app)

        if vertices == 3:
            label = "Triangle"
        elif vertices == 4:
            x, y, w, h = cv2.boundingRect(app)
            ratio = float(w) / h

            if 0.95 <=ratio <= 1.05:
                label = "Square"
            else:
                label = "Rectangle"
        elif vertices == 5:
            label = "Pentagon"
        elif vertices == 6:
            label = "Hexagon"
        elif vertices == 8:
            label = "Octagon"
        elif vertices == 9:
            label = "Nonagon"
        else:
            label = "Circle"
        
        cv2.drawContours(img_cop, [app], 0, (0, 255,255), 4)
        cv2.putText(img_cop, label, tuple(app[1][0]), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,0), 2)

    cv2.imshow("identified",img_cop)
    sorted_contours = sorted(contours,key = cv2.contourArea,reverse=True)
    large_2 = sorted_contours[0:2]
    for contour in large_2:
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.circle(img_cop, (cX, cY), 10, (0, 0, 0), -1)
    cv2.imshow("marked",img_cop)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

path = r"C:\Users\piyus\Downloads\Untitled design (3).png"
shape(path)