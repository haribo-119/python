'''
    이미지 저장
'''
import cv2
img = cv2.imread('..\ImgProcessing_Study\OpenCV\img.jpg',cv2.IMREAD_GRAYSCALE) # 흑백으로 이미지 불러오기

# 이미지 저장
result = cv2.imwrite('img_save.jpg',img) # true 또는 false를 반환
#imwrite('파일이름.저장형식', 저장할 이미지)
print(result)

'''
    동영상 저장
'''
import cv2
cap = cv2.VideoCapture(r'..\ImgProcessing_Study\OpenCV\video.mp4')

# 동영상 파일 저장
# 코덱 정의
fourcc   = cv2.VideoWriter_fourcc(*'DIVX')

# 프레임 크기, FPS
width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter('output.avi',fourcc,fps,(width,height))
# 저장할 파일명, 코덱,  FPS, 크기(Width,height)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret :
        break

    out.write(frame) # 영상 데이터만 저장(소리X)   
    cv2.imshow('video',frame)
    if cv2.waitKey(1) == ord('q'):
        break
out.release() # 자원 해제    
cap.release()
cv2.destroyAllWindows()