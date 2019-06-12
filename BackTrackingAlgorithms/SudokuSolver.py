
N = 0 #Number of possible solutions 
matrizFinal = [] #Sudoku solved matrix
for i in range(9): 
	matrizFinal.append([])
	for j in range(9):
		matrizFinal[i].append('-1')

matriz = [] #input Sudoku matrix
for i in range(9):
	matriz.append([])
	for j in range(9):
		matriz[i].append(int(input()))	

def isFeasible (matriz, fila, col, num) : #check if a number can be located in a spot
	for i in range (0,len(matriz),1) : #look for problems in its row and int column
		if (matriz[i][col]==num or matriz[fila][i]==num) :
			return False
	auxFila = fila - fila%3
	auxCol = col - col%3
	for j in range (auxFila,auxFila+3,1) : #look for problems in its 3x3 square
		for k in range (auxCol,auxCol+3,1) :
			if matriz[j][k] == num :
				return False
	return True

def copiarMatrices (matriz) : #copy the matrix which overwrite everytime while solving in the final matrix
	global matrizFinal
	for i in range (0, len(matriz) ,1) :		
		for j in range (0, len(matriz) ,1) :					
	   		matrizFinal [i][j] = matriz [i][j]		

def sudoku (i, j, matriz):
	global N
	if matriz[i][j] == 0 : #if we are in a spot to fill
		k = 1
		while (k<=9 and N<2) : 
			if isFeasible (matriz, i, j, k):
				matriz[i][j] = k
				if (i==8 and j==8) : #in case we have finished
					N = N+1
					if N==1:
						copiarMatrices(matriz)
				if (i<8 and j==8) : #keep on solving
					sudoku (i+1, 0, matriz)
				if (i<=8 and j<8) : #keep on solving
					sudoku (i, j+1, matriz)
			if N < 2:		
				matriz[i][j]=0
				k = k+1
	else : #if we are in a spot already filled
		if (i==8 and j==8) : #in case we have finished
			N = N+1
			if N==1:
				copiarMatrices(matriz)
		if (i<8 and j==8) : #keep on solving
			sudoku (i+1, 0, matriz)
		if (i<=8 and j<8) : #keep on solving
			sudoku (i, j+1, matriz)					

sudoku (0,0,matriz)   
if N==0:
	print('impossible') #not solution could be found
elif N==1:
	print(matrizFinal)
else:
	print('not sudoku') #if it is possible to solve it in more than one way, it is not a sudoku	




