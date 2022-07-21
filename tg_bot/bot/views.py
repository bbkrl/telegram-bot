import telebot

from decouple import config

token = config('TOKEN')
bot = telebot.Telebot(token)


@bot.message_handler(commands=['start'], content_types=['text'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет ✌️ ")


bot.infinity_poling()
