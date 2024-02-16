from telebot import types


def get_phone_nubmer():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    phone_number = types.KeyboardButton('Поделиться контактом 📲', request_contact=True)
    kb.add(phone_number)
    return kb


def main_menu():
    kb - types.ReplyKeyboardMarkup(row_width=1)
    main_menu = types.InlineKeyboardMarkup(text="Закрыть задолженность", callback_data='')
    feedback = types.InlineKeyboardMarkup(text="Оставьте отзыв", callback_data='feedback')
    kb.add(main_menu, feedback)
    return kb


def language():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    uzbek = types.InlineKeyboardMarkup(text='Uzbek', callback_data="")
    rus = types.InlineKeyboardMarkup(text='Русский', callback_data="")
    kb.row(rus)
    kb.add(uzbek)
