from aiogram import types, Dispatcher

from bot_lib.bot_create import logger, some_cb
from bot_lib.settings import MSG_START, BTN_LIST_1, BTN_LIST_2
from keyboards.common_keyboards import get_text_and_buttons_inline


# @dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    logger.info(f"{message.from_user.username} (id: {message.from_user.id}) wrote: {message.text}")
    await message.reply(MSG_START)
    # send buttons #1
    text, buttons = await get_text_and_buttons_inline(BTN_LIST_1, some_cb)
    await message.answer(text, reply_markup=buttons)
    # send buttons #2
    text, buttons = await get_text_and_buttons_inline(BTN_LIST_2, some_cb)
    await message.answer(text, reply_markup=buttons)


async def echo(message: types.Message):
    logger.info(f"{message.from_user.username} (id: {message.from_user.id}) wrote: {message.text}")
    await message.answer(f"I'm alive! 😎\nYour message:\n{message.text}")


def register_message_handlers(dp: Dispatcher):
    # Place your handlers here
    dp.register_message_handler(cmd_start, commands=['start'])
    dp.register_message_handler(echo)




