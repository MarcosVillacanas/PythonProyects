import networkx as nx
import matplotlib.pyplot as plt

def DFS3 (G, v, Visitados, Particular):
	Visitados[v] = True
	Particular.append(v)
	for Elem in G[v]:
		if not Visitados[Elem]:
			DFS3 (G, Elem, Visitados, Particular)

def DFS2 (G, v):
	Lon = len(G)
	Visitados = []
	for i in range(Lon):
		Visitados.append(False)
	Particular = []
	DFS3 (G, v, Visitados, Particular)
	return Particular

def DFS (G):
	Lon = len(G)
	Global = []
	for i in range (Lon):
		Global.append(DFS2(G,i))
	return Global	
	
#Main
numNodos = int(input('Numero de nodos: '))
numAristas = int(input('Numero de aristas: '))
G = nx.Graph()
for j in range (numAristas):
	G.add_edge(int(input('El nodo: ')) , int(input('enlaza con el nodo: ')) )
print(DFS(G))	