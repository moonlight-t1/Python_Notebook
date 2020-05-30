import telepot
import logging
import os
from module import get_dir_list, get_weather, money_translate

import cv2
import numpy as np
from skimage.measure import compare_ssim
from PIL import Image, ImageFont, ImageDraw

import threading
import time

logging.basicConfig(level=logging.DEBUG)  # 로깅 레벨 설정
logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = "1034329106:AAH3tthjTrG8gj9zDoPOml_bAvtsbgRG44Q"

run_thread = False  # 종료를 위한 글로벌 변수
send_frame = False  # 현재 화면을 전송 위한 글로벌 변수


def send_frame_to_telegram(chat_id, frame):  # 텔레그램에 사진전송
    cv2.imwrite("_tmp.jpg", frame)
    bot.sendPhoto(chat_id, open("_tmp.jpg", mode="rb"))


def capture_cam(chat_id):
    global run_thread, send_frame
    cap = cv2.VideoCapture(0)  # 0번 장치 캠 오픈
    if cap.isOpened() is False:
        print("카메라를 오픈 할 수 없습니다.")

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    old_image = None
    show_image = None

    while run_thread:
        ret, frame = cap.read()

        if ret is True:
            show_image = frame.copy()  # 이미지 복제

            if old_image is not None:
                grayA = cv2.cvtColor(
                    frame, cv2.COLOR_BGR2GRAY)  # 현재이미지의 흑백 이미지
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
                    send_frame_to_telegram(chat_id, show_image)

                if send_frame:
                    send_frame_to_telegram(chat_id, show_image)
                    send_frame = False

            old_image = frame
            cv2.imshow("CCTV", show_image)
            # 종료 버튼
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()


def handler(msg):
    global run_thread, send_frame
    content_type, chat_type, chat_id, msg_date, msg_id = telepot.glance(
        msg, long=True)

    print(msg)

    # /dir c:\\test
    # 명령어 입력 하게 만든다
    if content_type == "text":
        str_message = msg["text"]
        if str_message[0:1] == "/":
            args = str_message.split(" ")  # 명령어와 인자값(arguemnt) 분리
            command = args[0]
            del args[0]

            # 파일 내용 출력
            if command == "/dir" or command == "/목록":
                filepath = " ".join(args)  # 리스트를 문자열로 바꾼다
                if filepath.strip() == "":
                    bot.sendMessage(chat_id, "/dir [대상폴더] 로 입력해주세요.")
                else:
                    filelist = get_dir_list(filepath)
                    bot.sendMessage(chat_id, filelist)

            # 파일 전송
            elif command[0:4] == "/get":
                filepath = " ".join(args)
                if os.path.exists(filepath):
                    try:
                        if command == "getfile":
                            bot.sendDocument(chat_id, open(
                                filepath, "rb"))  # 파일 전송
                        elif command == "/getimage":
                            bot.sendPhoto(chat_id, open(
                                filepath, "rb"))  # 파일 전송
                        elif command == "/getaudio":
                            bot.sendAudio(chat_id, open(
                                filepath, "rb"))  # 파일 전송
                        elif command == "/getvideo":
                            bot.sendVideo(chat_id, open(
                                filepath, "rb"))  # 파일 전송
                    except Exception as e:
                        bot.sendMessage(chat_id, "파일 전송 실패 {}".format(e))
                else:
                    bot.sendMessage(chat_id, "파일이 존재하지 않습니다.")

            # 날씨 출력
            elif command == "/weather" or command == "/날씨":
                w = " ".join(args)
                weather = get_weather(w)
                bot.sendMessage(chat_id, weather)

            # 환율 출력
            elif command == "/money" or command == "/환율":
                m = " ".join(args)
                money = money_translate(m)
                bot.sendMessage(chat_id, money)

            # CCTV
            elif command == "/mon":
                if args[0] == "start":
                    if not run_thread:
                        print("감시시작")
                        run_thread = True
                        t = threading.Thread(
                            target=capture_cam, args=(chat_id, ))
                        t.daemon = True
                        t.start()
                        bot.sendMessage(chat_id, "감시를 시작했습니다.")
                    else:
                        bot.sendMessage(chat_id, "현재 감시가 동작 중입니다.")
                elif args[0] == "stop":
                    print("감시종료")
                    run_thread = False
                    bot.sendMessage(chat_id, "감시를 중지합니다.")

            # 현재 화면 전송
            elif command == "/c":
                send_frame = True


bot = telepot.Bot(TELEGRAM_TOKEN)
bot.message_loop(handler, run_forever=True)
