from aiogram import types
from aiogram.dispatcher.filters import CommandStart, CommandHelp

from misc import dp


@dp.message_handler(CommandStart())
async def welcome_user(message: types.Message):
    await message.answer("Привет, отправь мне стикер и я сконвертирую его в фотографию\n\nHi, just send me your sticker"
                         " and i convert it into photo")


@dp.message_handler(CommandHelp())
async def help_user(message: types.Message):
    await message.answer("Developer - @mr_storm\nMade on 07.09.2021\n")
