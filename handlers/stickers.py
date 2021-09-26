import os

from aiogram import types
from misc import dp, bot
from utils.converter import convert


@dp.message_handler(content_types=types.ContentTypes.STICKER)
async def stickers(message: types.Message):
    downloaded_file = await message.sticker.download()
    downloaded_file.close() # close downloaded file object

    send_file = convert(downloaded_file.name.split("/")[1].split('.')[0])  # name of sending file

    with open(f'{send_file}', 'rb') as photo:
        await message.answer_photo(photo=photo, caption="Для конвертирования своих стикеров в фото используй"
                                                        " @{}".format((await bot.me).username))

    os.remove(path=f'{send_file}')
