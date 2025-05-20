import cv2

ig= cv2.imread('picture/saved_sample.png')
ig=cv2.resize(ig,(0,0), fx=0.5,fy=0.5)
cv2.imwrite('picture/saved_sample.png',ig)