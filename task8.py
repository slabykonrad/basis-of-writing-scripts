#!/usr/bin/python3

class Students:
	def __init__(self, name, surname, grade):
		self.name = name
		self.surname = surname
		self.grade = grade

def chooseElementsByCriterium(stud_list,kryterium):
	listOfStudents=[]
	for item in stud_list:
		if float(item.grade) == float(kryterium) :
			listOfStudents.append(item)
	return listOfStudents

def readFromFile(name):
	studentList=[]
	with open(name) as fin:
		for line in fin:
			line=line.split()
			studentList.append(Students(line[0],line[1],line[2]))
	return studentList


list = chooseElementsByCriterium(readFromFile("task8_file.txt"),3.5)
for tmp in list:
	print(tmp.name + "  " + tmp.surname + "  " + str(tmp.grade))