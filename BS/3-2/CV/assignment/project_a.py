import sys
import cv2
import numpy as np

# 이미지 읽기
img = cv2.imread("./assets/cat.jpg")
if img is None:
    sys.exit("파일을 찾을 수 없습니다.")

# 컬러 사진을 흑백 사진으로 변환하는 공식 사용
R = img[:, :, 2]  # 빨간 채널
G = img[:, :, 1]  # 초록 채널
B = img[:, :, 0]  # 파란 채널

# 공식 I = 0.299R + 0.587G + 0.114B를 사용하여 흑백 이미지 계산
cvt_img = 0.299 * R + 0.587 * G + 0.114 * B
cvt_img = cv2.convertScaleAbs(cvt_img)  # 결과를 uint8 형식으로 변환

# 원본 이미지와 흑백 이미지를 표시
cv2.imshow("Color Image", img)
cv2.imshow("Grayscale Image", cvt_img)
cv2.waitKey()
cv2.destroyAllWindows()