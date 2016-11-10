#!/usr/bin/python

"""
This program for calculating the expectation maximization
"""


import os
import sys
import subprocess
import re
import scipy.stats
import numpy


def dotProduct(X1, X2):
	return numpy.dot(X1 , X2)


def eclidieanDistance(X1, X2):
	return numpy.linalg.norm(X1 - X2)

##input data

path_to_inputData = "/Users/youniesmahmoud/Documents/Fall2016/datamining/hw2/AD_modified/AD_completed_no_class.arff"
path_to_SVM_Data = "/Users/youniesmahmoud/Documents/Fall2016/datamining/hw2/AD_modified/svm_names.txt"

svmData = open(path_to_SVM_Data)
DataSVM = svmData.read()
DataSVM = DataSVM.split("\n")
DataSVM = DataSVM[0:-1]

for i in range(len(DataSVM)):
	m = re.search(r'-?[0-9]+.[0-9]*', DataSVM[i])
	#print (m.group(0))
	#print (i)
	#print(DataSVM[i])
	m = float(m.group(0))
	DataSVM[i] = (abs(m), i , DataSVM[i])

DataSVM.sort(reverse = True)

DataSVM = DataSVM[0:200]


for svm in DataSVM:
	print(svm[2])

inputData = open(path_to_inputData)
Data = inputData.read()
Data = Data.split("\n")
Data = Data[0:-1]

for i in range(len(Data)):
	Data[i] = Data[i].split(',')
	#print(len(Data[i]))
	for j in range(len(Data[i])):
		Data[i][j] = float(Data[i][j].strip())
	#Data[i] = numpy.array(Data[i]) we will return here
	NewData = []
	for svm in DataSVM:
		#print(svm)
		NewData.append( Data[i][svm[1]])

	Data[i] = numpy.array(NewData)


print(len(Data))
print(len(Data[0]))

##initialize the parameter 
K = 2 #number of clusters
NFeatures = len(Data[0])
N = len(Data)
centroids = Data[0:K] # choose random data points as kmeans

C = [1] + [0] *(K-1) # all of them the same cluster in the begining
Cs = [C] * N ## assign clusters randomly



def CalculateDistances(clus1 , clus2, M1 , M2):
	distances = []
	for Xi1 in clus1:
		for Xi2 in clus2:
			distances.append(dotProduct(Xi1, Xi2))
	single = round( min(distances) , 4)
	complete = round( max(distances) , 4)
	average =  round( numpy.mean(distances) , 4)
	centroidDistance = round( dotProduct(M1 , M2) , 4)
	return [single , complete , average , centroidDistance]


def assignCluster(Xi):
	##choose the cluster
	minDistance = float('-inf')
	c = 0
	for i in range(K):
		tempDistance = dotProduct(Xi , centroids[i])
		if(tempDistance > minDistance):
			minDistance = tempDistance
			c = i
	C = [0] * K
	C[c] = 1
	return C

def updateCentroids(newClusters):
	for i in range(K):
		Mi = []
		Ni = 0
		for j in range(N):
			if( newCs[j][i] == 1 ):
				Ni += 1
				Mi.append(Data[j])
		if(Ni != 0):
			centroids[i] = numpy.mean(Mi , axis = 0)
		else:
			print ("error4")

def getXis(newClusters):
	Xis = []
	for i in range(K):
		Mi = []
		Ni = 0
		for j in range(N):
			if( newCs[j][i] == 1 ):
				Ni += 1
				Mi.append(Data[j])
			Xis.append(Mi) 

	return Xis


while True:
	print ("g")
	newCs = []
	for Xi in Data:
		newCs.append(assignCluster(Xi))
	updateCentroids(newCs)
	if(newCs == Cs):
		print("converged")
		break
	else:
		Cs = newCs






Xis = getXis(Cs)

results = []

for i in range(K):
	first = i
	second = (i+1)%K
	results.append(CalculateDistances(Xis[first] , Xis[second] , centroids[first] , centroids[second]))

for result in results:
	print(result)
print(numpy.mean(results , axis = 0))










