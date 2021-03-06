import numpy as np
import cv2
from sklearn.cluster import KMeans

#Loading image
inputImg = cv2.imread('test6.jpg',-1)

#Reshaping array of B,G,R colors values only to three columns
BGRvalues = inputImg.reshape((-1,3))

#Setting kmeans variable, giving cluster number, giving maximum iterations
kmeans = KMeans(n_clusters=2,max_iter=10)
kmeans.fit(BGRvalues)

#Changing centers dtype to uint8, reshaping kmeans output to image shape
cluster_centers = np.uint8(kmeans.cluster_centers_)
response = cluster_centers[kmeans.labels_]
outputImg = response.reshape(inputImg.shape)

#Showing final image
cv2.imshow('Clustered Image',outputImg)

#Wait for any key press for closing all the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
