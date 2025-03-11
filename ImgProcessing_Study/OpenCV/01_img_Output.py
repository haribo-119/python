# 환경설정 - 터미널 : pip install opencv-python

# # 1.이미지 출력력
import cv2
print(cv2.__version__) # 버전 확인

img = cv2.imread(r'..\ImgProcessing_Study\OpenCV\img.jpg') # 해당 경로의 파일 읽어오기
cv2.imshow('img',img) # img 라는 이름의 창에 img를 표시
key = cv2.waitKey(0) # 지정된 시간(ms초) 동안 사용자 키 입력 대기
print(key)
cv2.destroyAllWindows() # 모든 창 닫기


# 읽기 옵션
# 1) cv2.IMREAD_COLOR : 컬러 이미지, 투명 영역은 무시 (기본값)
# 2) cv2.IMREAD_GRAYSCALE : 흑백 이미지
# 3) cv2.IMREAD_UNCHANGED : 투명 영역까지 포함

import cv2
img_color = cv2.imread(r'..\ImgProcessing_Study\OpenCV\img.jpg',cv2.IMREAD_COLOR)
img_gray = cv2.imread(r'..\ImgProcessing_Study\OpenCV\img.jpg',cv2.IMREAD_GRAYSCALE)
img_unchanged = cv2.imread(r'..\ImgProcessing_Study\OpenCV\img.jpg',cv2.IMREAD_UNCHANGED)


cv2.imshow('img_color',img_color)
cv2.imshow('img_gray',img_gray)
cv2.imshow('img_unchanged',img_unchanged)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Shape
# 이미지의 height, width, channel 정보
import cv2
img = cv2.imread(r'..\ImgProcessing_Study\OpenCV\img.jpg')
print(img.shape) # (640, 536, 3) 출력