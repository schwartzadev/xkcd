#!/usr/bin/env python

from urllib.request import urlopen
from random import randint
import urllib.error
from os import system
import re


class Comic:
	totalComics = 0
	def getImgUrl(self, num):
		try:
			url = 'https://xkcd.com/' + str(num)
			html = urlopen(url)
			htmlstr = html.read().decode('utf-8')
			search = re.search('https:\/\/imgs\.xkcd\.com\/comics\/(.*)\.(png|jpg|gif)',  htmlstr)
			return search.group(0) # get first find in the search
		except AttributeError:
			return('no link - try troubleshooting at https://xkcd.com/' + str(num))
		except urllib.error.HTTPError:
			return('HTTP Error (this is probably either comic #404 or a connectivity issue)')

	def printUrls(self, start, finish):
		print('%d comics total' % (self.totalComics))
		for i in range(start, finish):
			print('%d : %s' % (i,self.getImgUrl(i)))

	def saveImg(self, num):
		url = self.getImgUrl(num)
		f = open('img/' + str(num) + '.png','wb')
		try:
			f.write(urlopen(url).read())
			print('saved #%d' %(num))
		except Exception as e:
			print('%s (#%d)' % (url, num))
		f.close()

	def saveAll(self):
		for i in range(1, self.totalComics+1):
			self.saveImg(i)

	def randomComicNum(self):
		return randint(1, self.totalComics)

	def __init__(self):
		# set total num of comics
		html = urlopen('https://xkcd.com/')
		htmlstr = html.read().decode('utf-8')
		search = re.search('https:\/\/xkcd\.com\/[0-9]*\/',  htmlstr)
		url = search.group(0)
		self.totalComics = int(re.findall('\d+', url)[0])

	def openComic(self, num): # windows only afaik
		system('start img/' + str(num) + '.png')

c = Comic()

# # get a random comic, get it's url
# n = c.randomComicNum()
# print(n)
# print(c.getImgUrl(n))


# get random comic, download, open in Windows
n = c.randomComicNum()
c.saveImg(n)
c.openComic(n)


# # print all comic urls
# c.printUrls(0,c.totalComics+1)
# c.saveAll()

# Bad comics:
# 404, 1037, 1193, 1608, 1663