from aiogram import executor
from bot_lib.bot_create import dp, logger
from handlers import message_handlers, callback_handlers, error_handlers


# ====================
# CALLBACK HANDLERS
# ====================
callback_handlers.register_callback_handlers(dp)
# ==================
# MESSAGE HANDLERS
# ==================
message_handlers.register_message_handlers(dp)
# ==================
# ERROR HANDLERS
# ==================
error_handlers.register_error_handlers(dp)


if __name__ == '__main__':
    logger.info("Start Bot")
    executor.start_polling(dp, skip_updates=True)