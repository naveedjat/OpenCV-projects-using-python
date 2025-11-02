import cv2

image = cv2.imread("naveed.jpg") 
# FOR WITHOUT COLORS IMAGE WE USE THE cv2.IMREAD_GRAYSCALE .
image = cv2.imread("naveed.jpg", cv2.IMREAD_GRAYSCALE) 
# image = cv2.imread("naveed.jpg", cv2.IMREAD_COLOR_RGB) 

cv2.imshow("image",image)
cv2.waitKey(0)

cv2.destroyAllWindows()
