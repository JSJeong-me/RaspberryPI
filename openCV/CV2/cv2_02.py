import cv2

src = cv2.imread('./bus.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Color', src)

cv2.waitKey(0)

cv2.destroyAllWindows()
