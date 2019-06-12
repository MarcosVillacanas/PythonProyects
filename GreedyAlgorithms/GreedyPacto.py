class Candidato (): 

	def __init__(self, nombre, pros, contras):
		self.nombre = nombre
		self.pros = pros
		self.contras = contras
		self.ratio = float(pros /  contras)

#Main

mejorCand = Candidato(' ',-1,-1)
Candidatos = []
prosNecesarios = 0

for i in range (int(input())):
	entrada = input()

	nombre = entrada[:entrada.index(' ')]

	proscontras = entrada[entrada.index(' ')+1:]
	pros = int(proscontras[:proscontras.index(' ')])
	contras = int(proscontras[proscontras.index(' ')+1:])

	nuevoCand = Candidato(nombre,pros,contras)
	prosNecesarios += pros

	if nuevoCand.pros > mejorCand.pros :
		mejorCand = nuevoCand

	Candidatos.append(nuevoCand)

Candidatos.sort(key = lambda o: o.ratio, reverse = True)	
Candidatos.remove(mejorCand)	

prosNecesarios = (prosNecesarios / 2) + 1
prosConseguidos = mejorCand.pros
aux = 0

while prosConseguidos < prosNecesarios:
	prosConseguidos += Candidatos[aux].pros
	aux += 1

Candidatos = Candidatos[:aux]
Candidatos.sort(key = lambda o: o.nombre)

print(mejorCand.nombre)
for j in range(aux) :
	print(Candidatos[j].nombre)	




