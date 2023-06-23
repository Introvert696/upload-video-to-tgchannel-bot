from dotenv import load_dotenv
import os
import telebot
import shutil

load_dotenv()

dir_path = os.getenv("DIR")
tg_bot_key = os.getenv("TGBOTKEY")
target_channel = os.getenv("TARGETTGCHANNEL")

bot = telebot.TeleBot(tg_bot_key)


def sendVideos():
    files = os.listdir(dir_path)
    channel_chat_id = bot.get_chat(target_channel).id
    for vid in files:

        try:
            video = open(dir_path+vid, 'rb')
            bot.send_video(channel_chat_id, video)
            video.close()
            shutil.move(dir_path+vid, dir_path+"uploaded/"+vid)
            print(vid+" - загружено")

        except Exception as ex:
            print(vid+" - не загружен, ошибка")
            print(ex)


if __name__ == "__main__":
    # bot.polling()
    sendVideos()
