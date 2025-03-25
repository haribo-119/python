'''
    윤곽선
    경계선을 연결한 선
'''
import cv2
img = cv2.imread('../ImgProcessing_Study/OpenCV/card.png')
target_img = img.copy() # 사본 이미지

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, otsu = cv2.threshold(gray,-1,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)

# findContours 윤곽선을 검출
# findContours 함수는 윤곽선 정보(contours), 구조 또는 계층(hierarchy)를 반환함
# findContours(이미지,윤관석을 찾는 모드(mode),윤곽선을 찾을 때 근사치 방법(method))
contours, hierarchy = cv2.findContours(otsu,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

# drawContours 윤곽선 그리기
# drawContours(사본이미지(원본을 손상),윤관선 정보,-1은 전부 그림,색상,두께)
COLOR=(0,200,2) #녹색
cv2.drawContours(target_img, contours, -1,COLOR,2)

cv2.imshow('img',img)
cv2.imshow('gray',gray)
cv2.imshow('otsu',otsu)
cv2.imshow('contours',target_img)
# 원본 이미지 > 흑백 > otsu (이진화) > contours(윤곽선)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
    윤곽선 찾기 모드
    # findContours()
    1) cv2.RETR_EXTERNAL : 가장 외곽의 윤곽선만 찾음
    2) cv2.RETR_LIST : 모든 윤곽선 찾음(계층 정보가 없음)
    3) cv2.RETR_TREE : 모든 윤곽선 찾음(계층 정보를 트리 구조로 생성)
'''
''' 테스트 '''
import cv2
img = cv2.imread('../ImgProcessing_Study/OpenCV/card.png')
target_img = img.copy() # 사본 이미지

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, otsu = cv2.threshold(gray,-1,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)

# 테스트
# contours, hierarchy = cv2.findContours(otsu,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) # 외각
# contours, hierarchy = cv2.findContours(otsu,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
contours, hierarchy = cv2.findContours(otsu,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print(hierarchy)
print(f'총 발견 갯수 :{len(contours)}')

COLOR=(0,200,2) #녹색
cv2.drawContours(target_img, contours, -1,COLOR,2)

cv2.imshow('img',img)
cv2.imshow('gray',gray)
cv2.imshow('otsu',otsu)
cv2.imshow('contours',target_img)
# 원본 이미지 > 흑백 > otsu (이진화) > contours(윤곽선)
cv2.waitKey(0)
cv2.destroyAllWindows()