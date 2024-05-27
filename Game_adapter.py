from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("test"))
async def test(msg: Message):
    await msg.answer("Тестовое сообщение")


class IOAdapter:
    typeg = ''
    bot = None

    @staticmethod
    def init(typeg, bot=None):
        IOAdapter.typeg = typeg
        IOAdapter.bot = bot

    @staticmethod
    def get_io_functions():
        if IOAdapter.typeg == "console":
            return print, input
        elif IOAdapter.typeg == "tg_bot":
            return test, input()
