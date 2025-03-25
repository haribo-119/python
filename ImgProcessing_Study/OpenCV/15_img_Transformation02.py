'''
    열림 & 닫힘
    팽창과 침식 함께 연산
'''

'''열림 : 침식 후 팽창 (깍아서 노이즈 제거 후 살 찌움)'''
 # dilate(erode(img))
import cv2
import numpy as np
kernel = np.ones((3,3),dtype=np.uint8)

img =cv2.imread('../ImgProcessing_Study/OpenCV/erode.png',cv2.IMREAD_GRAYSCALE)

erode = cv2.erode(img,kernel,iterations=3) #침식
dilate = cv2.dilate(erode,kernel,iterations=3) # 팽창

cv2.imshow('img',img)
cv2.imshow('erode',erode)
cv2.imshow('dilate',dilate)
cv2.waitKey(0)
cv2.destroyAllWindows()

''' 닫힘 : 팽창 후 침식 (구멍을 메운 후 다시 깍음) '''
 # erode(dilate(img))
import cv2
import numpy as np
kernel = np.ones((3,3),dtype=np.uint8)

img = cv2.imread('../ImgProcessing_Study/OpenCV/dilate.png',cv2.IMREAD_GRAYSCALE)

dilate = cv2.dilate(img,kernel,iterations=3)
erode = cv2.erode(dilate,kernel,iterations=3)

cv2.imshow('img',img)
cv2.imshow('dilate',dilate)
cv2.imshow('erode',erode)
cv2.waitKey(0)
cv2.destroyAllWindows()
