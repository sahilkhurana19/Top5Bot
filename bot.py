from telegram.ext import Updater, CommandHandler
import telegram
import logging
import feedparser

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(token = '259123812:AAEDFd5tNT3pOwPzxlC3Z6Kyx7L69qJFs5U')
dispatcher = updater.dispatcher


def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="Hi!! I am a Bot made for getting various Top 5 Listings. I will be continuously updated with New Listings so keep a check on me.")

"""
Function for getting news from the RSS Feed of Times Of India
and displaying the title and its description.
"""

def news(bot, update):
	feed = feedparser.parse('http://timesofindia.indiatimes.com/rssfeeds/1221656.cms')
	for i in range(5):
		title = feed.entries[i].title
		description = feed.entries[i].description
		bot.sendMessage(chat_id=update.message.chat_id, text="<b>" + title + "</b>" + "\n\n" + description, parse_mode = telegram.ParseMode.HTML)

start_handler = CommandHandler('start', start)
news_handler = CommandHandler('topnews', news)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(news_handler)

updater.start_polling()