import telepot

TELEGRAM_TOEKN = "1034329106:AAH3tthjTrG8gj9zDoPOml_bAvtsbgRG44Q"


def handler(msg):
    content_type, chat_type, chat_id, msg_date, msg_id = telepot.glance(
        msg, long=True)

    print(msg)

    if content_type == "text":
        bot.sendMessage(chat_id, "[반사] {}".format(msg["text"]))


bot = telepot.Bot(TELEGRAM_TOEKN)
bot.message_loop(handler, run_forever=True)  # 콜백함수를 인자로 넣어준다
