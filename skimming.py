from textblob import TextBlob


class Keyword:

	def __init__(self, word):
		self.word = word
		self.score = 0

	def updateScore(self, section):
		self.score =self.score + 0.1+(1/(section+1))

	def normalizeScore(self, minS, maxS):
		self.score = (self.score - minS)/(maxS - minS)

def skimming(text, section, arrayKeyword):
	blob = TextBlob(text)
	nouns = blob.noun_phrases 
	for noun in nouns:
		flag = True
		for keyword in arrayKeyword:
			if keyword.word == str(noun):
				keyword.updateScore(section)
				flag = False				
		if flag:
			newKeyword = Keyword(noun)
			newKeyword.updateScore(section)
			arrayKeyword.append(newKeyword)
	return arrayKeyword

def normalizeKeywords(arrayKeyword):
	minScore = 0.0
	maxScore = 0.0
	for keyword in arrayKeyword:
		if maxScore == 0:
			minScore = keyword.score
			maxScore = keyword.score
		else:
			if keyword.score > maxScore:
				maxScore = keyword.score
			if minScore > keyword.score:
				minScore = keyword.score
	for keyword in arrayKeyword:
		keyword.normalizeScore(minScore, maxScore)
	return arrayKeyword						

def getKeywords(filename):
	f = open(filename, 'r')
	arrayKeyword = []
	for section, text in enumerate(list(f)):
		arrayKeyword = skimming(text, section, arrayKeyword)

	return normalizeKeywords(arrayKeyword)

def topKeywords(filename, n):
	arrayKeyword = getKeywords(filename)
	retArray = []
	for x in range(0,n):
		idmax = -1
		maxScore = 0
		for idx, keyword in enumerate(arrayKeyword):
			if keyword.score > maxScore:
				maxScore = keyword.score
				idmax = idx
		retArray.append(arrayKeyword[idmax])
		arrayKeyword.remove(arrayKeyword[idmax])
	return retArray	
	

