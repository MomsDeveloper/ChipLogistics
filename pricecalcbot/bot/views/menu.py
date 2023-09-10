"""Main menu view."""


from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from pricecalcbot.bot.callbacks.articles import OpenArticlesMenuCallback
from pricecalcbot.bot.callbacks.calcs import StartCalcsCallback
from pricecalcbot.bot.texts.menu import OPEN_ARTICLES_BTN, OPEN_CALC_BTN, TITLE

menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text=OPEN_ARTICLES_BTN,
            callback_data=OpenArticlesMenuCallback().pack(),
        ),
    ],
    [
        InlineKeyboardButton(
            text=OPEN_CALC_BTN,
            callback_data=StartCalcsCallback().pack(),
        ),
    ],
])


async def show_menu(message: Message) -> None:
    """Show main menu with navigation buttons.

    Main menu contains buttons for navigate to
    articles management menu and price calculation.

    Args:
        message: Message. Can be used to answer, modify or get user info.
    """
    await message.edit_text(
        text=TITLE,
        reply_markup=menu_kb,
    )
