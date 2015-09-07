##################################################################
# Performance of Computer Networks 
# CS 6352 HomeWork 1, Question.4.
# @Author: srayan.guhathakurta@utdallas.edu
##################################################################


# Theoretical values for exponential distribution
# Mean = 0.5
# Variance = 0.25

#!/usr/bin/python
import sys, os
import numpy

# Respective values of k, m and Seed value S[0] in sList
k = 16807
m = 2147483647
sList = [1111]
rList=[]
yList=[]
numIndex = 0
expIndex = 0
i = 0
lembda = 2


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

# Generating the sequence of 10000 exponentially distributed pseudo-random numbers
while expIndex < 10000:
	Yn = (-0.5) * numpy.log(rList[expIndex])
	yList.append(Yn)
	expIndex = expIndex + 1

#print (yList)

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



# Calculate mean and variance
mean = numpy.mean(yList)
str(mean)
mean_str = str(mean)
print "The mean is : " +(mean_str)

variance = numpy.var(yList)
str(variance)
variance_str = str(variance)
print "The variance is : " +(variance_str)

print "For exponential distribution the theoretical mean = 0.5 and variance = 0.25"
