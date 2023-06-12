from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("cat"))
    keyboard.add(KeyboardButton("dog"))
    return keyboard