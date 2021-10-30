
import config
import telebot
from datetime import datetime


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def start_chat(message):
    bot.send_message(message.chat.id, config.greeting)


@bot.message_handler(content_types=["photo"])
def handle_docs_document(message):
    file = bot.get_file(message.photo[len(message.photo)-1].file_id)
    downloaded = bot.download_file(file.file_path)
    src = '/home/prom/bot/gallery/' + message.chat.username + datetime.utcfromtimestamp(message.date).strftime("%Y-%m-%y-%H:%M")
    with open(src, 'wb') as newFile:
        newFile.write(downloaded)


@bot.message_handler(content_types=["text"])
def redirect_messages(message):
    with open('responses.txt', 'a', encoding='utf-8') as f:
        date = datetime.utcfromtimestamp(message.date)
        f.write('Отправил: @' + message.chat.username + '\n')
        f.write('Время отправки предложки: ' + date.strftime("%Y-%m-%d") + '\n')
        f.write('Текст предложки: ' + message.text + '\n\n')


if __name__ == '__main__':
    bot.infinity_polling()
