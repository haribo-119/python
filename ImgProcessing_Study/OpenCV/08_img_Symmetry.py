'''
    이미지 대칭
'''
# 좌우 대칭
import cv2
img = cv2.imread('..\ImgProcessing_Study\OpenCV\img.jpg')
# flipCode > 0 : 좌우 대칭 Horizontal
flip_horizontal = cv2.flip(img,1)

cv2.imshow('img',img)
cv2.imshow('flip_horiaontal',flip_horizontal)
cv2.waitKey(0)
cv2.destroyAllWindows(0)

# 상하 대칭
import cv2
img = cv2.imread('..\ImgProcessing_Study\OpenCV\img.jpg')
# flipCode == 0 : 상하 대칭 Vertical
flip_Vertical = cv2.flip(img,0)

cv2.imshow('img',img)
cv2.imshow('flip_horiaontal',flip_Vertical)
cv2.waitKey(0)
cv2.destroyAllWindows(0)

# 상하 좌우 대칭
img = cv2.imread('..\ImgProcessing_Study\OpenCV\img.jpg')
# flipCode < 0 : 상하 좌우 대칭 both
flip_both = cv2.flip(img,-1)

cv2.imshow('img',img)
cv2.imshow('flip_horiaontal',flip_both)
cv2.waitKey(0)
cv2.destroyAllWindows(0)