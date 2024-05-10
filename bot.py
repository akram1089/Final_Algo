import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes,CommandHandler
API_KEY = '7121001803:AAEX63j9seqXmxZwVjdaoOPhhZV1jC7GqsE'
logging.basicConfig(
    format='% (asctime)s - % (name)s - %(levelname)s - %(message',
    level=logging.INFO
    )
async def start (update: Update, context: ContextTypes. DEFAULT_TYPE):
    await context.bot.send_message(
    chat_id=update.effective_chat.id,
    text="I'm a bot, please talk to me!")
if __name__ == '_main__':
    application = ApplicationBuilder().token (API_KEY).build
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.run_polling()