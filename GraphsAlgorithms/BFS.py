import networkx as nx
import matplotlib.pyplot as plt

def BFS (grafo, nodoInicio):
	Longitud = len(G)
	ListaSol = []
	Visitados = []
	for i in range (Longitud):
		Visitados.append(False)
	Cola = []
	
	Cola.insert(0,nodoInicio)
	Visitados[nodoInicio] = True
	ListaSol.append(nodoInicio +1)

	while Cola:
		Elem = Cola.pop()
		for Aux in G[Elem]:
			if not Visitados[Aux]:
				Cola.insert(0,Aux)
				ListaSol.append(Aux +1)
				Visitados[Aux] = True

	return ListaSol			

#Main

numNodos = int(input('Numero nodos: '))
numAristas = int(input('Numero Aristas: '))
nodoInicio = int(input('Nodo inicial: ')) -1

G = nx.Graph()
ListaNodos = []

for i in range (numNodos):
	ListaNodos.append(i)
G.add_nodes_from(ListaNodos)

for j in range (numAristas):
	G.add_edge(int(input('El nodo: ')) -1, int(input('enlaza con el nodo: ')) -1)

print(BFS(G, nodoInicio))
nx.draw_circular(G,node_size=2000,node_color='c', with_labels=True)
plt.show()
