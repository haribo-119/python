'''
    이미지 변형(이진화)
    # 이진화 : 흰색과 검은색만으로로 나눔
'''
'''그림판에서 제작한 이미지로 확인'''
import cv2
img = cv2.imread('../ImgProcessing_Study/OpenCV/threshold.png',cv2.IMREAD_GRAYSCALE)

def empty(pos):
    print(pos)
    pass

name = 'Trackbar'
cv2.namedWindow(name)

cv2.createTrackbar('threshold',name,127,255,empty)

while True:
    thresh = cv2.getTrackbarPos('threshold',name) 
    ret, binary = cv2.threshold(img,thresh,255,cv2.THRESH_BINARY)

    if not ret:
        break

    cv2.imshow('img',img) #이미지 원본
    cv2.imshow(name,binary) # threshold
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()    