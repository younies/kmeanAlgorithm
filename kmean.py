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




def eclidieanDistance(X1, X2):
	return numpy.linalg.norm(X1 - X2)

##input data

path_to_inputData = ""

inputData = open(path_to_inputData)
Data = inputData.read()
Data = Data.split("\n")
Data = Data[0:-1]

for i in range(len(Data)):
	Data[i] = Data[i].aplit(";")
	for j in len(Data[i]):
		Data[i][j] = float(Data[i][j].strip())
