import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from config import TELEGRAM_TOKEN

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
