'''
    OpenCV를 이용하여 가로로 촬영된 영상을
    세로로 회전하는 프로그램을 작성하시오

    [조건]
    1) 회전 : 시계 반대방향으로 90도
    2) 재생속도 (FPS) : 원본 x 4배
    3) 출력 파일명 : city_output.avi(코덱:DIVX)
'''
import cv2

cap = cv2.VideoCapture('../ImgProcessing_Study/OpenCV/city.mp4')
fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # DIVX 코덱 설정

width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 원본 비디오 FPS를 가져옵니다.
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)
# 4배 빠른 재생 속도를 위한 대기 시간 계산
wait_time = int(1000/(fps*4))

#VideoWriter((height,width) - 반대로 넣음, 시계 반대방향으로 90도로 저장하기 위함)
out = cv2.VideoWriter('city_out.avi',fourcc,fps*4,(height,width))

while cap.isOpened() :
    ret, frame = cap.read()
    if not ret:
        print('가져올 프레임이 없습니다')
        break

    #시계 반대 방향으로 90도 (270도)
    rotate_270 = cv2.rotate(frame,cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imshow('video',rotate_270)
    # 회전된 프레임 비디오 파일에 저장
    out.write(rotate_270)

    if cv2.waitKey(wait_time)==ord('q'):
        print('사용자 입력에 의해 종료되었습니다')
        break
cap.release()
out.release()
cv2.destroyAllWindows()