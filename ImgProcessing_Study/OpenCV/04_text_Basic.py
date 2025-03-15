'''
    텍스트
    # OpenCV  에서 사용하는 글꼴 종류
    1) cv2.FONT_HERSHEY_SIMPLEX : 보통 크기의 산 세리프(sans-serif) 글꼴
    2) cv2.FONT_HERSHEY_PLAIN : 작은 크기의 산 세리프 글꼴
    3) cv2.FONT_HERSHEY_SCRIPT_SIMPLEX : 필기체 스타일 글꼴
    4) cv2.FONT_HERSHEY_TRIPLEX : 보통 크기의 세리프 글꼴
    5) cv2.FONT_ITALIC : 기울림(이탤릭체)
'''

import numpy as np
import cv2

img = np.zeros((480,640,3),dtype=np.uint8)

SCALE = 1
COLOR =(255,255,255) # 흰색
THICKNESS = 1

cv2.putText(img, "hi Simplex",(20,50),cv2.FONT_HERSHEY_SIMPLEX,SCALE,COLOR,THICKNESS)
# 텍스트 내용, 시작위치, 폰트 종류, 크기, 색깔, 두께

cv2.putText(img, "hi PLAIN",(20,150),cv2.FONT_HERSHEY_PLAIN,SCALE,COLOR,THICKNESS)
cv2.putText(img, "hi SCRIPT_SIMPLEX",(20,250),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,SCALE,COLOR,THICKNESS)
cv2.putText(img, "hi TRIPLEX",(20,350),cv2.FONT_HERSHEY_TRIPLEX,SCALE,COLOR,THICKNESS)
cv2.putText(img, "hi ITALIC",(20,450),cv2.FONT_HERSHEY_TRIPLEX| cv2.FONT_ITALIC,SCALE,COLOR,THICKNESS)
# FONT_ITALIC : 사용하려면, | 앞에 기본 폰트가 필요


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''
    한글
'''

import numpy as np
import cv2

img = np.zeros((480,640,3),dtype=np.uint8)

SCALE = 1
COLOR =(255,255,255) # 흰색
THICKNESS = 1

cv2.putText(img, "한글",(20,50),cv2.FONT_HERSHEY_SIMPLEX,SCALE,COLOR,THICKNESS)
# openCV 에서는 한글을 지원하지 안아 글자가 깨짐


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
    한글 우회 방법법
'''

import numpy as np
import cv2
# PIL (Python Image Library) 한글 우회
from PIL import ImageFont, ImageDraw, Image

def myPutText(src,text,pos,font_size,font_color) :
    img_pil = Image.fromarray(src)
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype('fonts/gulim.ttc',font_size)
    draw.text(pos,text,font=font,fill=font_color)
    return np.array(img_pil)

img = np.zeros((480,640,3),dtype=np.uint8)

FONT_SIZE = 30
COLOR =(255,255,255) # 흰색

# cv2.putText(img, "한글",(20,50),cv2.FONT_HERSHEY_SIMPLEX,SCALE,COLOR,THICKNESS)
# openCV 에서는 한글을 지원하지 안아 글자가 깨짐
img = myPutText(img,'안녕',(20,50),FONT_SIZE,COLOR,)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
