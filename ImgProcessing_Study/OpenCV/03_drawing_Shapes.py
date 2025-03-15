'''
    빈스케치북 만들기
'''
import cv2
import numpy as np

# 세로 480 X 가로 640, 3 Channel (RGB) 에 해당하는 스케치북 만들기
img = np.zeros((480,640,3), dtype=np.uint8)
# img[:] = (255,255,255) # 전체 공간을 흰 색으로 채우기
# # 각각 img[:] = (blue,green,red) blue, green, red로 순서로 채워진다
# print(img)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
    일부 영역 색칠
'''
import cv2
import numpy as np

img = np.zeros((480,640,3), dtype=np.uint8)
img [100:200,200:300] = (255,255,255)
# img [세로,가로]  = (흰색)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
    직선
    진선의 종류 (line type)
'''
# 1) cv2.LINE_4 : 상하좌우 4 방향으로 연결된 선
# 2) cv2.LINE_8 : 대각선을 포함한 8 방향으로 연결된 선 (기본값)
# 3) cv2.LINE_AA : 부드러운 선(anti-aliasing)

import cv2
import numpy as np

img = np.zeros((480,640,3), dtype=np.uint8)

COLOR =(0,255,255) #BGR , 색깔 
THICKNESS = 3 #두께

cv2.line(img,(50,100),(400,50),COLOR,THICKNESS,cv2.LINE_8)
# img,( X1축,Y1축),(X2축,Y2축) x1,x2 로부터 x2,y2까지
# 그리기할 위치, 시작 점, 끝 점, 색깔, 두께, 선 종류
cv2.line(img,(50,200),(400,150),COLOR,THICKNESS,cv2.LINE_4)
cv2.line(img,(50,300),(400,250),COLOR,THICKNESS,cv2.LINE_AA)


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
    원
'''
import cv2
import numpy as np

img = np.zeros((480,640,3), dtype=np.uint8)

COLOR =(255,255,0) #BGR , 색깔 
RADIUS = 50 # 반지름
THICKNESS = 10 #두께

cv2.circle(img,(200,100),RADIUS,COLOR,THICKNESS,cv2.LINE_AA) # 속이 빈 원
# circle(img,(원의 중심점),(반지름),(색깔),(두께),(선타입))
cv2.circle(img,(400,100),RADIUS,COLOR,cv2.FILLED,cv2.LINE_AA) # 속이 채워진 원

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
    사각형
'''
import cv2
import numpy as np

img = np.zeros((480,640,3), dtype=np.uint8)

COLOR =(0,255,0) #BGR , 색깔 
THICKNESS = 3 #두께

cv2.rectangle(img,(100,100),(200,200),COLOR,THICKNESS)
# rectangle(img,(그릴 위치),(그릴위치),(색깔),(두께께))
cv2.rectangle(img,(300,100),(400,200),COLOR,cv2.FILLED)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
    다각형
'''
import cv2
import numpy as np

img = np.zeros((480,640,3), dtype=np.uint8)

COLOR =(0,0,255) #BGR , 색깔 
THICKNESS = 3 #두께

pts1 = np.array([[100,100],[200,100],[100,200]])
pts2 = np.array([[200,100],[300,100],[300,200]])


# cv2.polylines(img,[pts1],True,COLOR,THICKNESS,cv2.LINE_AA)
# # polylines(img,[위치],(그림-열림 닫힘 여부),(색깔),(두께),(선 종류))
# cv2.polylines(img,[pts2],True,COLOR,THICKNESS,cv2.LINE_AA)

# cv2.polylines(img,[pts1,pts2],True,COLOR,THICKNESS,cv2.LINE_AA)
# polylines(img,[위치] - list 형태로 넣어줄 수 있음 )
# pts1 과 pts2 다각형을 같이 그려줌

cv2.polylines(img,[pts1,pts2],True,COLOR,THICKNESS,cv2.LINE_AA )

pts3 = np.array([[[100,300],[200,300],[100,400]],[[200,300],[300,300],[300,400]]])
cv2.fillPoly(img,pts3, COLOR,cv2.LINE_AA)


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()