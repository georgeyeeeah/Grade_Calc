import math
#Replace Prints with Functions
#Methods for everything
#Classes for everything

#Exams
ex = input("How many ex?")
if int(ex) > 0:
	exW = int(input("\nWeight of ALL Ex: \n")) / 100
	exList = ["\nEx Scores"]
	exOutof = ["\nEx Out Of"]
	exPList = ["\nWeight"] 
	exSW = input("\nAll the same weight? \n 1.Yes \n 2.No \n ")
	exTotal = 0
	for i in range(int(ex)):
		exList.append(input("\nWhat did you score on Ex " + str(i + 1) + ": "))
		exOutof.append(input("\nOut of " + str(i + 1) + ": "))
		if int(exSW) == 2:
			exWeightCalc = int(input("\nDo you need to calculate the weight? \n 1.Yes \n 2.No"))
			if exWeightCalc == 1:
				exPList.append((int(input("\nercentage of total grade")) * int(exW)) * 100) 
			else:
				exPList.append(input("\nWhat was the weight of Ex " + str(i + 1) + ": "))
			exTotal += ((int(exList[i + 1]) / int(exOutof[i + 1])) * 100) *  (int(exPList[i + 1]) / 100)
		else:
			exTotal += ((int(exList[i + 1]) / int(exOutof[i + 1])) * 100) / int(ex)
	exFinal = exTotal * exW
else:
	print("No ex")
	exFinal = 0
print("\n****************************************** \n")
for i in range(1,(int(ex) + 1)):
		print("Exam",i,":", exList[i],"out of", exOutof[i])
print("\n****************************************** \n")
#HW
hw = input("How many hw?")
if int(hw) > 0:
	hwOutof = ["hw Out Of"]
	hwW = int(input("Weight of ALL Hw: \n")) / 100
	hwList = ["Hw Scores"]
	hwPList = ["Weight"]
	hwSW = input("All the same weight? \n 1.Yes \n 2.No \n ")		
	hwTotal = 0
	for i in range(int(hw)):
		hwList.append(input("What did you score on Hw " + str(i + 1) + ": "))
		hwOutof.append(input("Out of " + str(i + 1) + ": "))
		if int(hwSW) == 2:
			hwWeightCalc = int(input("Do you need to calculate the weight? \n 1.Yes \n 2.No"))
			if hwWeightCalc == 1:
				hwPList.append((int(input("Percentage of total grade")) * int(hwW)) * 100) 
			else:
				hwPList.append(input("What was the weight of Hw " + str(i + 1) + ": "))
			hwTotal += ((int(hwList[i + 1]) / int(hwOutof[i + 1])) * 100) *  (int(hwPList[i + 1]) / 100)
		else:
			hwTotal += ((int(hwList[i + 1]) / int(hwOutof[i + 1])) * 100) / int(hw)
	hwFinal = hwTotal * hwW
else:
	hwFinal = 0
	print("No HW")
#quiz
quiz = input("How many q?")
if int(quiz) > 0:
	quizOutof = ["quiz Out Of"]
	quizW = int(input("Weight of ALL Q: \n")) / 100
	quizList = ["Q Scores"]
	quizPList = ["Weight"]
	quizTotal = 0
	quizSW = input("All the same weight? \n 1.Yes \n 2.No \n ")	
	for i in range(int(quiz)):
		quizList.append(input("What did you score on Q " + str(i + 1) + ": "))
		quizOutof.append(input("Out of " + str(i + 1) + ": "))
		if int(quizSW) == 2:
			quizWeightCalc = int(input("Do you need to calculate the weight? \n 1.Yes \n 2.No"))
			if quizWeightCalc == 1:
				quizPList.append((int(input("Percentage of total grade")) * int(quizW)) * 100) 
			else:
				quizPList.append(input("What was the weight of Q " + str(i + 1) + ": "))
			quizTotal += ((int(quizList[i + 1]) / int(quizOutof[i + 1])) * 100) *  (int(quizPList[i + 1]) / 100)
		else:
			quizTotal += ((int(quizList[i + 1]) / int(quizOutof[i + 1])) * 100) / int(quiz)
	quizFinal = quizTotal * quizW
else:
	quizFinal = 0
	print("No Q")
#EC

ec = input("How much EC?")
if int(ec) > 0:
	ecOutof = ["ec Out Of"]
	ecW = int(input("Weight of ALL EC: \n")) / 100
	ecList = ["EC Score"]
	ecPList = ["Weight"]
	ecTotal = 0
	ecSW = input("All the same weight? \n 1.Yes \n 2.No \n ")	
	for i in range(int(ec)):
		ecList.append(input("What did you score on EC " + str(i + 1) + ": "))
		ecOutof.append(input("Out of " + str(i + 1) + ": "))
		if int(ecSW) == 2:
			ecWeightCalc = int(input("Do you need to calculate the weight? \n 1.Yes \n 2.No"))
			if ecWeightCalc == 1:
				ecPList.append((int(input("Percentage of total grade")) * int(ecW)) * 100) 
			else:
				ecPList.append(input("What was the weight of EC " + str(i + 1) + ": "))
			ecTotal += ((int(ecList[i + 1]) / int(ecOutof[i + 1])) * 100) *  (int(ecPList[i + 1]) / 100)
		else:
			ecTotal += ((int(ecList[i + 1]) / int(ecOutof[i + 1])) * 100) / int(ec)
	ecFinal = ecTotal * ecW
else:
	ecFinal = 0
	print("no EC")
finalG = ecFinal + exFinal + hwFinal + quizFinal
print(finalG)
