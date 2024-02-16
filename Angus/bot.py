import telebot
import database
import buttons

bot = telebot.TeleBot("6260300152:AAG7EchVpa27hnIhm3tCWEGK8_1ZJcc7OnA")

users: {}

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    checker = database.check_users(user_id)
    if checker == True:
        bot.send_message(user_id, 'Главное меню', reply_markup=buttons.main_menu())
    elif checker == False:
        bot.send_message(user_id, "Здравствуйте. \n"
                                  "Прежде чем начать, выберите язык: ")
        bot.register_next_step_handler(message, registration)
def registration(message):
    user_id = message.from_user.id
    name = message.text
    bot.send_message(user_id, "Отправьте свой номер телефона", reply_markup=buttons.get_phone_number())
    bot.register_next_step_handler(message, get_number, name)
def get_number(message, name):
    user_id = message.from_user.id
    if message.contact:
        phone_number = message.contact.phone_number
        bot.send_message(user_id, "Вы успешно зарегестрировались!", reply_markup=types.ReplyKeyboardRemove())
        database.add_user(user_id=user_id, user_name=name, user_phone_number=phone_number)
        print(database.get_users())
    else:
        bot.send_message(user_id, "Отправьте свой номер через кнопку")
        bot.register_next_step_handler(message, get_number, name)
    print(message.contact)
def feedback_fc(message):
    user_id = message.from_user.id
    user_phone = message.from_user.phone_number
    bot.send_message(-1001996929800, f"{message.text}\n"
                                     f"Юзер пользователя: {user_id}" f"Телефон номер: {user_phone}")

bot.infinity_polling()

