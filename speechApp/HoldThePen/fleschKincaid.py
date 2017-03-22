##Python
from nltk.corpus import cmudict
from nltk.tokenize import sent_tokenize, word_tokenize
import re
class FK:



  # not_punctuation = ##lambda w: not (len(w)==1 and (not w.isalpha()))

  # stop_words = set()
  # stop_words.update([',', "'", "[", "]", "'s", "n't", ":", "(", ")", "?", "'m" ])
  # words = word_tokenize(text)
  # tokens = [w for w in words if not w.lower() in stop_words]

  # get_word_count = len(tokens) ##lambda text: len(list(filter(FK.not_punctuation, word_tokenize(text))))
  # get_sent_count = len(sent_tokenize(text.replace("\n", ".")))##lambda text: len(sent_tokenize(text.replace('\n', ".")))


  prondict = cmudict.dict()

  #numsyllables_pronlist = lambda l: len(list(filter(lambda s: s.lower()[-1].isdigit(), l)))


  def numsyllables(word):
    count = 0
    word = word.lower()
    if word in FK.prondict:
      pron = FK.prondict[word]
      for syl in pron[0]:
        if syl[-1].isdigit():
          count += 1
      return count
    else:
        count = 1
        return count


  def text_statistics(text):
    ##re.sub("[\(\[].*?[\)\]]", "", text)
    stop_words = set()
    stop_words.update([',', "'", "[", "]", "'s", "n't", ":", "(", ")", "?", "'m", "." ])
    words = word_tokenize(text)
    tokens = [w for w in words if not w.lower() in stop_words]

    word_count = len(tokens) ##lambda text: len(list(filter(FK.not_punctuation, word_tokenize(text))))
    sents = sent_tokenize(text.replace("\n", ". "))
    sentences = [s for s in sents if not s[0] in stop_words]
    sent_count = len(sentences)
    #print(sentences)
    # word_count = FK.get_word_count(text)
    # sent_count = FK.get_sent_count(text)
    syllable_count = 0
    for w in tokens:
      syllable_count = syllable_count + FK.numsyllables(w)
    # syllable_count = sum(map(lambda w: max(FK.numsyllables(w)), tokens))
    return word_count, sent_count, syllable_count


  #flesch_formula = lambda word_count, sent_count, syllable_count : 206.835 - 1.015*word_count/sent_count - 84.6*syllable_count/word_count
  def flesch(text):
    word_count, sent_count, syllable_count = FK.text_statistics(text)
    readability = 206.835 - 1.015*(word_count/sent_count) - 84.6*(syllable_count/word_count)
    return readability #FK.flesch_formula(word_count, sent_count, syllable_count)
   
 # fk_formula = lambda word_count, sent_count, syllable_count : 0.39 * word_count / sent_count + 11.8 * syllable_count / word_count - 15.59
  def flesch_kincaid(text):
    word_count, sent_count, syllable_count = FK.text_statistics(text)
    grade = 0.39 * (word_count / sent_count) + 11.8 * (syllable_count / word_count) - 15.59
    return grade ##FK.fk_formula(word_count, sent_count, syllable_count)


