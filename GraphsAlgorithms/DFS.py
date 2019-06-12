import networkx as nx #Graph's library
import matplotlib.pyplot as plt

def DFS3 (G, v, Visitados, Particular):
	Visitados[v] = True #set as visited the elements that are found
	Particular.append(v) #They are added also to the list
	for Elem in G[v]: #And from every neighbourd we make another call
		if not Visitados[Elem]:
			DFS3 (G, Elem, Visitados, Particular)

def DFS2 (G, v):
	Lon = len(G)
	Visitados = [] #Boolean array, which gives info about if one element is visited or not
	for i in range(Lon):
		Visitados.append(False)
	Particular = [] #The list generated from DFS with this node
	DFS3 (G, v, Visitados, Particular)
	return Particular

def DFS (G): #First DFS call
	Lon = len(G)
	Global = [] #Global list is created, it will host the DFS generated from every node
	for i in range (Lon):
		Global.append(DFS2(G,i)) #We generate a DFS from every element in the graph
	return Global	
	
#Main
numNodos = int(input('Numero de nodos: ')) #number of nodes
numAristas = int(input('Numero de aristas: ')) #number of arcs
G = nx.Graph()
for j in range (numAristas):
	G.add_edge(int(input('El nodo: ')) , int(input('enlaza con el nodo: ')) )
print(DFS(G))	
