###import statDisplay as sD
from apiHandler import Genius
import json
from speechApp import Text
import matplotlib.pyplot as plt

def main():

	genius = Genius()

	hits = genius.search("waves")
	# for hit in hits:
	# 	print(hit["result"]["full_title"])

	chooseSong(hits[0]["result"])


def chooseSong(selection):
	genius = Genius()
	metadata = genius.songMetadata(genius.songPath(selection))
	print(metadata["Description"])
	lyricString = genius.lyrics_from_song_api_path(genius.songPath(selection))
	print(lyricString)

	Alist = genius.annotationsGetter(metadata["id"])
	print(genius.getAnnotation(Alist[7]))

	text = Text()
	text.setText(lyricString)
	text.tokenize()
	diversity = text.lexicalDiversity()
	print(diversity)
	most_common = text.mostCommon()
	print(most_common)
	print(text.wordConcentration("wave"))
	print(text.kincaid())
	print(text.flesch())
	print(text.lexicalDensity())
	##print(text.namedEntities())

	print(len(lyricString))
	print(len(text.tokens))
	print(len(text.text))

	##sD.pieChartTop10(most_common, "Waves - Kanye West").show()



main()