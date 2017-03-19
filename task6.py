#!/usr/bin/python3
import pyparsing

def deletingOfComments(file):
	with open(file) as fileIn:
		line = fileIn.read()
		comment = pyparsing.nestedExpr("/*", "*/").suppress()
	with open(file, 'w') as fileOut:
		fileOut.write(comment.transformString(line))

	with open(file) as fileIn:
		lines = fileIn.readlines()
		with open(file, 'w') as fileOut:
			for line in lines:
				index=line.find("//")

				if index == -1:
					fileOut.write(line)

				if index > 0:
					if line[index:].find("\"") != -1:
						fileOut.write(line)
					else:
						fileOut.write(line[:index])
						fileOut.write("\n")



deletingComments("main.cpp")