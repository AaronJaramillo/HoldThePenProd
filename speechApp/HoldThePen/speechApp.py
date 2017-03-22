import nltk 
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.corpus import cmudict, state_union
from .fleschKincaid import FK as fk
import nltk
from nltk.corpus import stopwords
import re
from nltk.tokenize import PunktSentenceTokenizer

class Text:

	def setText(self, words):
		self.text = words
		re.sub("[\(\[].*?[\)\]]", "", self.text)
		self.tokenize()

	def tokenize(self):
		stop_words = set()##stopwords.words("english")
		stop_words.update([',', "'", "[", "]", "'s", "n't",".", ":","..." ,"(", ")", "?","+", "'m", ".","!", '"', "``", "''"])
		self.words = word_tokenize(self.text)
		self.tokens = [w.lower() for w in self.words if not w.lower() in stop_words] 
		stop_words.update(stopwords.words("english"))
		self.cleanedTokens = [w.lower() for w in self.words if not w.lower() in stop_words] 
    #print(self.tokens)

	def wordCount(self):
		return len(self.tokens)
		###UNIQUE WORDS
	def setCount(self):
		return len(set(self.tokens))
####differentWords/total words
	def lexicalDiversity(self):
		return len(set(self.tokens))/len(self.tokens)
######Top 10 most common words
	def mostCommon(self):
		return nltk.FreqDist(self.tokens).most_common(10)
	def mostCommonContent(self):
		return nltk.FreqDist(self.content).most_common(10)
#####the percent of the total text a single word makes up. 
	def wordConcentration(self, word):
		return 100 * self.tokens.count(word) / len(self.tokens)

	def POStagger(self):
        #print(nltk.pos_tag(self.cleanedTokens))
		return nltk.pos_tag(self.cleanedTokens)

	def countContent(self, taggedWords):
		#self.contentWords = 0
		tagged = self.POStagger()
		contentWordstypes = ["NN", "NNS", "NNP", "NNPS", "JJ", "JJR", "JJS", "RB", "RBR", "RBS", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]
		self.content = [a for (a,b) in tagged if b in contentWordstypes]
		self.contentWords = len(self.content)
		# for (a, b) in tagged:
		# 	if b in contentWordstypes:
		# 		self.contentWords += 1

	def namedEntities(self):
		train_text = state_union.raw("2005-GWBush.txt")
		custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
		tokenized = custom_sent_tokenizer.tokenize(self.text)
		try:
			for i in tokenized:
				words = nltk.word_tokenize(i)
				tagged = nltk.pos_tag(words)
				namedEnt = nltk.ne_chunk(tagged, binary=True)
				namedEnt.draw()
				return namedEnt
		except Exception as e:
			print(str(e))


	def lexicalDensity(self):
		self.countContent(self.POStagger)
		return self.contentWords / len(self.tokens)

	def flesch(self): ##readability Score
		return fk.flesch(self.text)

	def kincaid(self): ###Grade Level
		return fk.flesch_kincaid(self.text)




	#### Named Entities ###

	#### Lexical  Density### Words that matter over total words.

#### word length frequency distribution #### -- Toggle Syllabals and Letters

