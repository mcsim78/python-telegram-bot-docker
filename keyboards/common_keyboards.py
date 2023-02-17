from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


async def get_list_buttons(buttons_list, cb: CallbackData) -> InlineKeyboardMarkup:
    """Returns list of buttons with type InlineKeyboardButton() with row_width=2

    Args:
        buttons_list (dict): Dictionary of buttons with callback_data and text
        cb: CallbackData factory

    Returns:
        InlineKeyboardMarkup: List of buttons with type InlineKeyboardButton()
    """
    new_btn_list = []
    for btn in buttons_list:
        new_btn_list.append(InlineKeyboardButton(text=buttons_list[btn], callback_data=cb.new(action=btn)))
    keyboard = InlineKeyboardMarkup(row_width=2).add(*new_btn_list)
    return keyboard


async def get_text_and_buttons_inline(buttons_list, cb: CallbackData):
    """Returns text of message and list of buttons with type InlineKeyboardButton()
    Args:
        buttons_list (dict): Dictionary of buttons with menu text, callback_data and text label
        cb: CallbackData factory
    Returns:
        message_text (str): Text of message
        keyboard (InlineKeyboardMarkup): List of buttons with type InlineKeyboardButton()
    """
    message_text = buttons_list['message_text']
    buttons = buttons_list['buttons']
    keyboard = await get_list_buttons(buttons, cb)
    return message_text, keyboard
