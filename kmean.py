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


def dotProduct():
	return numpy.dot(X1 , X2)


def eclidieanDistance(X1, X2):
	return numpy.linalg.norm(X1 - X2)

##input data

path_to_inputData = "/Users/youniesmahmoud/Documents/Fall2016/datamining/hw2/AD_modified/AD_200_no_class_info.arff"

inputData = open(path_to_inputData)
Data = inputData.read()
Data = Data.split("\n")
Data = Data[0:-1]

for i in range(len(Data)):
	Data[i] = Data[i].split(',')
	print(len(Data[i]))
	for j in range(len(Data[i])):
		Data[i][j] = float(Data[i][j].strip())
	Data[i] = numpy.array(Data[i])




##initialize the parameter 
K = 3 #number of clusters
NFeatures = len(Data[0])
N = len(Data)
centroids = Data[0:K] # choose random data points as kmeans

C = [1] + [0] *(K-1) # all of them the same cluster in the begining
Cs = [C] * N ## assign clusters randomly



def assignCluster(Xi):
	##choose the cluster
	minDistance = float('inf')
	c = 0
	for i in range(K):
		tempDistance = eclidieanDistance(Xi , centroids[i])
		if(tempDistance < minDistance):
			minDistance = tempDistance
			c = i
	C = [0] * K
	C[c] = 1
	return C

def updateCentroids(newClusters):
	for i in range(K):
		Mi = []
		Ni = 0
		print(len(newCs))
		print(len(newCs[0]))

		for j in range(N):
			if( newCs[j][i] == 1 ):
				Ni += 1
				Mi.append(Data[j])
		if(Ni != 0):
			centroids[i] = numpy.mean(Mi , axis = 0)
		else:
			print ("error")




while True:
	newCs = []
	for Xi in Data:
		newCs.append(assignCluster(Xi))
	updateCentroids(newCs)
	if(newCs == Cs):
		print("converged")
		break
	else:
		Cs = newCs


def distances( centroid):
	ret = []
	for cent in centroids:
		ret.append(eclidieanDistance(centroid,cent))
	return ret


for centroid in centroids:
	print(distances(sum(centroid)))