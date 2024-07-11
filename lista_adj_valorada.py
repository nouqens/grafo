class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]

    def adicona_aresta(self, u, v, peso):
        # estamos pensando em grafos direcionados com peso nas arestas:
        self.grafo[u-1].append([v, peso])

        # se for grafos não direcionados com peso nas arestas adicionamos: 
        # self.grafo[v-1].append([u, peso])
    
    def mostra_lista(self):
        print('Lista de Adjacencia')
        for i in range(self.vertices):
            print(f'{i+1}:', end='  ' )
            for j in self.grafo[i]:
                print(f'{j}  ->', end='  ')
            print()


g = Grafo(4)


g.adicona_aresta(2,3, 5)
g.adicona_aresta(4,6, 7)
g.adicona_aresta(1,2, 6)
g.adicona_aresta(4,2, 9)

g.mostra_lista()
