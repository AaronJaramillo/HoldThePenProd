import requests
import json
from bs4 import BeautifulSoup

class Genius:

	base_url = "http://api.genius.com"
	headers = {'Authorization': 'Bearer 8Ir6ABMaTYwKsXpkJANh6c-bG2D3RTvfGv5sbCcxek0Dw1B17uv5kN3PLx05rFqf'}

	def search(self, searchString):
		search_url = self.base_url + "/search?q="
		
		search_url = search_url + searchString
		response = requests.get(search_url, headers=self.headers)
		searchInfo = response.json()
		print(searchInfo["meta"]["status"])
		return searchInfo["response"]["hits"]

	def makeCallAPI(self, song_api_path):
		song_url = self.base_url + str(song_api_path) + "?text_format=plain"
		response = requests.get(song_url, headers=self.headers)
		# json = response.json()
		# path = json["response"]["song"]["path"]
		#gotta go regular html scraping... come on Genius
		# page_url = "http://genius.com" + path
		return response

	def callReferentID(self, idString):
		song_url = self.base_url +"/referents?text_format=plain&song_id=" + idString
		response = requests.get(song_url, headers=self.headers)		
		return response.json()

	def getAnnotation(self, annote_api_path):
		annotationObject = self.makeCallAPI(annote_api_path).json()
		return annotationObject["response"]["annotation"]["body"]["plain"]


	def annotationsGetter(self, idString):
		annotationList = []
		objectJ = self.callReferentID(idString)
		for ob in objectJ["response"]["referents"]:
			for annote in ob["annotations"]:
				annotationList.append(annote["api_path"])
		return annotationList


		# if song_info: 
		#   return song_info["result"]["api_path"]
	def songPath(self, selection):
		return selection["api_path"]
		song_url = self.base_url + song_api_path + "?text_format=plain"
		response = requests.get(song_url, headers=self.headers)


	def lyrics_from_song_api_path(self, song_api_path):
		response = self.makeCallAPI(song_api_path)
		json = response.json()
		path = json["response"]["song"]["path"]
		#gotta go regular html scraping... come on Genius
		page_url = "http://genius.com" + path
		page = requests.get(page_url)
		html = BeautifulSoup(page.text, "html.parser")
		#remove script tags that they put in the middle of the lyrics
		[h.extract() for h in html('script')]
		#at least Genius is nice and has a tag called 'lyrics'!
		lyrics = html.find("div", class_="lyrics").get_text()
		return lyrics

	# def getWriters(self, writersOB):
	# 	writerList = writersOB
	# 	nameList = []
	# 	for writer in writerList:
	# 		nameList.append(writer["name"])
	# 	return nameList

	def songMetadata(self, song_api_path):
		songObject = self.makeCallAPI(song_api_path).json()
		songObject = songObject["response"]["song"]
		songMetadata = {}
		songMetadata["Title"] = songObject["title"]
		songMetadata["FullTitle"] = songObject["full_title"]
		songMetadata["Description"] = songObject["description"]["plain"]
		try:
			songMetadata["Album"] = songObject["album"]["name"]
		except:
			songMetadata["Album"] = "N/A"
		songMetadata["Artist"] = songObject["primary_artist"]["name"]
		songMetadata["Image"] = songObject["header_image_url"]
		songMetadata["id"] = str(songObject["id"])
		songMetadata["writers"] = songObject["writer_artists"]
		#print(songMetadata["Title"])
		songMetadata["Link"] = [link["url"] for link in songObject["media"] if link["provider"] == "youtube"]
		if len(songMetadata["Link"]) > 0:
			songMetadata["Link"] = songMetadata["Link"][0]
			
			songMetadata["Link"] = "http://www.youtube.com/embed/" + songMetadata["Link"].split("=")[1][0:]
			
		return songMetadata
