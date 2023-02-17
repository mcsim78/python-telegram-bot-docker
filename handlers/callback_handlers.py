from aiogram import types, Dispatcher

from bot_lib.settings import BTN_LIST_1, BTN_LIST_2
from bot_lib.bot_create import logger, some_cb


async def callback_btn_actions(callback_query: types.CallbackQuery, callback_data: dict):
    logger.info(f'Callback data: {callback_data}')
    await callback_query.message.answer(f'Pressed the button {callback_data["action"]}')


def register_callback_handlers(dp: Dispatcher):
    # Place your handlers here
    actions = BTN_LIST_1['buttons'].keys() | BTN_LIST_2['buttons'].keys()
    dp.register_callback_query_handler(callback_btn_actions, some_cb.filter(action=actions))
