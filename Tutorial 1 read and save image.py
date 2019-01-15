import cv2

image = cv2.imread("red_panda.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite("Gray_panda.jpg", gray_image)

