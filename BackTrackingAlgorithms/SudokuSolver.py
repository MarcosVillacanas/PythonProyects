
N = 0
matrizFinal = []
for i in range(9): #Declaracion de la matriz en la que guardare el resultado
	matrizFinal.append([])
	for j in range(9):
		matrizFinal[i].append('-1')

matriz = []
for i in range(9):
	matriz.append([])
	for j in range(9):
		matriz[i].append(int(input()))	

def isFeasible (matriz, fila, col, num) :
	for i in range (0,len(matriz),1) :
		if (matriz[i][col]==num or matriz[fila][i]==num) :
			return False
	auxFila = fila - fila%3
	auxCol = col - col%3
	for j in range (auxFila,auxFila+3,1) :
		for k in range (auxCol,auxCol+3,1) :
			if matriz[j][k] == num :
				return False
	return True

def copiarMatrices (matriz) :
	global matrizFinal
	for i in range (0, len(matriz) ,1) :		
		for j in range (0, len(matriz) ,1) :					
	   		matrizFinal [i][j] = matriz [i][j]		

def sudoku (i, j, matriz):
	global N
	if matriz[i][j] == 0 :
		k = 1
		while (k<=9 and N<2) : 
			if isFeasible (matriz, i, j, k):
				matriz[i][j] = k
				if (i==8 and j==8) :
					N = N+1
					if N==1:
						copiarMatrices(matriz)
				if (i<8 and j==8) :
					sudoku (i+1, 0, matriz)
				if (i<=8 and j<8) :
					sudoku (i, j+1, matriz)
			if N < 2:		
				matriz[i][j]=0
				k = k+1
	else :
		if (i==8 and j==8) :
			N = N+1
			if N==1:
				copiarMatrices(matriz)
		if (i<8 and j==8) :
			sudoku (i+1, 0, matriz)
		if (i<=8 and j<8) :
			sudoku (i, j+1, matriz)					

sudoku (0,0,matriz)   
if N==0:
	print('imposible')
elif N==1:
	print(matrizFinal)
else:
	print('casi sudoku')		




