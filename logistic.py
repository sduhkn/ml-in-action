import numpy as np
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt

def generate_data():
	np.random.seed(0)
	dataSize = 200
	X2, y = datasets.make_moons(200, noise=0.20)
	X1 = np.ones(200)
	X = np.c_[X1,X2]
	return X, y

def plotFig(wei,X,y):
	weights = wei.getA()
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(X[:, 1], X[:, 2], c=y, cmap=plt.cm.winter)
	x1 = np.arange(-3.0,3.0,0.1)
	y1 = (-weights[0]-weights[1]*x1)/weights[2]
	ax.plot(x1,y1)
	plt.show()

def sigmoid(inX):
	return 1.0 / (1+np.exp(-inX))

def gradAscent(dataMatIn, classLabel):
	dataMatrix = np.mat(dataMatIn)
	labelMat = np.mat(classLabel).transpose()
	m,n = np.shape(dataMatrix)
	alpha = 0.001
	maxCycles = 500
	weights = np.ones((n,1))
	for k in range(maxCycles):
		h = sigmoid(dataMatrix*weights)
		error = (labelMat - h)
		weights = weights + alpha * dataMatrix.transpose()*error
	return weights

X,y = generate_data()
weights = gradAscent(X,y)
plotFig(weights,X,y)
print weights
