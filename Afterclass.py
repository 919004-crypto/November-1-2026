import cv2

image = cv2.imread('bg.jpg')

cv2.namedWindow('Loaded Image',cv2.WINDOW_NORMAL)

cv2.resizeWindow('Loaded Image', 800, 500)

cv2.resizeWindow('Loaded Image', 200, 150)

cv2.resizeWindow('Loaded Image', 650, 400)

cv2.imshow('Loaded Image', image)

cv2.waitKey(0)
cv2.desstroyAllWindows()

print(f"Image Dimensions: {image.shape}")