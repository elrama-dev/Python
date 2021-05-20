#Import module
from cmath import *

#Loop 
run = True

#Run Program
print("== Mini Calculator Program ==")
print("> To exit program, please type 'q' without quote")
print("> To make variable, syntax: key=value")
print("> To evaluate math, syntax: 1+1 (Without '=')")
print("> This program using cmath module, you can see it in https://docs.python.org/3/library/cmath.html")
print("> To use cmath module, just call the function without module name")
print()
while run:
	calc = input(">>> ")
	try:
		if "=" in calc:
			exec(calc)
		else:
			result = eval(calc)
			print(result)
	except:
		if calc.lower() == "q":
			run = False
		else:
			print("Invalid syntax of math")
