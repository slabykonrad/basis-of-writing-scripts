#!/usr/bin/python3

firstMonth=input("Please enter first month\n")
secondMonth=input("Please enter second month\n")

def checkDifferenceBetweenMonths(month1,month2):
	list=["january","february","march","april","may","june","july","august",\
	"september","october","november","december"]

	if month1.lower() in list:
		number1 = list.index(month1.lower())+1
	else:
		print("Wrong name of first month\n")
		exit()

	if month2.lower() in list:
		number2 = list.index(month2.lower())+1
	else:
		print("Wrong name of second month\n")
		exit()

	if number1 <= number2:
		return number2-number1
	else:
		return 12-(number1-number2)

print("Difference between months = " + str(checkDifferenceBetweenMonths(firstMonth,secondMonth)))