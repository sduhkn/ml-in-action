def loadDataet():
	postingList = [['my','dog','has','flea',\
					'problems','help','please'],
					['maybe','not','take','him',\
					'to','dog','park','stupid'],
					['my','dalmation','is','so','cute',\
					'I','love','hime'],
					['stop','posting','stupid','worthless','garbage'],
					['mr','licks','ate','my','steak','how',\
					'to','stop','him'],
					['quit','buying','worthless','dog','food','stupid']]
	classVec = [0,1,0,1,0,1]
	return postingList, classVec

def createVocabList(dataSet):
	vocaSet = set([])
	for document in dataSet:
		vocaSet = vocaSet | set(document)

	return list(vocaSet)

def setOfWords2Vec(vocabList, inputSet):
	returnVec = [0]*len(vocabList)
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)] = 1
		else:
			print "The word :{}is not int my Vocabulary".format(word)

	return returnVec

listOPosts, listClasses = loadDataet();
myVocabList = createVocabList(listOPosts)
print myVocabList