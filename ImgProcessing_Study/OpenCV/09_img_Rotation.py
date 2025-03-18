'''
    이미지 회전
'''
'''시계방향 90도 회전'''
import cv2
img = cv2.imread('..\ImgProcessing_Study\OpenCV\img.jpg')

# 시계 방향으로 90도 회전
rotate_90 = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)

cv2.imshow('img',rotate_90)
cv2.waitKey(0)
cv2.destroyAllWindows

'''180도 회전'''
import cv2
img = cv2.imread('..\ImgProcessing_Study\OpenCV\img.jpg')

# 180도 회전
rotate_180 = cv2.rotate(img,cv2.ROTATE_180)

cv2.imshow('img',rotate_180)
cv2.waitKey(0)
cv2.destroyAllWindows

'''시계 반대 방향 90도 회전(시계방향 270도 회전)'''
import cv2
img = cv2.imread('..\ImgProcessing_Study\OpenCV\img.jpg')

# 시계 방향으로 270도 회전
rotate_270 = cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow('img',rotate_270)
cv2.waitKey(0)
cv2.destroyAllWindows