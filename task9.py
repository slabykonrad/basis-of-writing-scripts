#!/usr/bin/python3

import os
import sys
from fnmatch import fnmatch
from pathlib import Path

def findAllFiles(pathToDir, wordToFind=""):
	
	if not os.path.exists(pathToDir):
		print("Wrong path! Directory doesn't exist in this path")
		return

	pattern = "*" + wordToFind + "*.*"
	tmpList=[]

	for path, subdirs, files in os.walk(pathToDir):
		for file in files:
			if fnmatch(file, pattern):
				tmpList.append(file)

	return tmpList

list = findAllFiles("/home/slaby/workspace/c++")

if not list:
	print("List is empty")
	sys.exit()

for result in list:
	print(result)