#!/usr/bin/python3
# -*- coding: utf-8 -*-
#https://www.pydanny.com/why-doesnt-python-have-switch-case.html

def translateNumbersToStrng(num):
	if len(num) == 1:
		return convertNumberToUnity(int(num))
	if len(num) == 2:
		return convertNumberToDozens(num)
	if len(num) == 3:
		return convertNumberToHundreds(num)
	if len(num) == 4:
		return convertNumberToThousand(num)
	if len(num) == 5:
		return convertNumberToTenThousand(num)
		
def convertNumberToUnity(char):
	return{
		0 : "zero",
		1 : "jeden",
		2 : "dwa",
		3 : "trzy",
		4 : "cztery",
		5 : "pięć",
		6 : "sześć",
		7 : "siedem",
		8 : "osiem",
		9 : "dziewięć"
	}.get(char,"null")

def convertNumberToDozens(char):
	if int(int(char) / 10) % 10 == 1:
		return convertNumberToFirstDozen(char);
	else:
		return convertNumberToNextDozens(char);

def convertNumberToFirstDozen(char):
	if int(char) % 10 == 0:
		return "dziesięć"
	if int(char) % 10 == 1:
		char = int(char) % 10
		return convertNumberToUnity(int(char)) + "aście"
	if int(char) % 10 == 4:
		char = convertNumberToUnity(int(char) % 10)
		char = char[:-1]
		return char + "naście"
	if int(char) % 10 == 5 or int(char) % 10 == 9:
		char = convertNumberToUnity(int(char) % 10)
		char = char[:-1]
		return char + "tnaście"
	if int(char) % 10 == 6:
		char = convertNumberToUnity(int(char) % 10)
		char = char[:-2]
		return char + "snaście"
	else:
		char = int(char) % 10
		return convertNumberToUnity(int(char)) + "naście"

def convertNumberToNextDozens(char):
	if int(int(char) / 10)  % 10 == 2:
		if int(char) % 10 == 0:
			char = int(char) / 10
			return convertNumberToUnity(int(char)) + "dzieścia"
		else:
			tmp = int(char) % 10
			char = int(char) / 10
			return convertNumberToUnity(int(char)) + "dzieścia" + " " + convertNumberToUnity(int(tmp))
	if int(int(char) / 10)  % 10 == 3:
		if int(char) % 10 == 0:
			return convertNumberToUnity(int(int(char) / 10)) + "dzieści"
		else:
			tmp = int(char) % 10
			return convertNumberToUnity(int(int(char) / 10)) + "dzieści" + " " + convertNumberToUnity(int(tmp))
	if int(int(char) / 10)  % 10 == 4:
		if int(char) % 10 == 0:
			char = convertNumberToUnity(int(int(char) / 10))
			return char[:-1]+ "dzieści"
		else:
			tmp = int(char) % 10
			char = convertNumberToUnity(int(int(char) / 10))
			return char[:-1] + "dzieści" + " " + convertNumberToUnity(int(tmp))
	else:
		if int(char) % 10 == 0:
			return convertNumberToUnity(int(int(char) / 10)) + "dziesiąt"
		else:
			tmp = int(char) % 10
			return convertNumberToUnity(int(int(char) / 10)) + "dziesiąt" + " " + convertNumberToUnity(int(tmp))

def convertNumberToHundreds(char):
	if int(char) == 0:
		return ""
	if int(int(char) / 100)  % 10 == 0:
		if int(char) > 0 and int(char) < 10:
			return convertNumberToUnity(int(char))
		if int(char) > 9 and int(char) < 20:
			return convertNumberToFirstDozen(char)
		if int(char) > 19 and int(char) <= 99:
			return convertNumberToNextDozens(char)
	if int(int(char) / 100)  % 10 == 1:
		char = int(char) - 100
		if int(char) == 0:
			return "sto "
		if int(char) > 0 and int(char) < 10:
			return "sto " + convertNumberToUnity(int(char))
		if int(char) > 9 and int(char) < 20:
			return "sto " + convertNumberToFirstDozen(char)
		if int(char) > 19 and int(char) <= 99:
			return "sto " + convertNumberToNextDozens(char)
	if int(int(char) / 100)  % 10 == 2:
		char = int(char) - 200
		if int(char) == 0:
			return "dwieście "
		if int(char) > 0 and int(char) < 10:
			return "dwieście " + convertNumberToUnity(int(char))
		if int(char) > 9 and int(char) < 20:
			return "dwieście " + convertNumberToFirstDozen(char)
		if int(char) > 19 and int(char) <= 99:
			return "dwieście " + convertNumberToNextDozens(char)
	if int(int(char) / 100)  % 10 == 3 or int(int(char) / 100)  % 10 == 4:
		tmp = int(char) / 100
		char = int(char) - int(100 * int(tmp))
		if int(char) == 0:
			return convertNumberToUnity(int(tmp)) + "sta "
		if int(char) > 0 and int(char) < 10:
			return convertNumberToUnity(int(tmp)) + "sta " + convertNumberToUnity(int(char))
		if int(char) > 9 and int(char) < 20:
			return convertNumberToUnity(int(tmp)) + "sta " + convertNumberToFirstDozen(char)
		if int(char) > 19 and int(char) <= 99:
			return convertNumberToUnity(int(tmp)) + "sta " + convertNumberToNextDozens(char)
	else:
		tmp = int(char) / 100
		char = int(char) - int(100 * int(tmp))
		if int(char) == 0:
			return convertNumberToUnity(int(tmp)) + "set "
		if int(char) > 0 and int(char) < 10:
			return convertNumberToUnity(int(tmp)) + "set " + convertNumberToUnity(int(char))
		if int(char) > 9 and int(char) < 20:
			return convertNumberToUnity(int(tmp)) + "set " + convertNumberToFirstDozen(char)
		if int(char) > 19 and int(char) <= 99:
			return convertNumberToUnity(int(tmp)) + "set " + convertNumberToNextDozens(char)

def convertNumberToThousand(char):
	if int(char) == 0:
		return ""
	if int(int(char) / 1000) % 10 == 0:
		return convertNumberToHundreds(char)
	if int(int(char) / 1000) % 10 == 1:
		return "tysiąc " + convertNumberToHundreds(int(char)-1000)
	if int(int(char) / 1000) % 10 == 2 or int(int(char) / 1000)  % 10 == 3 or int(int(char) / 1000)  % 10 == 4:
		tmp = int(char) / 1000
		char = int(char) - int(int(tmp)*1000)
		return convertNumberToUnity(int(tmp)) + "tysiące " + convertNumberToHundreds(char)
	else:
		tmp = int(char) / 1000
		char = int(char) - int(int(tmp)*1000)
		return convertNumberToUnity(int(tmp)) + "tysięcy " + convertNumberToHundreds(char)

def convertNumberToTenThousand(char):
	if int(int(char) / 10000) % 10 == 1 and int(int(char) / 1000) % 10 > 0:
		tmp = int(char) / 1000
		char = int(char) - int(1000*int(tmp))
		return convertNumberToDozens(tmp) + " tysięcy " + convertNumberToThousand(char)
	if int(int(char) / 10000) % 10 == 1:
		return "dziesięć tysięcy " + convertNumberToThousand(int(char)-10000)
	else:
		tmp = int(char) / 1000
		char = int(char) - int(1000*int(tmp))
		return convertNumberToDozens(tmp) + " tysięcy " + convertNumberToThousand(char)

while 1:
	number=input("Please enter a number\n")

	if int(number) > 99999:
		print("The number is too much")

	print(translateNumbersToStrng(number))