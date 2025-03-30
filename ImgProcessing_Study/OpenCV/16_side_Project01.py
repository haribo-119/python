'''
    미니 프로젝트 : 개별 카드 추출해서 파일 저장
'''
import cv2
img = cv2.imread('../ImgProcessing_Study/OpenCV/card.png')
target_img = img.copy() # 사본 이미지

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, otsu = cv2.threshold(gray,-1,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(otsu,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

COLOR=(0,200,2) #녹색

idx = 1
for cnt in contours :
   # 카드 한장 크기 : 가로 130 x 세로 205 = 26,650
   if cv2.contourArea(cnt) > 25000 :
        x,y,width,height = cv2.boundingRect(cnt)
            # rectangle(이미지,사각형 좌표(왼쪽상단_모서리),사각형좌표(오른쪽하단_모서리),색상,두께)
        cv2.rectangle(target_img,(x,y),(x+width,y+height),COLOR,2)

        #[] 영역 만큼 짤라서 crop 변수에 저장
        crop = img[y:y+height, x:x+width]
        cv2.imshow(f'card_crop_{idx}',crop)
        cv2.imwrite(f'card_crop_{idx}.png',crop) # 파일 저장    
        idx += 1


cv2.imshow('img',img)
cv2.imshow('contours',target_img)
# 원본 이미지 > 흑백 > otsu (이진화) > contours(윤곽선)
cv2.waitKey(0)
cv2.destroyAllWindows()
