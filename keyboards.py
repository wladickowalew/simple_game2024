from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

buttons = [
    [KeyboardButton(text="Весна"), KeyboardButton(text="Лето")],
    [KeyboardButton(text="Осень"),KeyboardButton(text="Зима")]
]
first_kb = ReplyKeyboardMarkup(keyboard=buttons,
                               one_time_keyboard=True,
                               resize_keyboard=True)

r_buttons = [
    [KeyboardButton(text="Red"), KeyboardButton(text="Orange"), KeyboardButton(text="Yellow")],
    [KeyboardButton(text="Green")],
    [KeyboardButton(text="Cyan"), KeyboardButton(text="Blue")],
    [KeyboardButton(text="Magenta")]
]
rainbow_kb = ReplyKeyboardMarkup(keyboard=r_buttons,
                                 one_time_keyboard=True,
                                 resize_keyboard=True)

ibuttons = [
    [
        InlineKeyboardButton(text='Весна', callback_data='Spring'),
        InlineKeyboardButton(text="Лето", callback_data='Summer')],
    [
        InlineKeyboardButton(text="Осень", callback_data='Autumn'),
        InlineKeyboardButton(text="Зима", callback_data='Winter')]
]
ifirst_kb = InlineKeyboardMarkup(inline_keyboard=ibuttons)