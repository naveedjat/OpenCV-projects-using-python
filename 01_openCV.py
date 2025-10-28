import cv2

# Load the image from file
image = cv2.imread('karun.jpg')  # Replace with your image path


# Show the image in a window
cv2.imshow('Image',image)

cv2.waitKey(0)
