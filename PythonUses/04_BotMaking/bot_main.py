import telepot
import logging
import os
from module import get_dir_list, get_weather, money_translate

logging.basicConfig(level=logging.DEBUG)  # 로깅 레벨 설정
logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = "1034329106:AAH3tthjTrG8gj9zDoPOml_bAvtsbgRG44Q"


def handler(msg):
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


bot = telepot.Bot(TELEGRAM_TOKEN)
bot.message_loop(handler, run_forever=True)
