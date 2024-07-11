class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]

    def adicona_aresta(self, u, v):
        # estamos pensando em grafos direcionados:
        self.grafo[u-1].append(v)

        # se for grafos não direcionados adicionamos: 
        # self.grafo[v-1].append(u)
    
    def mostra_lista(self):
        print('Lista de Adjacencia')
        for i in range(self.vertices):
            print(f'{i+1}:', end='  ' )
            for j in self.grafo[i]:
                print(f'{j}  ->', end='  ')
            print()


g = Grafo(4)
g.adicona_aresta(2,3)
g.adicona_aresta(4,6)
g.adicona_aresta(1,2)
g.adicona_aresta(4,2)

g.mostra_lista()
