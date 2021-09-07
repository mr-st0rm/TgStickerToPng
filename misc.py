import logging
from aiogram import types

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
memory_storage = MemoryStorage()

dp = Dispatcher(bot, storage=memory_storage)
logging.basicConfig(level=logging.INFO)

