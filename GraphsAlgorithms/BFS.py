import networkx as nx #Graphs's Library
import matplotlib.pyplot as plt #This library allows you to show the graph

def BFS (grafo, nodoInicio):
	Longitud = len(G)
	ListaSol = [] #final list with the nodes after BFS
	Visitados = [] #boolean array  with the nodos i have visited
	for i in range (Longitud):
		Visitados.append(False)
	Cola = [] #Candidate's queue
	
	Cola.insert(0,nodoInicio) #the first node enters the queue
	Visitados[nodoInicio] = True #and so it is visited
	ListaSol.append(nodoInicio) #and it is added to the final list

	while Cola: #until the queue is empty
		Elem = Cola.pop() #pick up an element
		for Aux in G[Elem]: #and for every neighboourd
			if not Visitados[Aux]: #if it is not visited yet
				Cola.insert(0,Aux) #add it to the queue
				ListaSol.append(Aux) #add it to the list
				Visitados[Aux] = True #and dont forget saving it is visited

	return ListaSol			

#Main

numNodos = int(input('Numero nodos: ')) #number of nodes
numAristas = int(input('Numero Aristas: ')) #number of arcs
nodoInicio = int(input('Nodo inicial: ')) #the node which BFS starts with

G = nx.Graph()
ListaNodos = [] #Nodes which formed the graph

for i in range (numNodos):
	ListaNodos.append(i)
G.add_nodes_from(ListaNodos)

for j in range (numAristas):
	G.add_edge(int(input('El nodo: ')) , int(input('enlaza con el nodo: ')) )

print(BFS(G, nodoInicio))
nx.draw_circular(G,node_size=2000,node_color='c', with_labels=True)
plt.show()
