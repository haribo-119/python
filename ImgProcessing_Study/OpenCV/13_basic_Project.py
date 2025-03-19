'''
    미니 프로젝트 : 반자동 문서 스캐너
'''
import cv2
import numpy as np

point_list = []
src_img = cv2.imread('../ImgProcessing_Study/OpenCV/poker.jpg')

COLOR = (255,0,255) # 핑크
THICKNESS = 3
drawing = False # 선을 그릴지 여부 

def mouse_handler(event,x,y,flags,param) :
    global drawing
    if event == cv2.EVENT_LBUTTONDOWN :
        drawing = True # 선을 그리기 시작
        point_list.append((x,y))

    if  drawing :   
        prev_point = None # 직선의 시작점
        for point in point_list :
            cv2.circle(src_img,point,10,COLOR,cv2.FILLED)
            if prev_point:
                cv2.line(src_img,prev_point,point,COLOR,THICKNESS,cv2.LINE_AA)
            prev_point = point    

    if len(point_list) == 4:
        show_result() # 결과 출력

    cv2.imshow('img',src_img)

def show_result():
    # 가로 크기 640, 세로 크기 240으로 결과물 출력
    width, height = 400, 580
    # Input 4개 지점 (시계방향)
    src = np.float32(point_list)
    # Output 4개 지점 (시계방향)
    dst = np.array([[0,0],[width,0],[width,height],[0,height]],dtype=np.float32)

    # (src를 dst 변환) 값을  matrix에 저장 
    matrix = cv2.getPerspectiveTransform(src,dst)
    # matrix 대로 변환을 함(변환할 이미지, 가공, 크기)
    result = cv2.warpPerspective(src_img, matrix,(width,height))
    cv2.imshow('result',result)

cv2.namedWindow('img') # 여기에 마우스 이벤트 처리 핸들러 적용
cv2.setMouseCallback('img',mouse_handler)
cv2.imshow('img',src_img)
cv2.waitKey(0)
cv2.destroyAllWindows()