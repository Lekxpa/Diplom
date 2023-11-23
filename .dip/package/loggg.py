from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime


async def loggg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open('dates.csv', 'a', encoding = 'utf-8')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}, {datetime.now()}\n')
    file.close()