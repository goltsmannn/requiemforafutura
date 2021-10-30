
import config
import telebot
from datetime import datetime


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def start_chat(message):
    bot.send_message(message.chat.id, config.greeting)


@bot.message_handler(commands=["photo"])
def save_photos(message):

@bot.message_handler(content_types=["text"])
def redirect_messages(message):
    with open('responses.txt', 'a', encoding='utf-8') as f:
        date = datetime.utcfromtimestamp(message.date)
        f.write('Отправил: @' + message.chat.username + '\n')
        f.write('Время отправки предложки: ' + date.strftime("%Y-%m-%d") + '\n')
        f.write('Текст предложки: ' + message.text + '\n\n')


if __name__ == '__main__':
    bot.infinity_polling()
