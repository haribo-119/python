'''
    이미지 변형(이진화)
    # 이진화 : 흰색과 검은색만으로로 나눔
'''
# # Threthold(=임계값) : 주어진 시간에 따라 기준이 변경
# # 3초면 가장 큰거거를 찾게됨, 10초면 큰거>중간 찾게됨
# # 시간이 길어질 수록 찾게되는 범위가 커진다 
# import cv2
# img = cv2.imread('../ImgProcessing_Study/OpenCV/book.jpg',cv2.IMREAD_GRAYSCALE)

# #threshold(이미지 파일,임계값,임계값보다 클때 적용할 색상,cv2.THRESH_BINARY)
# ret, binary = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# cv2.imshow('img',img)
# cv2.imshow('binary',binary)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Trackbar(값 변화에 따른 변형 확인)
import cv2
img = cv2.imread('../ImgProcessing_Study/OpenCV/book.jpg',cv2.IMREAD_GRAYSCALE)

def empty(pos):
    print(pos)
    pass

name = 'Trackbar'
cv2.namedWindow(name)

# createTrackbar(bar 이름 정의,윈도우 이름,임계값,최대값,값을 변경했을때 이벤트 처리)
cv2.createTrackbar('threshold',name,127,255,empty)

while True:
    thresh = cv2.getTrackbarPos('threshold',name) #bar 이름, 창의 이름
    ret, binary = cv2.threshold(img,thresh,255,cv2.THRESH_BINARY)

    if not ret:
        break

    cv2.imshow(name,binary)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()    