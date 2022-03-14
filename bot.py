import telebot
import os

import blink_detection
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, 'Привет!')


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, 'Скинь мне видео, я скажу сколько раз там человек моргнул.')


@bot.message_handler(content_types=['text'])
def text_handler(message):
    bot.send_message(message.chat.id, 'Используй /help')


@bot.message_handler(content_types=['video'])
def handle_docs_photo(message):
    try:
        file_info = bot.get_file(message.video.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        dir_path = os.path.dirname(os.path.realpath(__file__))
        src = dir_path + '/video/' + message.video.file_name

        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        bot.reply_to(message, "Пожалуй, я сохраню это")

        left_blinks, right_blinks = blink_detection.calculate_blinks(src)
        bot.send_message(message.chat.id, f'Левым глазом ты моргнул {left_blinks} раз, а правым {right_blinks} раз')


    except Exception as e:
        bot.reply_to(message, e)


if __name__ == "__main__":
    print('bot started!')
    bot.polling()