'''
    프로젝트 : 얼굴을 인식하여 캐릭터 씌우기
    1) Face Detection - 얼굴을 찾기
    2) Face Recognition - 누구의 얼굴인지, 얼굴의 주인 ex) 페이스 로그인
'''
import cv2
import mediapipe as mp

''' 얼굴을 찾고, 찾은 얼굴에 표시를 해주기 위한 변수 정의 '''
# 얼굴 검출을 위한 face_delection 모듈을 사용
mp_face_detection = mp.solutions.face_detection 
# 얼굴의 특징을 그리기 위한  drawing_utils 모듈을 사용
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture('../ImgProcessing_Study/Face_mediapipe/face_video.mp4')
with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.7) as face_detection:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      break

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    # cv2.COLOR_BGR2RGB : BGR에서 RGB로 색상을 변경
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # 이미지안의 얼굴을 검출
    results = face_detection.process(image)

    # Draw the face detection annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # 검출된 얼굴에 그리기
    if results.detections:
      # 6개 특징 : 오른쪽 눈, 왼쪽 눈, 코 끝부분, 입 중심, 오른쪽 귀, 왼쪽 귀(귀구슬점, 이주)
      for detection in results.detections:
        mp_drawing.draw_detection(image, detection)
        print(detection)


    # Flip the image horizontally for a selfie-view display.
    # cv2.resize(image,None,fx=0.5,fy=0.5 화면 크기 줄이기
    cv2.imshow('MediaPipe Face Detection', cv2.resize(image,None,fx=0.5,fy=0.5))
    
    if cv2.waitKey(4) == ord('q'):
      break
cap.release()
cv2.destroyAllWindows()