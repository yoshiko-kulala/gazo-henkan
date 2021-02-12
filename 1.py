import cv2
import numpy as np

img = cv2.imread("girl.JPG")

#while True:
cv2.imshow("test",img)
cv2.waitKey(1)
    
for numx in range(48):
    for numy in range(48):
        pixelValue = img[numx, numy]
        outo=int(pixelValue[0]/8)+int(pixelValue[1]/4)*32+int(pixelValue[2]/8)*2048
        print (hex(outo) + ',', end='')
    print("")