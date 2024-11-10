import cv2
import matplotlib.pyplot as plt
# Đọc ảnh
img = cv2.imread('/Users/speed/Downloads/image/Image_for_TeamSV/femme.png')  # Ảnh xám
img_1 = cv2.imread('/Users/speed/Downloads/image/Image_for_TeamSV/Fruit.jpg')

img_1_rgb = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)

# Áp dụng Canny
edges = cv2.Canny(img, 100, 200)
edges_1 = cv2.Canny(img_1_rgb, 100, 200)
# Hiển thị kết quả
plt.subplot(1,2,1)
plt.imshow(edges)

plt.subplot(1,2,2)
plt.imshow(edges_1)
plt.show()

