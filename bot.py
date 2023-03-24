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
catogory.row('catagory_1','catagory_2','catagory_3', 'catagory_3')
catogory.row('catagory_4','catagory_5','catagory_6', 'catagory_7')
catogory.row('catagory_8','catagory_9','catagory_10', 'catagory_11')
catogory.row('catagory_12','catagory_13','catagory_14', 'catagory_15')
catogory.row('catagory_16','catagory_17','catagory_18', 'catagory_19')
catogory.row('catagory_20','catagory_21','catagory_22', 'catagory_23')


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
