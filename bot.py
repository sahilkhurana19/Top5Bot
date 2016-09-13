from telegram.ext import Updater, CommandHandler
from bs4 import BeautifulSoup
from datetime import date
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
	feed = feedparser.parse('http://timesofindia.indiatimes.com/rssfeedstopstories.cms')
	for i in range(5):
		title = feed.entries[i].title
		description = feed.entries[i].description
		bot.sendMessage(chat_id=update.message.chat_id, text="<b>" + title + "</b>" + "\n\n" + description, parse_mode = telegram.ParseMode.HTML)


def songs(bot,update):
	url = "https://open.spotify.com/user/spotify/playlist/4hOKQuZbraPDIfaGbM3lKI"
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html,"lxml")
	songName = soup.select("[class~=track-name]")
	artistName = soup.select("[class~=artists-albums]")
	for i in range(5):
		song = songName[i].string
		link = "https://www.youtube.com/results?search_query=" + song
		bot.sendMessage(chat_id=update.message.chat_id, text='<b>' + song + '</b>' + ' by ' + artistName[i].a.get_text(), parse_mode=telegram.ParseMode.HTML)

def movies(bot, update):
	bms = "https://in.bookmyshow.com/national-capital-region-ncr"
	year = str(date.today().year)
	response = requests.get(bms)
	html = response.content
	soup = BeautifulSoup(html)
	movieName = soup.find_all("a", {"class":"__name"})
	for i in range(5):
		movieList = movieName[i].string.rsplit(" (")[0]
		movieList = movieList.replace(" ","+")
		omdb = "http://www.omdbapi.com/?t=" + movieList + "&y=" + year + "&plot=full&r=json"
		movieDetails = requests.get(omdb).json()
		bot.sendMessage(chat_id=update.message.chat_id, text="<b>" + movieName[i].string + "</b>"+ "\nActors: " + movieDetails["Actors"] + "\nPlot: " + movieDetails["Plot"], parse_mode = telegram.ParseMode.HTML)

def worldNews(bot, update):
	feed = feedparser.parse('http://timesofindia.indiatimes.com/rssfeeds/296589292.cms')
	for i in range(5):
		title = feed.entries[i].title
		description = feed.entries[i].description.rsplit("/></a>")[1]
		bot.sendMessage(chat_id=update.message.chat_id, text="<b>" + title + "</b>" + "\n\n" + description, parse_mode = telegram.ParseMode.HTML)

def sportsNews(bot, update):
	feed = feedparser.parse('http://timesofindia.indiatimes.com/rssfeeds/4719148.cms')
	for i in range(5):
		title = feed.entries[i].title
		description = feed.entries[i].description.rsplit("/></a>")[1]
		bot.sendMessage(chat_id=update.message.chat_id, text="<b>" + title + "</b>" + "\n\n" + description, parse_mode = telegram.ParseMode.HTML)


movies_handler = CommandHandler('topmovies', movies)
start_handler = CommandHandler('start', start)
news_handler = CommandHandler('topnews', news)
songs_handler = CommandHandler('topsongs', songs)
worldNews_handler = CommandHandler('topinternationalnews', worldNews)
sportsNews_handler = CommandHandler('topsportsnews', sportsNews)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(news_handler)
dispatcher.add_handler(songs_handler)
dispatcher.add_handler(movies_handler)
dispatcher.add_handler(worldNews_handler)
dispatcher.add_handler(sportsNews_handler)

updater.start_polling()