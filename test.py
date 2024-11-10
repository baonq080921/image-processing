import cv2
import matplotlib.pyplot as plt


L = 256

image = cv2.imread('/Users/speed/Downloads/image/Image_for_TeamSV/femme.png')

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)
image_neg = L-1-image_rgb

#ANH GOC
plt.subplot(2,2,1)
plt.imshow(image_rgb)
plt.axis('off')
plt.title('ORIGINAL IMAGE', fontsize=8)

#ANH XAM
plt.subplot(2,2,2)
plt.imshow(image_rgb,cmap='gray')
plt.axis('off')
plt.title('GRAY IMAGE', fontsize=8)

#Anh Am ban
plt.subplot(2,2,3)
plt.imshow(image_neg)
plt.axis('off')
plt.title('NEGATIVE IMAGE',fontsize=8)

plt.subplot(2,2,4)
plt.imshow(image_hsv)
plt.axis('off')
plt.title('HSV IMAGE',fontsize=8)

plt.show()

