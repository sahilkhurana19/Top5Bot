from telegram.ext import Updater, CommandHandler
import logging

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(token = '259123812:AAEDFd5tNT3pOwPzxlC3Z6Kyx7L69qJFs5U')
dispatcher = updater.dispatcher

def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="Hi!! I am Bot made for getting various Top 5 Listings. I will be continuously updated with New Listings so keep a check on me.")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()