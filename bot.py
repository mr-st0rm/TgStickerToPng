from aiogram import executor

import handlers
from config import ADMINS
from misc import dp, bot


async def send_adm(dp):
    try:
        for admin in ADMINS:
            await bot.send_message(chat_id=admin, text="Я запущен!")
    except:
        pass

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=send_adm)
