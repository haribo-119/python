'''
    경계선
    Canny Edge Detection
'''
import cv2
img = cv2.imread('../ImgProcessing_Study/OpenCV/snowman.png')

# Canny(대상 이미지, minVal(하위임계값),maxVal(상위임계값))
canny = cv2.Canny(img, 150,200)

cv2.imshow('img',img)
cv2.imshow('canny',canny)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''경계선 트랙바 threshold1(하위임계값),threshold2(상위임계값))'''
import cv2
img = cv2.imread('../ImgProcessing_Study/OpenCV/snowman.png')

def empty(pos):
    pass


name = "Trackbar"
cv2.namedWindow(name)
cv2.createTrackbar('threshold1',name,0,255,empty) # minVal
cv2.createTrackbar('threshold2',name,0,255,empty) # maxVal


while True:
    threshold1 = cv2.getTrackbarPos('threshold1',name)
    threshold2 = cv2.getTrackbarPos('threshold2',name)


    # Canny(대상 이미지, minVal(하위임계값),maxVal(상위임계값))
    canny = cv2.Canny(img, threshold1,threshold2)

    cv2.imshow('img',img)
    cv2.imshow(name,canny)

    if cv2.waitKey(1) == ord('q') :
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
