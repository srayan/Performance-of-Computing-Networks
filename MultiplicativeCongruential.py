##################################################################
# Performance of Computer Networks 
# CS 6352 HomeWork 1, Question.3.
# @Author: srayan.guhathakurta@utdallas.edu
##################################################################



#!/usr/bin/python
import sys, os
import numpy

# Respective values of k, m and Seed value S[0] in sList
k = 16807
m = 2147483647
sList = [1111]
rList=[]
numIndex = 0
i = 0

# Initializing arrays for calculation of the number of intervals in the ranges
interval1 =  []
interval2 =  []
interval3 =  []
interval4 =  []
interval5 =  []
interval6 =  []
interval7 =  []
interval8 =  []
interval9 =  []
interval10 = []

# Generation of uniformly distributed pseudo-random numbers using Multiplicative congruential method
# Populating the S list/array for 10000 iterations
while len(sList) < 10000:
	Sn = (k * sList[-1]) % m
	sList.append(Sn)
	
#print (sList)

# Populating the sequence of uniformly distributed pseudo-random numbers
while numIndex < 10000:
	Rn = sList[numIndex] / float(m)
	rList.append(Rn)
	numIndex = numIndex + 1

#print (rList)

# Print out statements
# Type casting to append number with string in print statement
totNumS = len(sList)
str(totNumS)
totNumS_str = str(totNumS)
#print "Total number of entries in the sList: " +(totNumS_str)

totNumR = len(rList)
str(totNumR)
totNumR_str = str(totNumR)
#print "Total number of entries in the rList: " +(totNumR_str)


# Counting the number of outcomes
# Calculate the number of intervals in-between (0-0.1); (0.1-0.2); ... (0.9-1.0)
for i in range (len(rList)):
	if rList[i] >= 0 and rList[i] <=0.1:
		interval1.append(rList[i])

	if rList[i] > 0.1 and rList[i] <=0.2:
		interval2.append(rList[i])

	if rList[i] > 0.2 and rList[i] <=0.3:
		interval3.append(rList[i])

	if rList[i] > 0.3 and rList[i] <=0.4:
		interval4.append(rList[i])

	if rList[i] > 0.4 and rList[i] <=0.5:
		interval5.append(rList[i])

	if rList[i] > 0.5 and rList[i] <=0.6:
		interval6.append(rList[i])

	if rList[i] > 0.6 and rList[i] <=0.7:
		interval7.append(rList[i])

	if rList[i] > 0.7 and rList[i] <=0.8:
		interval8.append(rList[i])

	if rList[i] > 0.8 and rList[i] <=0.9:
		interval9.append(rList[i])

	if rList[i] > 0.9 and rList[i] <=1.0:
		interval10.append(rList[i])


# Printing the output to the number of outcomes in the intervals
totNum1 = len(interval1)
str(totNum1)
totNum1_str = str(totNum1)
print "[0, 0.1]: " +(totNum1_str)

totNum2 = len(interval2)
str(totNum2)
totNum2_str = str(totNum2)
print "[0.1, 0.2]: " +(totNum2_str)

totNum3 = len(interval3)
str(totNum3)
totNum3_str = str(totNum3)
print "[0.2, 0.3]: " +(totNum3_str)

totNum4 = len(interval4)
str(totNum4)
totNum4_str = str(totNum4)
print "[0.3, 0.4]: " +(totNum4_str)

totNum5 = len(interval5)
str(totNum5)
totNum5_str = str(totNum5)
print "[0.4, 0.5]: " +(totNum5_str)

totNum6 = len(interval6)
str(totNum6)
totNum6_str = str(totNum6)
print "[0.5, 0.6]: " +(totNum6_str)

totNum7 = len(interval7)
str(totNum7)
totNum7_str = str(totNum7)
print "[0.6, 0.7]: " +(totNum7_str)

totNum8 = len(interval8)
str(totNum8)
totNum8_str = str(totNum8)
print "[0.7, 0.8]: " +(totNum8_str)

totNum9 = len(interval9)
str(totNum9)
totNum9_str = str(totNum9)
print "[0.8, 0.9]: " +(totNum9_str)

totNum10 = len(interval10)
str(totNum10)
totNum10_str = str(totNum10)
print "[0.9, 1.0]: " +(totNum10_str)



# Calculate mean and variance
mean = numpy.mean(rList)
str(mean)
mean_str = str(mean)
print "The mean is : " +(mean_str)

variance = numpy.var(rList)
str(variance)
variance_str = str(variance)
print "The variance is : " +(variance_str)
