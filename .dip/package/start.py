# from telegram import Dis
# import telegram.ext.Dispatcher

import package.commands
import package.set


async def start():
        package.commands.app.run_polling()

    # dispatch = Dispatcher(bot)
    # try:
    #     await Dispatcher
    #     await disp.package.commands.app.run_polling()

    # finally:
    #     await package.set.bot.session.close()