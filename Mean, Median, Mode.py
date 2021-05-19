from math import floor
print("== Mean, Median, Mode ==")
print("Note:\n> Input syntax: 10, 20\n> Mode will be counted if input has at least 2 same numbers\n")
lists = input("Input number: ")
try:
	data = eval(f"sorted([{lists}])")
	if len(data) == 1 :
		print("NO! You can't, you must input at least 2 number")
	else:
		print("\nSorted data: "+str(data))
		
		dict = {}
		mean = 0
		for val in data :
			dict[val] = data.count(val)
			mean += val
			
		#Mean
		print("Mean: "+str(mean/len(data)))
		
		#Median
		length = len(data) % 2
		if length > 0 :
			median = data[floor(len(data)/2)]
		else :
			median = (data[int(len(data)/2)]+data[int(len(data)/2-1)])/2
		print("Median: "+str(median))
		
		#Mode
		valList = list(dict.values())
		keyList = list(dict.keys())
		mode = keyList[valList.index(sorted(valList)[-1])]
		if sorted(valList)[-1] != sorted(valList)[-2] :
			print("Mode: "+str(mode))
except:
	print("Oh no, you broke the program! Please exit and try again with correct input\nCorrect input: 1,2,3")
