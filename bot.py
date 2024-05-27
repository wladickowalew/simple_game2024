import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import CallbackQuery

from config import TELEGRAM_TOKEN
from keyboards import *

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()


@dp.message(Command("rainbow"))
async def rainbow(message: types.Message):
    await message.answer(f"Какое у тебя любимый цвет радуги?", reply_markup=rainbow_kb)


@dp.message(Command("time_year"))
async def time_year(message: types.Message):
    await message.answer(f"Какое у тебя любимое время года?", reply_markup=first_kb)


@dp.message(Command("itime_year"))
async def itime_year(message: types.Message):
    await message.answer(f"Какое у тебя любимое время года?", reply_markup=ifirst_kb)


@dp.message(Command("name"))
async def name(message: types.Message):
    s = message.from_user.full_name
    id = message.from_user.id
    await message.answer(f"name: {s} id: {id}")


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


@dp.callback_query(F.data == "Spring")
async def sping_callback(callback: CallbackQuery):
    await bot.send_message(callback.from_user.id, "ВЫ любите бабочек и когда тепло)")
    await callback.answer()


@dp.callback_query(F.data == "Summer")
async def sping_callback(callback: CallbackQuery):
    await bot.send_message(callback.from_user.id, "Море жара!")
    await callback.answer()


@dp.callback_query(F.data == "Autumn")
async def sping_callback(callback: CallbackQuery):
    await bot.send_message(callback.from_user.id, "Дожди и слякоть")
    await callback.answer()


@dp.callback_query(F.data == "Winter")
async def sping_callback(callback: CallbackQuery):
    await bot.send_message(callback.from_user.id, "Вьюга, новый год!")
    await callback.answer()


if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
