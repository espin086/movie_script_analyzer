#!/usr/bin/python


import sys #used to facilitate arguments in terminal
import requests #used to download web pages
from bs4 import BeautifulSoup #used to wrangle html text

if sys.argv[1] == "--h":
	print ''
	print '***************************************'
	print '************** help menu **************'
	print '***************************************'
	print ''
	print 'author: JJ Espinoza'
	print 'description: x'
	print 'created: 2017-12-13'
	print ''
	print 'commands:                 descriptions:'
	print '_______________________________________'
	print ''
	print '--h                           help menu'
	print '--plots ["url"]               scrapes movie plots'
	print '--links ["url"]               scrapes hyperlinks on page'
	print '--wikisearch ["term"]         Finds wikis'
	print '--wikiscrape ["term"]         Scrapes wikis'
	print '_______________________________________'
	print ''

#####################
if sys.argv[1] == "--links":
	url = sys.argv[2]
	#returns HTML content
	r = requests.get(url)
	#Converted into something useful
	soup = BeautifulSoup(r.content)
	#extract all hyperlinks for each link document
	for link in soup.find_all('a'):
		print(link.text, link.get('href'))

#######################
if sys.argv[1] == "--wikisearch":
	print(wikipedia.search(sys.argv[2]))
	page = wikipedia.page(sys.argv[2])
	print(wikipedia.summary(sys.argv[2]))

if sys.argv[1] == "--wikiscrape":
	page = wikipedia.page(sys.argv[2])
	print(page.title)
	print(page.url)
	print(page.content)


#######################
if sys.argv[1] == "--plots":

	#################
	#Using Beautiful Soup
	# url = sys.argv[2]
	# #returns HTML content
	# r = requests.get(url)
	# #Converted into something useful
	# soup = BeautifulSoup(r.content)
	# #extract all hyperlinks for each link document
	# g_data = soup.find_all("div", {"id": "mw-content-txt"})

	for item in g_data:
		print(item.text)









