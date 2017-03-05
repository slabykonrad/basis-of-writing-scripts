#!/usr/bin/python3
import string

myString = input("Please enter the string\n")

def findAllDifferentChars(insc):
	list = []
	for elem in insc:
		if not elem in list:
			list.append(elem)
	return list


result = findAllDifferentChars(myString)
print(len(result))