#!/usr/bin/python3

myString = input("Please enter a text\n")

def divideByWords(insc):
	list = insc.split()
	list.sort(key=len,reverse=True)
	return list

myList = divideByWords(myString)
print(myList)