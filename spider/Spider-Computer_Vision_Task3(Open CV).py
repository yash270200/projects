import numpy as np
import cv2

#input image
inputImg = cv2.imread('C:/Users/YASH PATEL/Desktop/With football.jpg',-1)

#Creating an array of 3 columns corresponding to R,G,B values of all the pixels
samples = inputImg.reshape((-1,3))

#Changing because cv2.kmeasn take only float32 values
samples = np.float32(samples)

#Setting k(Number of cluster in final result)
k_parameter = 2

#Setting k-means iterating termination criteria
criteria = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,10,1.0)

#kmeans clustering
ret,labels,center = cv2.kmeans(samples,k_parameter,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

#Changing center back to uint8, and reshaping to original image
center = np.uint8(center)
outputImg = center[labels.flatten()].reshape((inputImg.shape))

#Showing final output image
cv2.imshow('Result',outputImg)

#Closing all windows at any key press
cv2.waitKey(0)
cv2.destroyAllWindows()
