import cv2
import numpy as np
from skimage.measure import compare_ssim
from PIL import Image, ImageFont, ImageDraw

cap = cv2.VideoCapture(0)  # 0번 장치 캠 오픈
if cap.isOpened() == False:
    print("카메라를 오픈 할 수 없습니다.")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

old_image = None
show_image = None

while True:
    ret, frame = cap.read()

    if ret is True:
        show_image = frame.copy()  # 이미지 복제

        if old_image is not None:
            grayA = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 현재이미지의 흑백 이미지
            grayB = cv2.cvtColor(
                old_image, cv2.COLOR_BGR2GRAY)  # 이전 이미지의 흑백 이미지
            (score, diff) = compare_ssim(
                grayA, grayB, full=True)  # (확률, 유사도 측정 후 이미지)
            diff = (diff * 255).astype("uint8")
            cv2.imshow("DIFF", diff)
            text = "유사도: {:0.09f}".format(score)

            # 이미지 위에 글씨
            font = ImageFont.truetype("malgun.ttf", 17)
            text_w, text_h = font.getsize(text)
            # opencv frame 넓이 높이
            w = show_image.shape[1]
            h = show_image.shape[0]
            # 글씨의 좌상단 좌표
            X_POS = w - text_w - 10
            Y_POS = h - text_h - 10

            # opencv 이미지를 pillow 형태로 변환
            pil_image = Image.fromarray(show_image)
            draw = ImageDraw.Draw(pil_image)
            draw.text((X_POS, Y_POS), text, (255, 255, 255), font=font)
            show_image = np.array(pil_image)  # 다시 opencv로

            # 스코어 낮아지면 빨간 사각형
            if score < 0.90:
                cv2.rectangle(show_image, (0, 0), (w, h), (0, 0, 255), 6)

        old_image = frame
        cv2.imshow("CCTV", show_image)
        # 종료 버튼
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
