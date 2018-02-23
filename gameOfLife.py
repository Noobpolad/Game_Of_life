import random

row = int(input("Put the number of rows: ")) + 2
col = int(input("Put the number of colums: ")) + 2

originalBoard = []		
modifiedBoard = []
userInput = "con"

def defineOriginalBoard():
	
	for a in range(0,row):

		newRow = []

		for b in range(0,col):

			c = random.randint(0,1)
					
			if a == 0 or a == row - 1  or b == 0 or b == col - 1 :

				newRow.append(0)
						
			else:

				newRow.append(c)
						
		originalBoard.append(newRow)		

def printOriginalBoard():

	print("Initial board:")

	for a in range(0,row):

		for b in range(0,col):

			if a == 0 or a == row - 1  or b == 0 or b == col - 1 :

				print(" ",end=" ")

			else:
				print(originalBoard[a][b],end=" ")

		print()

def defineModifiedBoard():

	for a in range(1,row-1):

		newModifiedRow = []

		for b in range(1,col-1):

			if originalBoard[a][b] == 1 and originalBoard[a-1][b] + originalBoard[a+1][b] + originalBoard[a][b-1] + originalBoard[a][b+1] + originalBoard[a-1][b-1] + originalBoard[a-1][b+1] + originalBoard[a+1][b-1] + originalBoard[a+1][b+1] > 3 or originalBoard[a][b] == 1 and originalBoard[a-1][b] + originalBoard[a+1][b] + originalBoard[a][b-1] + originalBoard[a][b+1] + originalBoard[a-1][b-1] + originalBoard[a-1][b+1] + originalBoard[a+1][b-1] + originalBoard[a+1][b+1] < 2:

				newModifiedRow.append(0)

			elif originalBoard[a][b] == 0 and originalBoard[a-1][b] + originalBoard[a+1][b] + originalBoard[a][b-1] + originalBoard[a][b+1] + originalBoard[a-1][b-1] + originalBoard[a-1][b+1] + originalBoard[a+1][b-1] + originalBoard[a+1][b+1] == 3:
				
				newModifiedRow.append(1)

			elif originalBoard[a][b] == 1 and originalBoard[a-1][b] + originalBoard[a+1][b] + originalBoard[a][b-1] + originalBoard[a][b+1] + originalBoard[a-1][b-1] + originalBoard[a-1][b+1] + originalBoard[a+1][b-1] + originalBoard[a+1][b+1] == 3 or originalBoard[a][b] == 1 and originalBoard[a-1][b] + originalBoard[a+1][b] + originalBoard[a][b-1] + originalBoard[a][b+1] + originalBoard[a-1][b-1] + originalBoard[a-1][b+1] + originalBoard[a+1][b-1] + originalBoard[a+1][b+1] == 2:

				newModifiedRow.append(1)

			elif originalBoard[a][b] == 0 and originalBoard[a-1][b] + originalBoard[a+1][b] + originalBoard[a][b-1] + originalBoard[a][b+1] + originalBoard[a-1][b-1] + originalBoard[a-1][b+1] + originalBoard[a+1][b-1] + originalBoard[a+1][b+1] != 3:	

				newModifiedRow.append(0)

		modifiedBoard.append(newModifiedRow)
		
def printModifiedBoard():

	print("Modified board:")
	print()

	for a in range(0,row-2):

		print("  ",end="")

		for b in range(0,col-2):

				print(modifiedBoard[a][b], end=" ")

		print()

	print()	

def changeModifiedToOriginal():

	for a in range(0,row-2):

		for b in range(0,col-2):	

			originalBoard[a+1][b+1] = modifiedBoard[a][b]

def checkIfAllDead():

	for a in range(0,row-2):

		for b in range(0,col-2):

			if modifiedBoard[a][b] == 1:

				return False

	return True			

defineOriginalBoard()

while userInput == "con":

	defineModifiedBoard()

	printOriginalBoard()

	printModifiedBoard()

	changeModifiedToOriginal()

	if checkIfAllDead() == True:

		print("All are dead !")

		break

	modifiedBoard = []

	userInput = input("Put the command: ")
	print()