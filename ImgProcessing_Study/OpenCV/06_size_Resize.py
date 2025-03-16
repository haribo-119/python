'''
    이미지
'''
# 고정 크기로 설정
import cv2
img = cv2.imread('..\ImgProcessing_Study\OpenCV\img.jpg')
dst = cv2.resize(img, (400,500)) # width,height 고정 크기

cv2.imshow('before',img)
cv2.imshow('after',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 비율로 설정
import cv2
img = cv2.imread('..\ImgProcessing_Study\OpenCV\img.jpg')
dst = cv2.resize(img,None,fx=0.5,fy=0.5) # x,y 비율 정의(0.5배로 축소)

cv2.imshow('before',img)
cv2.imshow('after',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
    이미지 보간법
    # 좀 더 이미지를 자연스럽게 줄여줌
    (이미지를 줄일때 비어있는 셀을 채워준다)
    1) cv2.INTER_AREA : 크기 줄일 때 사용
    2) cv2.INTER_CUBIC : 크기 늘릴때 사용(속도 느림, 퀄리티 좋음)
    3) cv2.INTER_LINEAR : 크기 늘릴 때 사용(기본값)
'''

# 보간법 적용하여 축소
import cv2
img = cv2.imread('..\ImgProcessing_Study\OpenCV\img.jpg')
dst = cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA) # x,y 비율 정의(0.5배로 축소)

cv2.imshow('before',img)
cv2.imshow('after',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 보간법 적용하여 확대
import cv2
img = cv2.imread('..\ImgProcessing_Study\OpenCV\img.jpg')
dst = cv2.resize(img,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_CUBIC) # x,y 비율 정의(0.5배로 축소)

cv2.imshow('before',img)
cv2.imshow('after',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
    동영상
'''
# 고정 크기로 설정
import cv2
cap = cv2.VideoCapture(r'..\ImgProcessing_Study\OpenCV\video.mp4')

while cap.isOpened() :
    ret,frame = cap.read()
    if not ret:
        break
    
    # 고정 크기로 설정
    frame_resized = cv2.resize(frame,(400,500))    

    cv2.imshow('video',frame_resized)
    if cv2.waitKey(1) == ord('q') :
        break

cap.release()
cv2.destroyAllWindows()



# 비율로 설정
import cv2
cap = cv2.VideoCapture(r'..\ImgProcessing_Study\OpenCV\video.mp4')

while cap.isOpened() :
    ret,frame = cap.read()
    if not ret:
        break
    
    # 비율로 설정
    frame_resized = cv2.resize(frame,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_CUBIC)    

    cv2.imshow('video',frame_resized)
    if cv2.waitKey(1) == ord('q') :
        break

cap.release()
cv2.destroyAllWindows()