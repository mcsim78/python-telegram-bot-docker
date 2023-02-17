from aiogram import Dispatcher
from aiogram.utils.exceptions import MessageNotModified
from bot_lib.bot_create import dp, logger


@dp.errors_handler(exception=MessageNotModified)  # for skipping this exception
async def message_not_modified_handler(update, error):
    logger.error(f"MessageNotModified: {error} Update: {update}")
    return True


def register_error_handlers(dp: Dispatcher):
    dp.register_errors_handler(message_not_modified_handler, exception=MessageNotModified)
