import telebot
from telebot import types

bot = telebot.TeleBot("6076557712:AAHiHRMsr68rOUm1-5BjpuDZUf4pmXwWimA")

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.add("/show_products")

catogory = types.ReplyKeyboardMarkup(resize_keyboard=True)
catogory.add('c 1','c 2','c 3', 'c 4')

@bot.message_handler(content_types=['new_chat_members'])
def handle_new_chat_members(message):
    for member in message.new_chat_members:
        bot.send_message(member.id, "welcom to kbs!!!")

@bot.message_handler(commands=['start', 'hello'])
def startbot(message):
    bot.reply_to(message, "welcom!!!", reply_markup=menu)

@bot.message_handler(commands=['show_products'])
def product_catogory(message):
    bot.reply_to(message, 'select catogory', reply_markup=catogory)

@bot.message_handler(func=lambda msg: True)
def print_message(message):
    print(message.text)

bot.infinity_polling()
