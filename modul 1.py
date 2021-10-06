import cv2

img = cv2.imread("aura.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gambar aura Original", img)
cv2.imshow("Gambar aura Grayscale", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()