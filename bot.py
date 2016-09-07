from telegram.ext import Updater, CommandHandler
import telegram
import logging
import feedparser
import requests
import json

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

def songs(bot,update):
	url = 'https://api.spotify.com/v1/users/spotify/playlists/5FJXhjdILmRA2z5bvz4nzf/tracks?limit=5'
	headers = {'Authorization': 'Bearer BQAUTshSZjK_TgBhbZeF4KiSO6ZvLlR11piUXpOFtYyIoGgWNIZF3Uw1tbYB7s3WPdBT8nCiWY1UT3gBlsurah7OtS2ILhDekdOO9pxNil843GzA6fyLmfIoo524AR0aRcl0kdMqLeP2g_Q8VJNjKLRt0q-2N8XVZ0xg2om7'}
	r = requests.get(url, headers=headers)
	
	#url = 'https://api.spotify.com/v1/users/spotify/playlists/5FJXhjdILmRA2z5bvz4nzf/tracks?limit=5'
	#headers = {'Authorization': 'Bearer BQAUTshSZjK_TgBhbZeF4KiSO6ZvLlR11piUXpOFtYyIoGgWNIZF3Uw1tbYB7s3WPdBT8nCiWY1UT3gBlsurah7OtS2ILhDekdOO9pxNil843GzA6fyLmfIoo524AR0aRcl0kdMqLeP2g_Q8VJNjKLRt0q-2N8XVZ0xg2om7'}

	#r = requests.get(url, headers=headers)
	print(r)
	data = r.json()
	for i in range(5):
		songName = data["items"][i]["track"]["name"]
		artitstName = data["items"][i]["track"]["artists"][i]["name"]
		previewUrl = data["items"][i]["track"]["preview_url"]
		bot.sendMessage(chat_id=update.message.chat_id, text = songName + "\n" + artitstName + "\n" + previewUrl)
	

start_handler = CommandHandler('start', start)
news_handler = CommandHandler('topnews', news)
songs_handler = CommandHandler('topsongs', songs)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(news_handler)
dispatcher.add_handler(songs_handler)

updater.start_polling()