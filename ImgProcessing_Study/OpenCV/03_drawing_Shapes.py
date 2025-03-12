'''
    빈스케치북 만들기
'''
# import cv2
# import numpy as np

# # 세로 480 X 가로 640, 3 Channel (RGB) 에 해당하는 스케치북 만들기
# img = np.zeros((480,640,3), dtype=np.uint8)
# # img[:] = (255,255,255) # 전체 공간을 흰 색으로 채우기
# # # 각각 img[:] = (blue,green,red) blue, green, red로 순서로 채워진다
# # print(img)
# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
    일부 영역 색칠
'''
# import cv2
# import numpy as np

# img = np.zeros((480,640,3), dtype=np.uint8)
# img [100:200,200:300] = (255,255,255)
# # img [세로,가로]  = (흰색)

# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

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

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()