
import unittest
from speechApp import Text
import nltk 



def main():

	text = Text()
	text.setText("The Pepsi Center is a massive stadium, do you not think")
	text.tokenize()
	diversity = text.lexicalDiversity()
	print(diversity)
	print(text.mostCommon())
	print(text.wordConcentration("hundred"))
	print(text.kincaid())
	print(text.flesch())
	print(text.lexicalDensity())
	print(text.namedEntities())
main()
##class TestspeechApp(unittest.TestCase):

