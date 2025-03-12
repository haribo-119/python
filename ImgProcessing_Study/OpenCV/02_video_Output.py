# # 동영상 파일 출력
import cv2
cap = cv2.VideoCapture(r'..\ImgProcessing_Study\OpenCV\video.mp4')

while cap.isOpened(): # 동영상 파일이 올바로 열려있는지 확인
   #cpa.read()의 반환값이 ret, frame
   ret, frame = cap.read() # ret : 성공 여부, frame : 받아온 이미지(프레임)
   if not ret:# ret : true, flase 값
      print('더 이상 가져올 프레임이 없어요')
      break
   cv2.imshow('video',frame)

   if cv2.waitKey(1) == ord('q'):
      #cv2.waitKey(1)는 키보드 입력시 아스키 코드를 출력
      # ord()함수는 아스키 코드로 만들어준다 
      print('사용자 입력에 의해 종료합니다')
      break 
   
cap.release() # 자원 해제
cv2.destroyAllWindows() # 모든 창 닫기

# 카메라 출력
import cv2
cap = cv2.VideoCapture(0) # 0번째 카메라 장치 (Device ID)

if not cap.isOpened(): # 카메라가 열리지 않은 경우
    exit() #프로그램 종류

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    cv2.imshow('camera',frame)
    if cv2.waitKey(1) == ord('q')
      break
    
cap.release()
cv2.destroyAllWindows()