#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    PicklePersistence,
    filters
)
from telegram.error import BadRequest

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define the rules message
RULES_MESSAGE = (
    "📜 **Rules for Original Views, Likes, or Reach:**\n\n"
    "1. **No Fake Followers:**\n"
    "   🚫 Your account should not have fake followers.\n"
    "2. **Stay Active:**\n"
    "   🔄 Keep your account active by posting regularly.\n"
    "3. **Fresh Accounts Only:**\n"
    "   🌱 Your account should not be too old.\n"
    "4. **Optimal Posting Times:**\n"
    "   🕛 Post at **12 PM**, **6 PM**, or **8 PM** for best reach.\n"
    "5. **Use Hashtags and Viral Music:**\n"
    "   🎵 Utilize proper hashtags and trending music on your posts.\n\n"
    "✨ **Follow these rules to help make your content go viral!**"
)

# Channel URLs and IDs
JOIN_CHANNELS = [
    ("https://t.me/techhearnner", "@techhearnner"),
    ("https://t.me/ajubhaitirangaclub", "@ajubhaitirangaclub"),
    ("https://t.me/betproai", "@betproai"),
    ("https://t.me/nmnearn", "@nmnearn")
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message asking the user to join the channels first."""
    join_channel_keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="-----👉 Join Channel 1 👈-----", url=JOIN_CHANNELS[0][0])],
        [InlineKeyboardButton(text="-----👉 Join Channel 2 👈-----", url=JOIN_CHANNELS[1][0])],
        [InlineKeyboardButton(text="-----👉 Join Channel 3 👈-----", url=JOIN_CHANNELS[2][0])],
        [InlineKeyboardButton(text="-----👉 Join Channel 4 👈-----", url=JOIN_CHANNELS[3][0])],
       
    ])
    await update.message.reply_text(
        "Hello!!! Welcome to the most advanced viral Instagram and YouTube bot.📈",
        reply_markup=join_channel_keyboard
    )

    await update.message.reply_text(
        "💀 Please join the following channels to access premium bot features 💀\n\n"
        "🤖 After joining the channels, click here\n"
        "----------👉 /viral 👈---------\n"
        "to access premium features 🤖"
    )

async def handle_join_check(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the event when the user clicks the 'I have joined all channels' button."""
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    all_joined = True

    try:
        for url, channel_id in JOIN_CHANNELS:
            member = await context.bot.get_chat_member(chat_id=channel_id, user_id=user_id)
            if member.status not in ['member', 'administrator', 'creator']:
                all_joined = False
                break

        if all_joined:
            keyboard = [
                [InlineKeyboardButton(text="📸 📸  Instagram  📸 📸", callback_data="instagram")],
                [InlineKeyboardButton(text="▶️ ▶️ YouTube ▶️ ▶️", callback_data="youtube")]
            ]
            await query.message.reply_text("Thanks for joining us! 📲 Ready to choose a platform that could go viral? Let’s dive in!", reply_markup=InlineKeyboardMarkup(keyboard))
        else:
            join_channel_keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton(text="-----👉 Join Channel 1 👈-----", url=JOIN_CHANNELS[0][0])],
                [InlineKeyboardButton(text="-----👉 Join Channel 2 👈-----", url=JOIN_CHANNELS[1][0])],
                [InlineKeyboardButton(text="-----👉 Join Channel 3 👈-----", url=JOIN_CHANNELS[2][0])],
                [InlineKeyboardButton(text="-----👉 Join Channel 4 👈-----", url=JOIN_CHANNELS[3][0])],
                [InlineKeyboardButton(text="I have joined all channels", callback_data="joined_check")]
            ])
            await query.message.reply_text("Sorry 😭,!!You need to join all our channels to access premium features. Please join the channels first:", reply_markup=join_channel_keyboard)
    except BadRequest as e:
        if str(e) == 'Chat not found':
            await query.message.reply_text("There was an error checking your channel membership. Please ensure you have joined the channels.")
        else:
            logger.error(f"Error checking channel membership: {e}")
            await query.message.reply_text("There was an error checking your channel membership. Please try again later.")

