from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.callback_data import CallbackData
from loguru import logger
from aiogram import Bot, Dispatcher
from bot_lib.settings import TELEGRAM_TOKEN


logger.add('logs/bot.log', format='{time:DD-MM-YY HH:mm:ss} - {level} - {message}', level='INFO', rotation='1 week',
           compression='zip')
# CallbackData factory
some_cb = CallbackData('callback_name', 'action')

bot = Bot(token=TELEGRAM_TOKEN, parse_mode='HTML')
storage = MemoryStorage()
# TODO: replace MemoryStorage to another stateful storage
dp = Dispatcher(bot, storage=storage)



