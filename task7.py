#!/usr/bin/python3
import collections 

def wordCounter(file):
	file = open(file, "r", encoding="utf-8-sig")
	counterWord=collections.Counter()
	for word in file.read().lower().split():
		if word[-1] in "`~!@#$%^&*()_-+=|\'\";\:<,>.?/*-+":
			word = word[:-1]
		if word[0] in "`~!@#$%^&*()_-+=|\'\";\:<,>.?/*-+":
			word = word[1:]
		if not word.isalpha():
			continue
		if word not in counterWord:
			counterWord[word]=1
		else:
			counterWord[word]+=1
	return counterWord

	

def countingWordsInFiles(*args):
	wordcount=collections.Counter()
	for item in list(args):
		wordcount.update(wordCounter(item))

	#for k,v in wordcount.items():
	#	print(k,v)
	print(wordcount.most_common(10))

countingWordsInFiles("in.txt","in2.txt")
