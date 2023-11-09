from telegram import Update
from telegram.ext import ContextTypes
import logging
import datetime
from datetime import datetime
import package.view
import package.set
import package.loggg



# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level=logging.INFO)


async def loggg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # await update.message.reply_text(f"{datetime.now()}")
    file = open('dates.csv', 'a', encoding = 'utf-8')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}, {datetime.now()}\n')
    file.close()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await loggg(update, context)
    # await package.loggg.loggg(update, context)
    # markup = ReplyKeyboardMarkup(package.view.start_msg(update), resize_keyboard=False, one_time_keyboard=False, selective=False, input_field_placeholder=None)
    # btn1 = KeyboardButton("👋 Меню")
    # markup.add(btn1)
    # bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user), reply_markup=markup)
    await update.message.reply_animation(animation='https://usagif.com/wp-content/uploads/gify/barbie-animated-usagif-22.gif')
    # await update.message.reply_animation(animation=open('C:/Users/Asus/Desktop/barbie-animated-usagif-22.gif', 'rb'))
    # await update.message.reply_animation(document=open('package\barbie-animated-usagif-22.gif', 'rb')) 
    await update.message.reply_text(package.view.start_msg(update))


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(package.view.about_msg())


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/about_us\n/services\n/price\n/portfolio\n/contacts\n/send_request')
    # await update.message.reply_text(f'/about_us\n/services\n/price\n/portfolio\n/contacts\n/search_phone_number\n/send_request')


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
   


async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(package.view.price_msg())


async def contacts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(package.view.contacts_msg())


async def request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(package.view.request_msg())
    await loggg(update, context)
    # dt = update.message.text
    # print(dt)
    # if text_message = None:
    await update.message.reply_text(f'Ваша заявка принята! Мы свяжемся с Вами в указанное Вами время!\n\
    \n/menu')


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
# С этого момента создаваемый бот должен обрабатывать все получаемые текстовые сообщения,

# говорим обработчику `MessageHandler`, если увидишь текстовое 
# сообщение (фильтр `Filters.text`)  и это будет не команда 
# (фильтр ~Filters.command), то вызови функцию `echo()`
# echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
# регистрируем обработчик `echo_handler` в экземпляре `dispatcher`
# dispatcher.add_handler(echo_handler)
   

# def inline_caps(update, context):
#     query = update.inline_query.query
#     if not query:
#         return
#     results = list()
#     results.append(
#         InlineQueryResultArticle(
#             id=query.upper(),
#             title='Convert to UPPER TEXT',
#             input_message_content=InputTextMessageContent(query.upper())
#         )
#     )
#     context.bot.answer_inline_query(update.inline_query.id, results)



# from aiogram.fsm.state import StatesGroup, State

# class SendFileSteps(StatesGroup):
#     get_code_from_user = State()
    

# from aiogram.types import Message
# from package import views
# from package.utils.api_action import register_user

# async def start_command(message: Message):
#     register_user(chat_id=message.chat.id, first_name=message.from_user.first_name, last_name=message.from_user.last_name, username=message.from_user.username)
#     await message.answer(views.start_bot_msg())

# #api action
# def register_user(chat_id, first_name, last_name, username):
#     requests.post(API_URL + f"create-user/", data={'chat_id': chat_id, 'first_name': first_name, 'last_name': last_name if last_name else '', 'username': username if username else '',})




#обработчик встроенных запросов
# inline_caps_handler = InlineQueryHandler(inline_caps)
# app.add_handler(inline_caps_handler)

# обработчик текстовых сообщений
# echo_handler = MessageHandler(Filters.TEXT & (~Filters.COMMAND), echo)


#обработчик встроенных запросов
# inline_caps_handler = InlineQueryHandler(inline_caps)
# app.add_handler(inline_caps_handler)


# запуск прослушивания сообщений
# updater.start_polling()

#обработчик нажатия Ctrl + C
# updater.idle()

# def unknown(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, 
#                              text="Sorry, I didn't understand that command.")

#обработчик нераспознанных команд
# unknown_handler = MessageHandler(Filters.command, unknown)
# app.add_handler(unknown_handler)



# https://t.me/Dip_bot_bot

# if __name__ == '__main__':
#     application = ApplicationBuilder().token('TOKEN').build()
    
#     start_handler = CommandHandler('start', start)
#     application.add_handler(start_handler)
    
#     application.run_polling()


# async def msg(update, context):
#     file_to_get = await update.message.document.send_file()


#     file_path = await file_to_download.download_to_drive()
    
#     os.system(f'python {file_path} > {str(file_path)}.out 2> {str(file_path)}.error') # прочитали файл и записали его в файл hello
    
#     text_message = None
#     with open(str(file_path) +'.out') as f:
#         text_message = f.read()

#     if text_message == '':
#         with open(str(file_path) + '.error') as f:
#             text_message = f.read()

#     if text_message == '':
#         text_message = 'Nothing to output'

#     # print(type(file_path))
#     # print(file_path)
#     await update.message.reply_text(text_message)
#     # await update.message.reply_text(str(file_path))
         
# # async def callback(update: Update, context: CallbackContext)