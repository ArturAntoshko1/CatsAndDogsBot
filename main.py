import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from dotenv import load_dotenv
import requests
import json

from keyboards import main_keyboard


load_dotenv()
bot_token = os.getenv("BOT_TOKEN")


bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def welcome(message: types.Message) -> None:
    await message.reply("Привет пользователь! Выбери опцию:", reply_markup=main_keyboard())


@dp.message_handler(Text(equals="cat"))
async def send_cat(message: types.Message) -> None:
    photo = requests.get(
        "https://api.thecatapi.com/v1/images/search").json()[0]["url"]
    await bot.send_photo(message.from_user.id, photo)


@dp.message_handler(Text(equals="dog"))
async def send_dog(message: types.Message) -> None:
    photo = requests.get(
        "https://api.thedogapi.com/v1/images/search").json()[0]["url"]
    await bot.send_photo(message.from_user.id, photo)


if __name__ == "__main__":
    executor.start_polling(dp)
