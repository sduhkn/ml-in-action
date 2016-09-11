import numpy as np
import operator

def createDataSet():
	group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = np.array(['A','A','B','B'])
	return group, labels

def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	## calculate the distance
	diffMat = np.tile(inX, (dataSetSize,1)) - dataSet
	print "diffMat:{}".format(diffMat)
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances ** 0.5
	print distances
	sortedDistIndicies = distances.argsort()
	print "sortedDistIndicies:{}".format(sortedDistIndicies)
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		print "voteIlabel:{}".format(voteIlabel)
		classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
		sortedClassCount = sorted(classCount.iteritems(),
			key=operator.itemgetter(1), reverse=True)
		return sortedClassCount[0][0]

group, labels = createDataSet()
class1 = classify0(np.array([0,0]), group, labels, 3)
print class1