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
    if db.checkUsernameExist(message.chat.id):
        data=db.get_info(message.chat.id)
        print(data)
    else:
        db.addUser(message.chat.id, message.from_user.first_name, message.from_user.last_name)
        print("user added to database ")
        bot.reply_to(message, "registerd succesfully")


@bot.message_handler(commands=['show_products'])
def product_catogory(message):
    bot.reply_to(message, 'select catogory', reply_markup=catogory)

@bot.message_handler(func=lambda msg: True)
def print_message(message):
    print(message.text)

bot.infinity_polling()
