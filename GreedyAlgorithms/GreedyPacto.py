class Candidato (): #Object Oriented Programming

	def __init__(self, nombre, pros, contras): #The elements have a name, pros, cons and a ratio
		self.nombre = nombre
		self.pros = pros
		self.contras = contras
		self.ratio = float(pros /  contras)

#Main

mejorCand = Candidato(' ',-1,-1)
Candidatos = [] #list of candidates
prosNecesarios = 0 #with the total sum of pros / 2 + 1, a team wins

for i in range (int(input())):
	entrada = input()

	nombre = entrada[:entrada.index(' ')] #name

	proscontras = entrada[entrada.index(' ')+1:]
	pros = int(proscontras[:proscontras.index(' ')]) #pros
	contras = int(proscontras[proscontras.index(' ')+1:]) #cons

	nuevoCand = Candidato(nombre,pros,contras) #new Candidate
	prosNecesarios += pros

	if nuevoCand.pros > mejorCand.pros :
		mejorCand = nuevoCand #we try to find the best candidate

	Candidatos.append(nuevoCand)

Candidatos.sort(key = lambda o: o.ratio, reverse = True) #sort the list of them, to have the best first	
Candidatos.remove(mejorCand)	

prosNecesarios = (prosNecesarios / 2) + 1
prosConseguidos = mejorCand.pros
aux = 0

while prosConseguidos < prosNecesarios: #as soon as we have the pros a team need to win, we finish and return that team sorted
	prosConseguidos += Candidatos[aux].pros
	aux += 1

Candidatos = Candidatos[:aux]
Candidatos.sort(key = lambda o: o.nombre)

print(mejorCand.nombre)
for j in range(aux) :
	print(Candidatos[j].nombre)	




