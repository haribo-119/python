'''
    오츠 알고리즘
    최적에 임계치 값을 찾아준다
    Bimodal Image에 사용하기 적합(최적의 임계치를 자동으로 발견)
'''
import cv2
img = cv2.imread('../ImgProcessing_Study/OpenCV/book.jpg',cv2.IMREAD_GRAYSCALE)

ret, binary = cv2.threshold(img,127,255,cv2.THRESH_BINARY) 
# threshold(-1로 값을 둔건, |cv2.THRESH_OTSU에서 오츠 알고리즘이 임계치를 정해줌 )
ret, otsu = cv2.threshold(img,-1,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU) # 오츠 알고리즘 적용
print('otsu threshold',ret) # 임계치가 몇으로 설정되어 있는지 확인

cv2.imshow('img',img)
cv2.imshow('binary',binary) 
cv2.imshow('otsu',otsu) 
cv2.waitKey(0)
cv2.destroyAllWindows()