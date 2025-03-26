'''
    윤관선 - 면적
'''

''' 경계 사각형 '''
# 윤곽선의 경계면을 둘러싸는 사각형
# boundingRect()
import cv2
img = cv2.imread('../ImgProcessing_Study/OpenCV/card.png')
target_img = img.copy() # 사본 이미지

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, otsu = cv2.threshold(gray,-1,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(otsu,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

COLOR=(0,200,2) #녹색

for cnt in contours :
    # boundingRect()는 x,y,width,height를 반환
    x,y,width,height = cv2.boundingRect(cnt)
    # rectangle(이미지,사각형 좌표(왼쪽상단_모서리),사각형좌표(오른쪽하단_모서리),색상,두께)
    cv2.rectangle(target_img,(x,y),(x+width,y+height),COLOR,2)

cv2.imshow('img',img)
cv2.imshow('contours',target_img)
# 원본 이미지 > 흑백 > otsu (이진화) > contours(윤곽선)
cv2.waitKey(0)
cv2.destroyAllWindows()

''' 면적 '''
#contourArea()
import cv2
img = cv2.imread('../ImgProcessing_Study/OpenCV/card.png')
target_img = img.copy() # 사본 이미지

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, otsu = cv2.threshold(gray,-1,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(otsu,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

COLOR=(0,200,2) #녹색

for cnt in contours :
   # 카드 한장 크기 : 가로 130 x 세로 205 = 26,650
   if cv2.contourArea(cnt) > 25000 :
        x,y,width,height = cv2.boundingRect(cnt)
            # rectangle(이미지,사각형 좌표(왼쪽상단_모서리),사각형좌표(오른쪽하단_모서리),색상,두께)
        cv2.rectangle(target_img,(x,y),(x+width,y+height),COLOR,2)

cv2.imshow('img',img)
cv2.imshow('contours',target_img)
# 원본 이미지 > 흑백 > otsu (이진화) > contours(윤곽선)
cv2.waitKey(0)
cv2.destroyAllWindows()