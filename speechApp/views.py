# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from speechApp.forms import searchBar
from .HoldThePen.searchHandler import API
import random

def index(request):
	features = ['/songs/2874239', '/songs/576123', '/songs/437103', '/songs/720401', '/songs/496445', '/songs/453', '/songs/474036', '/songs/542389', '/songs/1743010', '/songs/2386385', '/songs/727466', '/songs/644712', '/songs/729458', '/songs/665379', '/songs/226866', '/songs/1866151', '/songs/715223', '/songs/720259', '/songs/499725', '/songs/713548', '/songs/591746', '/songs/696428', '/songs/548094', '/songs/2423196', '/songs/573451', '/songs/572029', '/songs/336227', '/songs/2129514', '/songs/471152', '/songs/2450579', '/songs/2263723', '/songs/2137030', '/songs/503256', '/songs/2286779', '/songs/451776', '/songs/2332455', '/songs/724693', '/songs/518089', '/songs/299338', '/songs/579177', '/songs/2156106', '/songs/655148', '/songs/70324', '/songs/515319', '/songs/1783757', '/songs/547828', '/songs/401425', '/songs/2866720', '/songs/2372707', '/songs/658724', '/songs/731073', '/songs/1967201', '/songs/230407', '/songs/2158461', '/songs/1779228', '/songs/461944', '/songs/501510', '/songs/551256', '/songs/387414', '/songs/192879', '/songs/663713', '/songs/2457254', '/songs/570363', '/songs/547812', '/songs/671181', '/songs/2268553', '/songs/622818', '/songs/2314529', '/songs/2458848', '/songs/2153759', '/songs/507478', '/songs/245054', '/songs/709741', '/songs/694659', '/songs/513887', '/songs/706298', '/songs/527546', '/songs/382949', '/songs/115612', '/songs/539654', '/songs/2254724', '/songs/183538', '/songs/494172', '/songs/2263487', '/songs/1593', '/songs/54003', '/songs/640182', '/songs/1863307', '/songs/693878', '/songs/344880', '/songs/378195', '/songs/668175', '/songs/90473', '/songs/1883014', '/songs/1778100', '/songs/2412668', '/songs/2295118', '/songs/164574', '/songs/567753', '/songs/2266961', '/songs/2158086']
	featureList = []
	featureList.append({"Title": "Title", "Artist": "Artist", "setCount": "Unique Words / Total Words", "diversity": "Lexical Diversity", "density": "Lexical Density", "gradeLevel": "Grade Level", "readability": "Readability Score", "id": "id", "Image": "https://images.rapgenius.com/a1a2c1072ecc2551b68aea8b1b76c9d4.512x512x1.png"})
	for x in range(4):
		featureList.append(compare(features[random.randrange(0, len(features))]))
	return render(request, 'home.html', {'playlist': featureList})

def search(request):
   if request.method == "POST":
      #Get the posted form
      mySearch = searchBar(request.POST)
      mySearch.is_valid()
      call = API()
      searchTerm = mySearch.cleaned_data["searchString"]
      result = call.runSearch(searchTerm)
      resultList = call.resultList
      return render(request, 'searchResult.html', {"hits": resultList})

def profile(request):
	api_path = request.GET.get('path', '')

	song = API().selection(api_path)
	
	lyricString = song.lyrics
	song.info["lyrics"] = lyricString
	song.info["lyrics"] = song.info["lyrics"].splitlines(1)
	song.info["diversity"] = str(song.lexicalDiversity) + "%"
	song.info["density"] = str(song.lexicalDensity) + "%"
	song.info["gradeLevel"] = round(song.kincaid, 2)
	song.info["readability"] = round(song.readability, 2)
	song.info["wordCount"] = song.wordCount
	song.info["setCount"] = str(song.setCount) + " / " + str(song.wordCount) 
	song.info["top"] = song.mostCommon[:]
	song.info["topContent"] = song.mostCommonContext[:]
	song.info["top"] = zip(song.info["top"], [round(100*(x/song.wordCount),2) for (y,x) in song.info["top"]])
	song.info["topContent"] = zip(song.info["topContent"], [round(100*(x/song.wordCount),2) for (y,x) in song.info["topContent"]])
	#print(song.info["top"])
	# for line in song.info["lyrics"]:
	# 	if line[0] =='[':
	# 		song.info["lyrics"].insert((song.info["lyrics"].index(line)-1),"<br>")
	# line.replace('\n', '<br>') #for line in song.info["lyrics"]]


	return render(request, 'profile.html', song.info)


def compare(path):
	#api_path = request.GET.get('path', '')
	api_path = path
	song = API().selection(api_path)
	
	lyricString = song.lyrics
	song.info["lyrics"] = lyricString
	song.info["lyrics"] = song.info["lyrics"].splitlines(1)
	song.info["diversity"] = str(song.lexicalDiversity) + "%"
	song.info["density"] = str(song.lexicalDensity) + "%"
	song.info["gradeLevel"] = round(song.kincaid, 2)
	song.info["readability"] = round(song.readability, 2)
	song.info["wordCount"] = song.wordCount
	song.info["setCount"] = str(song.setCount) + " / " + str(song.wordCount) 
	song.info["top"] = song.mostCommon[:]
	song.info["topContent"] = song.mostCommonContext[:]
	song.info["top"] = zip(song.info["top"], [round(100*(x/song.wordCount),2) for (y,x) in song.info["top"]])
	song.info["topContent"] = zip(song.info["topContent"], [round(100*(x/song.wordCount),2) for (y,x) in song.info["topContent"]])
	return song.info