async def handle_platform_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the platform choice (Instagram or YouTube)."""
    query = update.callback_query
    await query.answer()
    platform = query.data

    if platform == "instagram":

        keyboard = [
            [InlineKeyboardButton(text="🔥 Make your content viral 🔥", callback_data="insta_viral")],
            [InlineKeyboardButton(text="👀 Instagram views 👀", callback_data="insta_views")],
            [InlineKeyboardButton(text="❤️ Likes ❤️", callback_data="insta_likes")],
            [InlineKeyboardButton(text="👍 IG reach 👍", callback_data="insta_reach")],
            [InlineKeyboardButton(text="😈 IG monetization 😈", callback_data="insta_monetization")]
        ]
    else:
        keyboard = [
            [InlineKeyboardButton(text=" 🔥 🔥 Channel views 🔥 🔥", callback_data="yt_views")],
            [InlineKeyboardButton(text=" 👍 👍 Likes 👍 👍", callback_data="yt_likes")],
            [InlineKeyboardButton(text=" 👀 👀 Watch time 👀 👀", callback_data="yt_watch_time")],
            [InlineKeyboardButton(text=" 👾 👾 Channel monetization 👾 👾", callback_data="yt_monetization")]
        ]

    await query.message.reply_text("🚀 🚀Select an option to viral your content 🚀 🚀 :", reply_markup=InlineKeyboardMarkup(keyboard))

async def handle_option_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the choice of specific Instagram or YouTube options."""
    query = update.callback_query
    await query.answer()
    option = query.data

    # Show the rules message
    await query.message.reply_text(RULES_MESSAGE)

    # Ask if the user has followed the rules
    keyboard = [
        [InlineKeyboardButton(text="👍 Yes, I have followed the rules", callback_data=f"confirm_{option}")]

        
    ]
    await query.message.reply_text(
    "✅ **Have you followed these rules?**",
    reply_markup=InlineKeyboardMarkup(keyboard),
    parse_mode='Markdown'
)

async def handle_rule_confirmation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the confirmation that the user has followed the rules."""
    query = update.callback_query
    await query.answer()
    option = query.data.split("_", 1)[1]

    # Ask the user to send their post link
    await query.message.reply_text(
    "🔗 **Please send your post link:**",
    parse_mode='Markdown'
)

    context.user_data["option"] = option
    context.user_data["awaiting_post_link"] = True

async def handle_post_link(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the receipt of the post link."""
    if context.user_data.get("awaiting_post_link"):
        post_link = update.message.text
        option = context.user_data["option"]

        # Check if the link starts with 'https://'
        if not post_link.startswith("https://"):
            await update.message.reply_text("Sorry 😭!! , Please provide the correct link!! ")
            return

        # Show the task processing message
        await update.message.reply_text(
            "Your task is in process, you will get the result in 3-4 hours.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text=" ⌛ ⌛Research in progress ⌛ ⌛ ", callback_data="in_progress")]
            ])
        )
                # Send the sticker
        await update.message.reply_sticker(sticker='CAACAgUAAxkBAAICNWaufUNuk76GBxxiMu7iYU8FQUviAAJHDwACSil4VQ8kt4YTSHQYNQQ')

        # Clear the waiting state
        context.user_data["awaiting_post_link"] = False
        logger.info(f"Post link received: {post_link}, Option: {option}")

