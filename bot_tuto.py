#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""This example showcases how PTBs "arbitrary callback data" feature can be used.

For detailed info on arbitrary callback data, see the wiki page at
https://github.com/python-telegram-bot/python-telegram-bot/wiki/Arbitrary-callback_data

Note:
To use arbitrary callback data, you must install PTB via
`pip install "python-telegram-bot[callback-data]"`
"""
import logging
from typing import List, Tuple, cast

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    InvalidCallbackData,
    PicklePersistence,
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with inline buttons for features."""
    features = {
        "Option Strategy Executor": "This feature allows you to execute various options trading strategies automatically. Watch this video to learn more: https://youtu.be/nRsXY93wLZ0?si=6fg3PbfWmkRgXwy-",  
        "Option Simulator": "The option simulator helps you simulate and understand the outcomes of different trading scenarios. Watch this video to learn more: https://youtu.be/qHBR8u6pbGg?si=-VAVH9vkzs9pUAf3",
        "Indices Historical Data": "Access historical data of indices to make informed trading decisions.  Watch this video to learn more: https://youtu.be/UGIQzDORpMY?si=HHibX1te4ap1UmKK",
        "Future Dashboard": "View a comprehensive dashboard for tracking market trends.  Watch this video to learn more: https://youtu.be/6JTGtda84PM?si=oxmaZlvmRjR7Hn8Z"
    }
    keyboard = build_keyboard(features)
    await update.message.reply_text("👋 Welcome to OptionPerks Bot! Please choose a feature:", reply_markup=keyboard)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text(
        "Use /start to test this bot. Use /clear to clear the stored data so that you can see "
        "what happens, if the button data is not available. "
    )


async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Clears the callback data cache"""
    context.bot.callback_data_cache.clear_callback_data()
    context.bot.callback_data_cache.clear_callback_queries()
    await update.effective_message.reply_text("All clear!")

def build_keyboard(features: dict) -> InlineKeyboardMarkup:
    keyboard_buttons = [
        [InlineKeyboardButton(text=feature, callback_data=explanation)] for feature, explanation in features.items()
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)



async def list_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and sends the YouTube link for the selected feature."""
    query = update.callback_query
    await query.answer()
    feature_url = query.data
    await query.message.reply_text(
        text=f"Here's the YouTube link for the selected feature: {feature_url}"
    )
    
    # Add a handler for the /start command again
    await start(update, context)

    # we can delete the data stored for the query, because we've replaced the buttons
    context.drop_callback_data(query)


async def handle_invalid_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Informs the user that the button is no longer available."""
    await update.callback_query.answer()
    await update.effective_message.edit_text(
        "Sorry, I could not process this button click 😕 Please send /start to get a new keyboard."
    )


def main() -> None:
    """Run the bot."""
    # We use persistence to demonstrate how buttons can still work after the bot was restarted
    persistence = PicklePersistence(filepath="arbitrarycallbackdatabot")
    # Create the Application and pass it your bot's token.
    application = (
        Application.builder()
        .token("7121001803:AAEX63j9seqXmxZwVjdaoOPhhZV1jC7GqsE")
        .persistence(persistence)
        .arbitrary_callback_data(True)
        .build()
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("clear", clear))
    application.add_handler(
        CallbackQueryHandler(handle_invalid_button, pattern=InvalidCallbackData)
    )
    application.add_handler(CallbackQueryHandler(list_button))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()