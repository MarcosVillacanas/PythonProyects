def isFeasible (Matriz, xCand, yCand):
	if xCand >= 0 and xCand < 5 and yCand >= 0 and yCand < 5 :
		return not Matriz[xCand][yCand]

def caballo (Matriz, xAct, yAct, movs):
	global xFin, yFin, movMin

	Matriz[xAct][yAct] = True
	if xAct == xFin and yAct == yFin :
		if movs < movMin :
			movMin = movs
		Matriz [xAct][yAct] = False	
		
	elif movs < movMin :
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

		Matriz [xAct][yAct] = False								

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