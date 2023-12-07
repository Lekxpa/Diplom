from telegram.ext import ApplicationBuilder, CommandHandler
import package.bot
import package.set


app = ApplicationBuilder().token(package.set.Tok_adm.token).build()


app.add_handler(CommandHandler("start", package.bot.start))
app.add_handler(CommandHandler("menu", package.bot.menu))
app.add_handler(CommandHandler("about_us", package.bot.about))
app.add_handler(CommandHandler("services", package.bot.services))
app.add_handler(CommandHandler("portfolio", package.bot.portfolio))
app.add_handler(CommandHandler("price", package.bot.price))
app.add_handler(CommandHandler("contacts", package.bot.contacts))
app.add_handler(CommandHandler("more_information", package.bot.information))
app.add_handler(CommandHandler("send_request", package.bot.send_request))
app.add_handler(CommandHandler("request", package.bot.request))
app.add_handler(CommandHandler("get_presentation", package.bot.get_presentation))
app.add_handler(CommandHandler("call", package.bot.call))


app.run_polling()