import telebot
from telebot import types
import dataBase


TOKEN = None

with open("token.txt") as f:
    TOKEN = f.read().strip()

bot = telebot.TeleBot(TOKEN)

db = dataBase.DataBase()

data = ()

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.add("/show_products")

catogory = types.ReplyKeyboardMarkup(resize_keyboard=True)
catogory.add('catagory_example','catagory_example','catagory_example', 'catagory_example')


@bot.message_handler(commands=['start', 'hello'])
def startbot(message):
    # bot.reply_to(message, "welcome!!!", reply_markup=menu)
    bot.send_message(message.chat.id, "Welcome to KBS Grocery")
    if db.checkUsernameExist(message.chat.id):
        d=db.get_info(message.chat.id)
        data = d[0]
        bot.send_message(message.chat.id, ("hello "+data[1]+"\nPlease select an option.."), reply_markup=menu)
        # print(data[1])
        
    else:
        db.addUser(message.chat.id, message.from_user.first_name, message.from_user.last_name)
        print("user added to database ")
        d=db.get_info(message.chat.id)
        data = d[0]
        bot.send_message(message.chat.id, ("hello "+data[1]+"\nPlease select an option.."), reply_markup=menu)
        # bot.reply_to(message, "registerd succesfully")


@bot.message_handler(commands=['show_products'])
def product_catogory(message):
    bot.send_message(message.chat.id, 'Please select the catogory', reply_markup=catogory)

@bot.message_handler(func=lambda msg: True)
def print_message(message):
    print(message.text)

bot.infinity_polling()