async def handle_viral(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the /viral command and checks channel membership."""
    user_id = update.effective_user.id
    all_joined = True

    try:
        for url, channel_id in JOIN_CHANNELS:
            member = await context.bot.get_chat_member(chat_id=channel_id, user_id=user_id)
            if member.status not in ['member', 'administrator', 'creator']:
                all_joined = False
                break

        if all_joined:
            # Provide platform choices if user is a member
            keyboard = [
                [InlineKeyboardButton(text="📸 📸  Instagram  📸 📸", callback_data="instagram")],
                [InlineKeyboardButton(text="▶️ ▶️ YouTube ▶️ ▶️", callback_data="youtube")]
            ]
            await update.message.reply_text("Thanks for joining us! 📲 Ready to choose a platform that could go viral? Let’s dive in!", reply_markup=InlineKeyboardMarkup(keyboard))
        else:
            # Prompt the user to join the channels
            join_channel_keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton(text="-----👉 Join Channel 1 👈-----", url=JOIN_CHANNELS[0][0])],
                [InlineKeyboardButton(text="-----👉 Join Channel 2 👈-----", url=JOIN_CHANNELS[1][0])],
                [InlineKeyboardButton(text="-----👉 Join Channel 3 👈-----", url=JOIN_CHANNELS[2][0])],
                [InlineKeyboardButton(text="-----👉 Join Channel 4 👈-----", url=JOIN_CHANNELS[3][0])],
                [InlineKeyboardButton(text="I have joined all channels", callback_data="joined_check")]
            ])
            await update.message.reply_text("Sorry 😭,!!You need to join all our channels to access premium features. Please join the channels first:", reply_markup=join_channel_keyboard)
    except BadRequest as e:
        if str(e) == 'Chat not found':
            await update.message.reply_text("There was an error checking your channel membership. Please ensure you have joined the channels.")
        else:
            logger.error(f"Error checking channel membership: {e}")
            await update.message.reply_text("There was an error checking your channel membership. Please try again later.")

async def handle_random_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Replies to any random text message with a join channel prompt."""
    logger.info(f"Random message received: {update.message.text}")
    join_channel_keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="-----👉 Join Channel 1 👈-----", url=JOIN_CHANNELS[0][0])],
        [InlineKeyboardButton(text="-----👉 Join Channel 2 👈-----", url=JOIN_CHANNELS[1][0])],
        [InlineKeyboardButton(text="-----👉 Join Channel 3 👈-----", url=JOIN_CHANNELS[2][0])],
        [InlineKeyboardButton(text="-----👉 Join Channel 4 👈-----", url=JOIN_CHANNELS[3][0])]
    ])
    await update.message.reply_text(
        "Please join our channels to access premium features:",
        reply_markup=join_channel_keyboard
    )

async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the /clear command to reset the state and provide a join channel prompt."""
    user_id = update.effective_user.id
    
    # Reset any user data
    context.user_data.clear()
    
    # Send a message asking the user to join the channels
    join_channel_keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="-----👉 Join Channel 1 👈-----", url=JOIN_CHANNELS[0][0])],
        [InlineKeyboardButton(text="-----👉 Join Channel 2 👈-----", url=JOIN_CHANNELS[1][0])],
        [InlineKeyboardButton(text="-----👉 Join Channel 3 👈-----", url=JOIN_CHANNELS[2][0])],
        [InlineKeyboardButton(text="-----👉 Join Channel 4 👈-----", url=JOIN_CHANNELS[3][0])]
    ])

    await update.message.reply_text(
        "All previous interactions have been cleared. Please join our channels to start fresh to viral your content 📈:",
        reply_markup=join_channel_keyboard
    )
        
    # Send the additional message with instructions
    await update.message.reply_text(
        "💀 Please join the following channels to access premium bot features 💀\n\n"
        "🤖 After joining the channels, click here\n"
        "----------👉 /viral 👈---------\n"
        "to access premium features 🤖"
    )

def main() -> None:
    """Run the bot."""
    persistence = PicklePersistence(filepath="viralo_bot")
    application = (
        Application.builder()
        .token("7209425858:AAFBulAAaom02yCU6d5oP0ZLztGwBq_IvxM")
        .persistence(persistence)
        .arbitrary_callback_data(True)
        .build()
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("viral", handle_viral))
    application.add_handler(CommandHandler("clear", clear))

    application.add_handler(CallbackQueryHandler(handle_join_check, pattern="^joined_check$"))
    application.add_handler(CallbackQueryHandler(handle_platform_choice, pattern="^(instagram|youtube)$"))
    application.add_handler(CallbackQueryHandler(handle_option_choice, pattern="^(insta_|yt_)"))
    application.add_handler(CallbackQueryHandler(handle_rule_confirmation, pattern="^confirm_"))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_post_link))  # Handle post link before random messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_random_message))  # General message handler for random texts

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
