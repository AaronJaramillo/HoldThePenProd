###statDisplay
import matplotlib.pyplot as plt
from speechApp import Text
from apiHandler import Genius

def pieChart(ratio, title):
	slices = [ratio, (1-ratio)]
	activities = ['Unique Words','Reapeated Words']
	cols = ['c','r']

	plt.pie(slices,
	labels=activities,
	colors=cols,
	startangle=90,
	shadow= True,
	#explode=(0,0.1,0,0),
	autopct='%1.1f%%')

	plt.title(title)
	return plt
	##plt.show()

#pieChart(0.39, "Lexical Diversity")

def pieChartTop10(mostCommon, total, title):
	counts = []
	words = []
	for (a, b) in mostCommon:
		words.append(a)
		counts.append(b)
	aggregate = 0
	for x in counts:
		aggregate = aggregate + x

	remaining = total - aggregate

	counts.append(remaining)
	words.append("remaining")
	plt.pie(counts,
	labels=words,
	startangle=90,
	shadow= True,
	#explode=(0,0.1,0,0),
	autopct='%1.1f%%')

	plt.title(title)
	return plt
	##plt.show()
	###return plt
def histogramIT(mostCommon, title):
	counts = []
	words = []
	for (a, b) in mostCommon:
		words.append(a)
		counts.append(b)
	width = 0.35
	ind = range(10)
	fig, ax = plt.subplots()
#	plt.bar(range(10), counts, color='g')
	ax.bar(range(10), counts, color='g')
	ax.legend()

	plt.xlabel('Word')
	plt.ylabel('Frequency')
	ax.set_xticks(ind)
	ax.set_xticklabels(words)
	plt.title(title)

	return plt
	##plt.show()

##histogramIT([("n't", 14), ('do', 12), ('I', 12), ('the', 11), ('me', 9), ('lie', 8), ('No', 8), (']', 7), ('[', 7), ('up', 6)], "Kanye West - Waves")










