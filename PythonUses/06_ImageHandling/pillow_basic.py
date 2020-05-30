import os
import requests
from PIL import Image

path = os.getcwd() + "\\PythonUses\\Images\\"
img = Image.open(path + "1.jpg")

img.show()  # 기본 뷰어로 열기
img = img.rotate(45)  # 이미지 회전
img.save(path + "sample.png")  # 다른 포맷으로 저장

url = "https://cdn.pixabay.com/photo/2020/01/24/12/29/konigssee-4790116_960_720.jpg"
img = Image.open(requests.get(url, stream=True).raw)  # 웹 이미지 가져오기
img.show()
img.save(path + "4.jpg")
