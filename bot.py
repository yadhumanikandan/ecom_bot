import telebot
from telebot import types
import dataBase
import threading


TOKEN = None

with open("token.txt") as f:
    TOKEN = f.read().strip()

bot = telebot.TeleBot(TOKEN)

db = dataBase.DataBase()

#for waiting a fuction to finish befor continuing the exicution
semaphore = threading.Semaphore(0)

#to store all the data of user
allData = ()
firstName = ()
flname = ""
number = ""
address = ""

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.add("/show_products")

catogory = types.ReplyKeyboardMarkup(resize_keyboard=True)
catogory.row('catagory_1','catagory_2','catagory_3')
catogory.row('catagory_4','catagory_5','catagory_6')
catogory.row('catagory_7','catagory_8','catagory_9')


@bot.message_handler(commands=['start', 'hello'])
def startbot(message):
    bot.send_message(message.chat.id, "Welcome to KBS Grocery")
    if db.checkUsernameExist(message.chat.id):
        d=db.get_info(message.chat.id)
        firstName = d[0]
        bot.send_message(message.chat.id, ("hello "+firstName[1]+"\nPlease select an option.."), reply_markup=menu)
        
    else:
        db.addUser(message.chat.id, message.from_user.first_name, message.from_user.last_name, " ", " ", " ")
        print("user added to database ")
        d=db.get_info(message.chat.id)
        firstName = d[0]
        bot.send_message(message.chat.id, ("hello "+firstName[1]+"\nPlease register by entering your details."))
        bot.send_message(message.chat.id, "Enter your full name")
        bot.register_next_step_handler(message, fname)
        semaphore.acquire()
        bot.send_message(message.chat.id, "Enter your phone number")
        bot.register_next_step_handler(message, phnum)
        semaphore.acquire()
        bot.send_message(message.chat.id, "Enter your address in one line")
        bot.register_next_step_handler(message, addres)
        semaphore.acquire()
        bot.send_message(message.chat.id, "Registerd succesfully")
        bot.send_message(message.chat.id, "Please select an option ", reply_markup=menu)
        userData = db.get_info(message.chat.id)
        allData = userData[0]


def fname(message):
    flname = message.text
    db.updateFname(message.chat.id, flname)
    semaphore.release()

def phnum(message):
    number = message.text
    db.updatePhone(message.chat.id, number)
    semaphore.release()

def addres(message):
    address = message.text
    db.updateAddress(message.chat.id, address)
    semaphore.release()


@bot.message_handler(commands=['show_products'])
def product_catogory(message):
    bot.send_message(message.chat.id, 'Please select the catogory', reply_markup=catogory)

#to debug a security problem
@bot.message_handler(commands=['print_data'])
def printData(message):
    userData = db.get_info(message.chat.id)
    allData = userData[0]
    print(allData)

@bot.message_handler(func=lambda msg: True)
def print_message(message):
    print(message.text)



bot.infinity_polling()
