#!/usr/bin/python3

start = input("Please pass the beginning of range\n")
end = input("Please pass the ending of range\n")
start = int(start)
end = int(end)

if start < 2:
	print("You have entered wrong beginning of range")

if start >= end: 
	print("You have entered wrong ending of range")

def findAllPrimeNumbers(argStart,argEnd):
	file = open('results.txt', 'w')
	for elem in range(argStart,argEnd):
		for i in range(2,elem):
			if elem%i == 0:
				break
		else:
			file.write(str(elem)+"\n")
	file.close()			

findAllPrimeNumbers(start,end);