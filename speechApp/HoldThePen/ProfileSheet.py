from .apiHandler import Genius
import json
from .speechApp import Text
#import .statDisplay as sD
#import matplotlib.pyplot as plt

class ProfileSheet:

	def profileGen(self, apiPath):
		self.api = apiPath
		self.songInfo()
		self.lyrics()
		self.stats()

	def songInfo(self):
		self.info = Genius().songMetadata(self.api)
		self.title = self.info["Title"]
		self.fullTitle = self.info["FullTitle"]
		self.description = self.info["Description"]
		self.album = self.info["Album"]
		self.artist = self.info["Artist"]
		self.image = self.info["Image"]
		self.songId = self.info["id"]
		self.info["writers"] = [(w["name"], w["image_url"]) for w in self.info["writers"]]
		#self.info["artistPic"] = [x["image_url"] for x in self.info["writers"]]

	def lyrics(self):
		self.lyrics = Genius().lyrics_from_song_api_path(self.api)
		self.wordCount = len(self.lyrics.split())

	def stats(self):
		text = Text()
		text.setText(self.lyrics)
		self.lexicalDiversity = round(100*text.lexicalDiversity(), 2)
		self.lexicalDensity = round(100*text.lexicalDensity(), 2)
		self.mostCommon = text.mostCommon()
		self.mostCommonContext = text.mostCommonContent()
		self.readability = text.flesch()
		self.kincaid = text.kincaid()
		self.wordCount = text.wordCount()
		self.setCount = text.setCount()

	# def statDisplays(self):
	# 	self.diversityPie = sD.pieChart(self.lexicalDiverity, self.title)
	# 	self.densityPie	= sD.pieChart(self.lexicalDensity, self.title)
	# 	self.top10Pie = sD.pieChartTop10(self.mostCommon, self.wordCount, self.title)
	# 	self.top10Histogram = sD.histogramIT(self.mostCommon, self.title)

	def setAnnotations(self):
		self.annotations = Genius().annotationsGetter(self.songId)




