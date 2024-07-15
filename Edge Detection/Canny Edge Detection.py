import cv2
from matplotlib import pyplot as plt

def solve(s):

    img = cv2.imread(s)
    img = cv2.resize(img,(500,500))
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # canny edge detection
    edges = cv2.Canny(gray,100,200)

    # displaying output
    plt.subplot(121),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Canny Edge detected'), plt.xticks([]), plt.yticks([])
    plt.show()

# function call
s = "photo-1533450718592-29d45635f0a9.jpeg"
solve(s)