import telebot
from telebot import types
import dataBase


bot = telebot.TeleBot("6076557712:AAHiHRMsr68rOUm1-5BjpuDZUf4pmXwWimA")

db = dataBase.DataBase()

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.add("/show_products")

catogory = types.ReplyKeyboardMarkup(resize_keyboard=True)
catogory.add('catagory_example','catagory_example','catagory_example', 'catagory_example')


@bot.message_handler(commands=['start', 'hello'])
def startbot(message):
    # bot.reply_to(message, "welcome!!!", reply_markup=menu)
    flag = db.checkUsernameExist(message.chat.id)
    print(flag)


@bot.message_handler(commands=['show_products'])
def product_catogory(message):
    bot.reply_to(message, 'select catogory', reply_markup=catogory)

@bot.message_handler(func=lambda msg: True)
def print_message(message):
    print(message.text)

bot.infinity_polling()
