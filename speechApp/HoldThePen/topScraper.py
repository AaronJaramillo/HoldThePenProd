import requests
from bs4 import BeautifulSoup
from .searchHandler import API

def main():
	header = {'User-Agent': 'Mozilla/5.0'}
	r = requests.get("https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_top_10_singles_in_2016", headers=header)
	html = BeautifulSoup(page.text, "html.parser")
	table = soup.find("table", { "class" : "wikitable sortable" })
	for row in table.findAll("tr"):
		cells = row.findAll("td")
		if len(cells) == 7:
			date = cells[0].find(text=True)
			singleName = cells[1].findAll(text=True)
			artist = cells[2].find(text=True)
			peak = cells[3].find(text=True)
			peakDate = cell[4].find(text=True)
			weeks = cell[5].find(text=True)
			references = cell[6].find(text=True)
	call = API()
	apiPathList = []
	for searchTerm in singleName:
		result = call.runSearch(searchTerm)
		resultList = call.resultList
		apiPathList.append(call.resultList[0][1])
	print(apiPathList)

main()

# def compare(path):
# 	#api_path = request.GET.get('path', '')
# 	api_path = path
# 	song = API().selection(api_path)
	
# 	lyricString = song.lyrics
# 	song.info["lyrics"] = lyricString
# 	song.info["lyrics"] = song.info["lyrics"].splitlines(1)
# 	song.info["diversity"] = str(song.lexicalDiversity) + "%"
# 	song.info["density"] = str(song.lexicalDensity) + "%"
# 	song.info["gradeLevel"] = round(song.kincaid, 2)
# 	song.info["readability"] = round(song.readability, 2)
# 	song.info["wordCount"] = song.wordCount
# 	song.info["setCount"] = str(song.setCount) + " / " + str(song.wordCount) 
# 	song.info["top"] = song.mostCommon[:]
# 	song.info["topContent"] = song.mostCommonContext[:]
# 	song.info["top"] = zip(song.info["top"], [round(100*(x/song.wordCount),2) for (y,x) in song.info["top"]])
# 	song.info["topContent"] = zip(song.info["topContent"], [round(100*(x/song.wordCount),2) for (y,x) in song.info["topContent"]])
# 	return song.info