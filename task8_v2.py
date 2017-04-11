#!/usr/bin/python3

def chooseElementsByCriterium(stud_list,kryterium):
	listOfStudents=[]
	for item in stud_list:
		if float(item["grade"]) == float(kryterium) :
			listOfStudents.append(item)
	return listOfStudents

def readFromFile(name):
	studentList=[]
	with open(name) as fin:
		for line in fin:
			line=line.split()
			student = {'student': {'name':line[0],'surname':line[1]} ,'grade':line[2]}
			studentList.append(student)
	return studentList


list = chooseElementsByCriterium(readFromFile("task8_file.txt"),3.5)
for tmp in list:
	print(tmp)