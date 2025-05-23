'''
    프로젝트 : 얼굴을 인식하여 캐릭터 씌우기
    1) Face Detection - 얼굴을 찾기
    2) Face Recognition - 누구의 얼굴인지, 얼굴의 주인 ex) 페이스 로그인
'''
import cv2
import mediapipe as mp

# 대상이미지(3채널), x,y좌표 , width,heght, 덮어씌울 이미지(4채널)
def overlay(image,x,y,w,h,overlay_image) : 
  alpha = overlay_image[:, :, 3] #BGRA - A(alpha)값만 가져옴
  mask_image = alpha / 255 # 0~255 -> 255로 나누면 0 ~ 1 사이의 값
  # mask_image 값의 1 : 불투명, 0:완전)

  for c in range(0,3): #channel BGR
    image[y-h:y+h,x-w:x+w,c] = (overlay_image[:,:,c] * mask_image) 
    + (image[y-h:y+h,x-w:x+w,c] * (1-mask_image))

  
    


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

    '''이미지 불러오기'''# ..\ImgProcessing_Study\OpenCV\img.jpg
    image_right_eye = cv2.imread('../ImgProcessing_Study/Face_mediapipe/face_right.png',cv2.IMREAD_UNCHANGED) #크기:100x100(가로,세로)
    image_left_eye = cv2.imread('../ImgProcessing_Study/Face_mediapipe/face_left.png',cv2.IMREAD_UNCHANGED) #크기:100x100
    image_nose_tip = cv2.imread('../ImgProcessing_Study/Face_mediapipe/face_nose.png',cv2.IMREAD_UNCHANGED) #크기:300x100

    # cv2.imshow('img',image_right_eye)

    # 검출된 얼굴에 그리기
    if results.detections:
      # 6개 특징 : 오른쪽 눈, 왼쪽 눈, 코 끝부분, 입 중심, 오른쪽 귀, 왼쪽 귀(귀구슬점, 이주)
      for detection in results.detections:
        # mp_drawing.draw_detection(image, detection)#얼굴에 빨간 점들  찍어줌
        # print(detection)
        '''
          특정 위치 가져오기 print(detection)출력값 참고
        '''
        keypoints = detection.location_data.relative_keypoints
        right_eye = keypoints[0] # 오른쪽 눈 - [6개 특징]의 배열 순서
        left_eye = keypoints[1] # 왼쪽 눈 - [6개 특징]의 배열 순서
        nose_tip = keypoints[2]

        #  _ 변수 사용안함
        h, w, _ = image.shape # height, width, channel : 이미지로부터 세로, 가로 크기 가져옴
        right_eye = (int(right_eye.x * w)-20,int(right_eye.y * h)-100) # 이미지 내에서 실제 좌표(x,y)
        left_eye = (int(left_eye.x * w)+ 20, int(left_eye.y * h)-100)
        nose_tip =(int(nose_tip.x * w),int(nose_tip.y * h))
        
        '''
          양 눈에 동그라미 그리기
        '''
        # blue = (255,0,0)
        # pink = (203,192,255)
        # yellow = (0,255,255)
        # cv2.circle(image,right_eye,50,pink,10,cv2.LINE_AA)
        # cv2.circle(image,left_eye,50,blue,10,cv2.LINE_AA)
        # cv2.circle(image,nose_tip,30,yellow,10,cv2.LINE_AA)
        
        '''
          각 특징에다가 이미지 그리기
        '''
        # image[right_eye[1]-50 : right_eye[1] +50,right_eye[0]-50 : right_eye[0]+50] = image_right_eye
        # image[left_eye[1]-50 : left_eye[1] +50,left_eye[0]-50 : left_eye[0]+50] = image_left_eye
        # image[nose_tip[1]-50 : nose_tip[1] +50,nose_tip[0]-150 : nose_tip[0]+150] = image_nose_tip

        '''
          투명도 적용
        '''
        # image,x,y,w,h,overlay_image
        overlay(image,*right_eye,50,50,image_right_eye)
        overlay(image,*left_eye,50,50,image_left_eye)
        overlay(image,*nose_tip,150,50,image_nose_tip)


    # Flip the image horizontally for a selfie-view display.
    # cv2.resize(image,None,fx=0.5,fy=0.5 화면 크기 줄이기
    cv2.imshow('MediaPipe Face Detection', cv2.resize(image,None,fx=0.5,fy=0.5))
    
    if cv2.waitKey(4) == ord('q'):
      break
cap.release()
cv2.destroyAllWindows()