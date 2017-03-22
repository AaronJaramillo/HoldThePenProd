###SEARCH MODULE
from .ProfileSheet import ProfileSheet as ps
from .apiHandler import Genius

class API:

	def runSearch(self, searchString):
		hitList = Genius().search(searchString)
		self.showList(hitList)
		return hitList

	def showList(self, hitList):
		self.resultList = []
		#self.api_pathList = []
		for hit in hitList:
			self.resultList.append(tuple((hit["result"]["full_title"], hit["result"]["api_path"])))
			#self.api_pathList.append(hit["result"]["api_path"])

	def selection(self, path):
		profile = ps()
		profile.profileGen(path)
		return profile







