import os
import cv2
import numpy
from PIL import Image
import requests


path = os.getcwd() + "\\PythonUses\\Images\\"
# img = cv2.imread(path + "2.jpg", cv2.IMREAD_COLOR)

# print(img.shape)  # 크기 출력(높이 , 폭, 채널)
# print(type(img))  # 타입 넘파이(numpy) array (ndarray)
# cv2.imshow("A", img)  # OpenCV는 자체 창으로 사진 연다
# cv2.waitKey(0)  # waitKey가 없으면 창이 켜졌다가 사라진다(무한대로 대기)
# cv2.destroyAllWindows()

# url = "https://cdn.pixabay.com/photo/2020/01/24/12/29/konigssee-4790116_960_720.jpg"

# url에서 get을 한 후 content(데이터)를 가져온다.
# bytearray로 캐스팅한다.
# 부호가 없는 8비트의 넘파이 배열 생성
# arr = numpy.asarray(bytearray(requests.get(url).content), dtype=numpy.uint8)
# img = cv2.imdecode(arr, cv2.IMREAD_COLOR)

# cv2.imshow("A", img)
# cv2.waitKey(0)  # waitKey가 없으면 창이 켜졌다가 사라진다(무한대로 대기)
# cv2.destroyAllWindows()

# PIL RGB, width : height
# OPENCV BGR, height: width
pil_image = Image.open(path + "3.jpg")
opencv_image = numpy.array(pil_image)
opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_RGB2BGR)  # 색 convert

cv2.imshow("A", opencv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
