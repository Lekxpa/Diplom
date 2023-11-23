# from telegram import Dis
# import telegram.ext.Dispatcher

import package.commands
import package.set


async def start():
        package.commands.app.run_polling()