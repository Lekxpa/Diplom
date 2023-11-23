from telegram import Update
from telegram.ext import ContextTypes
import logging
import datetime
from datetime import datetime
import package.view
import package.set
import package.loggg



logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)


async def loggg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open('dates.csv', 'a', encoding = 'utf-8')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}, {datetime.now()}\n')
    file.close()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await loggg(update, context)
    await update.message.reply_animation(animation='https://usagif.com/wp-content/uploads/gify/barbie-animated-usagif-22.gif')
    await update.message.reply_text(package.view.start_msg(update))


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(package.view.about_msg())


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/about_us\n/services\n/price\n/portfolio\n/contacts\n/request')


async def information(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(package.view.information_msg())


async def services(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(package.view.services_msg())


async def portfolio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(package.view.portfolio_msg())
    

async def get_presentation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # await update.message.reply_document(document='https://docs.google.com/presentation/d/1y4Do2m-q6hxR3qADBzSi-aOHrtaYvAxNrJFVerFLrYI/edit?usp=sharing')
    # await update.message.reply_copy(copy='https://docs.google.com/presentation/d/1y4Do2m-q6hxR3qADBzSi-aOHrtaYvAxNrJFVerFLrYI/edit?usp=sharing')
    # await update.message.reply_document(document=open('package\Презентация.pdf', 'rb'))
    await update.message.reply_document(document=open('C:/Users/Asus/Desktop/Презентация.pdf', 'rb'))
    # await update.message.reply_animation(animation='https://usagif.com/wp-content/uploads/gify/barbie-animated-usagif-22.gif')
    await update.message.reply_text(f'/menu')


async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(package.view.price_msg())


async def contacts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(package.view.contacts_msg())


async def send_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
     await update.message.reply_text(f'Благодарим Вас за заявку! Мы свяжемся с Вами в ближайшее время!\n\
                    \n/menu')


async def request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Нажмите, пожалуйста, кнопку send_request,\n\
        \n/send_request\n\
        \nчтобы автоматически отправить свои данные\n\
        \n(имя и ник в Telegram)\n\
        \nнашему менеджеру,чтобы он смог связаться с Вами,\n\
        \nлибо нажмите кнопку menu для возврата в основное меню\n\
        \n/menu')
    
    file = open('request.csv', 'a', encoding = 'utf-8')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.effective_user.name}, {update.message.text}, {datetime.now()}\n')
    file.close()
    await loggg(update, context)
    

async def call(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(package.view.call())