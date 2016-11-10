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

path_to_inputData = ""
path_to_SVM_Data = ""

svmData = open(path_to_SVM_Data)
DataSVM = svmData.read()
DataSVM = DataSVM.split("\n")
DataSVM = DataSVM[0:-1]




for i in range(len(DataSVM)):
	m1 = re.search('\+?-?', DataSVM[i])
	m2 = re.search('[0-9]+.[0-9]*', DataSVM[i])
	m3 = re.search('<.*>', DataSVM[i])
	#print (m.group(0))
	#print (i)
	#print(DataSVM[i])
	DataSVM[i] = (float(m2.group(0)), m3.group(0) )




weightRange = [1.0 , 0.99]


for svm in DataSVM:
	if(svm[0] <= weightRange[0] and svm[0] >= weightRange[1]):
		print(svm[1])











