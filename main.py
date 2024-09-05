import os
from dotenv import load_dotenv # библиотека для безопасного получения токена от яндекс расписаний из файла .env
from telebot import TeleBot # библиотека для работы бота
import time

load_dotenv()

token = os.getenv('TOKEN')

bot = TeleBot(token, parse_mode=None)  # инициализация бота



@bot.message_handler(commands=["start"]) # обработчик команды начать/start
def start_message(message):
    bot.send_message(message.chat.id, f"Приветствую тебя, я эхо бот\nОтправь текст и я повторю")  # Отправляем клавиатуру.


@bot.message_handler(content_types=['text'])  # обработчик команды начать/start
def start_message(message):
    bot.send_message(message.chat.id,
                     f"ты написал - {message.text}")  # Отправляем клавиатуру.


if __name__ == '__main__':
    while True:
        try:
            bot.polling(non_stop=True, interval=0)
        except Exception as e:
            print(e)
            time.sleep(5)
            continue