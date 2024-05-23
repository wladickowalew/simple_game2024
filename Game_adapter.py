from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("test"))
async def test(msg: Message):
    await msg.answer("Тестовое сообщение")


class IOAdapter:
    typeg = ''

    @staticmethod
    def init(typeg):
        IOAdapter.typeg = typeg

    @staticmethod
    def get_io_functions():
        if IOAdapter.typeg == "console":
            return print, input
