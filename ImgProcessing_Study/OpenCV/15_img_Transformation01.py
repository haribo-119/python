'''
    이미지 변환
'''

'''팽창'''
# 이미지를 확장하여 작은 구멍을 채움
# 흰색 영역의 외곽 픽셀 주변에 횐색을 추가

import cv2
import numpy as np

kernel = np.ones((3,3), dtype=np.uint8)
# print(kernel) #np.ones : 3X3 배열에 각각 1을 넣어준다

img = cv2.imread('../ImgProcessing_Study/OpenCV/dilate.png',cv2.IMREAD_GRAYSCALE)
dilate1 = cv2.dilate(img,kernel,iterations=1) # iterations는 반복 횟수
dilate2 = cv2.dilate(img,kernel,iterations=2)
dilate3 = cv2.dilate(img,kernel,iterations=3)

cv2.imshow('gray',img)
cv2.imshow('dilate1',dilate1)
cv2.imshow('dilate2',dilate2)
cv2.imshow('dilate3',dilate3)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''침식'''
# 팽창의 반대 
# 이미지를 깍아서 노이즈를 제거
# 흰색 영역의 외곽 픽셀을 검은색으로 변경

import cv2
import numpy as np
kernel = np.ones((3,3), dtype=np.uint8)

img = cv2.imread('../ImgProcessing_Study/OpenCV/erode.png',cv2.IMREAD_GRAYSCALE)
erode1 = cv2.erode(img,kernel,iterations=1) # iterations는 반복 횟수
erode2 = cv2.erode(img,kernel,iterations=2)
erode3 = cv2.erode(img,kernel,iterations=3)

cv2.imshow('img',img)
cv2.imshow('erode1',erode1)
cv2.imshow('erode2',erode2)
cv2.imshow('erode3',erode3)

cv2.waitKey(0)
cv2.destroyAllWindows()
