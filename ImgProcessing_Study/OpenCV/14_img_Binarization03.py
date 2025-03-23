'''Adaptive Threshold
   이미지를 작은 영역으로 나누어서 임계치 적용
'''
import cv2
img = cv2.imread('../ImgProcessing_Study/OpenCV/book.jpg',cv2.IMREAD_GRAYSCALE)

def empty(pos):
    # print(pos)
    pass

name = 'Trackbar'
cv2.namedWindow(name)

# createTrackbar(bar 이름 정의,윈도우 이름,임계값,최대값,값을 변경했을때 이벤트 처리)
cv2.createTrackbar('block_size',name,25,100,empty) # 홀수만 가능, 1보다는 큰 값
cv2.createTrackbar('c',name,3,10,empty) #일반적으로 양수의 값을 사용

while True:
    block_size = cv2.getTrackbarPos('block_size',name) #bar 이름, 창의 이름 
    c = cv2.getTrackbarPos('c',name) #bar 이름, 창의 이름
    
    if block_size <= 1: # 1 이하면 3으로 변경
        block_size = 3

    if block_size % 2 == 0 : # 짝수이면 홀수로 변경
        block_size += 1     
    #adaptiveThreshold(불러올 이미지,임계치가 넘었을때 최대값,)
    binary = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,block_size,c)

    cv2.imshow(name,binary)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()   