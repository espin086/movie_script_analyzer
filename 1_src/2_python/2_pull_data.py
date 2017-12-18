#!/usr/bin/python


import sys #used to facilitate arguments in terminal
import requests
from bs4 import BeautifulSoup

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
	print '--links ["url"]               scrapes hyperlinks on page'
	print '--plots ["url"]               scrapes movie plots'
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
if sys.argv[1] == "--plots":
	url = sys.argv[2]
	#returns HTML content
	r = requests.get(url)
	#Converted into something useful
	soup = BeautifulSoup(r.content)
	#extract all hyperlinks for each link document
	g_data = soup.find_all("div", {"id": "mw-content-txt"})

	for item in g_data:
		print(item.text)









