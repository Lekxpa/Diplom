# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
# import datetime


# async def loggg(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     # await update.message.reply_text(f"{datetime.now()}")
#     file = open('dates.csv', 'a', encoding = 'utf-8')
#     file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}, {datetime.now()}\n')
#     file.close()

def phone():

    phone_user = input('Укажите, пожалуйста, Ваш номер телефона в формате 79000000000: ')
    if phone_user.isdigit() and len(str(phone_user)) = 11:
        return 'kljj'
    else:
        return '8420940'

phone()