'''
    영역을 잘라서 새로운 윈도우(창)에 표시
    - 이미지 뿐만 아니라 동영상도 동일
'''
import cv2
img = cv2.imread('..\ImgProcessing_Study\OpenCV\img.jpg')
# img.shape #(390.640.3)

# crop = img[세로범위,가로범위]
crop = img[100:200,200:400] 
# 세로 기준 100 : 200 까지, 가로 기준 200:400 까지 자름

cv2.imshow('img',img) # 원본 이미지
cv2.imshow('crop',crop) # 잘린 이미지
cv2.waitKey(0)
cv2.destroyAllWindows()


# 영역을 잘라서 기존 윈도우에 넣기
import cv2
img = cv2.imread('..\ImgProcessing_Study\OpenCV\img.jpg')
crop = img[300:400,200:400] 
img[100:200,200:400] = crop


cv2.imshow('img',img) 
cv2.waitKey(0)
cv2.destroyAllWindows()