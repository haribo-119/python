'''
    이미지 변형(원근)
'''

'''
   1) 사다리꼴 이미지 펼치기
'''
import cv2
import numpy as np

img = cv2.imread('../ImgProcessing_Study/OpenCV/newspaper.jpg')

# 가로 크기 640, 세로 크기 240으로 결과물 출력
width, height = 640, 240

# Input 4개 지점 (시계방향)
src = np.array([[511,352],[1008,345],[1122,584],[455,594]],dtype=np.float32)
# Output 4개 지점 (시계방향)
dst = np.array([[0,0],[width,0],[width,height],[0,height]],dtype=np.float32)


# (src를 dst 변환) 값을  matrix에 저장 
matrix = cv2.getPerspectiveTransform(src,dst)
# matrix 대로 변환을 함(변환할 이미지, 가공, 크기)
result = cv2.warpPerspective(img, matrix,(width,height))

cv2.imshow('img',img)
cv2.imshow('result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
    2) 회전된 이미지 올바로 세우기
'''
import cv2
import numpy as np

img = cv2.imread('../ImgProcessing_Study/OpenCV/poker.jpg')

# 가로 크기 640, 세로 크기 240으로 결과물 출력
width, height = 400, 580

# Input 4개 지점 (시계방향)
src = np.array([[966,211],[1266,475],[884,896],[580,610]],dtype=np.float32)
# Output 4개 지점 (시계방향)
dst = np.array([[0,0],[width,0],[width,height],[0,height]],dtype=np.float32)


# (src를 dst 변환) 값을  matrix에 저장 
matrix = cv2.getPerspectiveTransform(src,dst)
# matrix 대로 변환을 함(변환할 이미지, 가공, 크기)
result = cv2.warpPerspective(img, matrix,(width,height))

cv2.imshow('img',img)
cv2.imshow('result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()
