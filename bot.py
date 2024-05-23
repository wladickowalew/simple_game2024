import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from Game_adapter import *
from config import TELEGRAM_TOKEN

IOAdapter.init("tg_bot")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

dp.include_routers(router)


@dp.message(Command("name"))
async def name(message: types.Message):
    s = message.from_user.full_name
    id = message.from_user.id
    await message.answer(f"name: {s} id: {id}")


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
