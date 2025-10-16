import cv2
from matplotlib import pyplot as plt
image = cv2.imread("naveed.jpg") 


resized_image = cv2.resize(image, (100,100))
Gaussian = cv2.GaussianBlur(resized_image, (15, 15), -5)  
Gaussian_rgb = cv2.cvtColor(Gaussian, cv2.COLOR_BGR2RGB)  
plt.imshow(Gaussian_rgb)
# plt.title('Gaussian Blurred Image')
plt.axis('on') #off
plt.show()
