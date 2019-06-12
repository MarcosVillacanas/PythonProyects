def isFeasible (Matriz, xCand, yCand): #the chest board is  5x5
	if xCand >= 0 and xCand < 5 and yCand >= 0 and yCand < 5 :
		return not Matriz[xCand][yCand] #a spot mustnt be visited before

def caballo (Matriz, xAct, yAct, movs):
	global xFin, yFin, movMin

	Matriz[xAct][yAct] = True #the spot is visited
	if xAct == xFin and yAct == yFin : #if we have found the exit
		if movs < movMin : #and with less moves than any other time, we have a new best
			movMin = movs
		Matriz [xAct][yAct] = False #backtracking	
		
	elif movs < movMin : #keep on solving in any way a horse can move through the chest
		if isFeasible (Matriz, xAct - 2, yAct + 1) :
			caballo (Matriz, xAct - 2, yAct + 1, movs + 1)	
		if isFeasible (Matriz, xAct - 2, yAct - 1) :
			caballo (Matriz, xAct - 2, yAct - 1, movs + 1)	

		if isFeasible (Matriz, xAct + 2, yAct + 1) :
			caballo (Matriz, xAct + 2, yAct + 1, movs + 1)	
		if isFeasible (Matriz, xAct + 2, yAct - 1) :
			caballo (Matriz, xAct + 2, yAct - 1, movs + 1)	

		if isFeasible (Matriz, xAct - 1, yAct + 2) :
			caballo (Matriz, xAct - 1, yAct + 2, movs + 1)	
		if isFeasible (Matriz, xAct + 1, yAct + 2) :
			caballo (Matriz, xAct + 1, yAct + 2, movs + 1)	

		if isFeasible (Matriz, xAct - 1, yAct - 2) :
			caballo (Matriz, xAct - 1, yAct - 2, movs + 1)	
		if isFeasible (Matriz, xAct + 1, yAct - 2) :
			caballo (Matriz, xAct + 1, yAct - 2, movs + 1)		

		Matriz [xAct][yAct] = False #backtracking								

#Main

xyIni = input()
xIni = int(xyIni[:1])
yIni = int(xyIni[2:])
xyFin = input()
xFin = int(xyFin[:1])
yFin = int(xyFin[2:])

Matriz = []
for i in range (5):
	Matriz.append([])
	for j in range (5):
		Matriz[i].append (False)

movMin = float('inf')

caballo(Matriz, xIni, yIni, 1)
print(movMin)

#This is a game in which a spot to begin and a exit spot are given and you have to tell the less moves a horse would need to reach the exit from the beggining
