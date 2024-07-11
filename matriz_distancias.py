class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def adiconar_aresta(self, u, v, peso):
        #grafo direcionado simples
        self.grafo[u-1][v-1] = peso #trocar o = por += se for grafo multiplo

        self.grafo[v-1][u-1] = 1

    def mostra_matriz(self):
        print('A Matriz de adjacencia é:')
        for i in range(self.vertices):
            print(self.grafo[i])
    

v = int(input('Quantidade de vertices: '))

g = Grafo(v)

a = int(input('numero de arestas: '))
for x in range(a):
   u = int(input('De qual vertice parte essa aresta: '))
   v = int(input('Para qual vertice chega essa aresta: ')) 
   p = int(input('O peso dessa aresta: '))
   g.adiconar_aresta(u,v,p)



g.mostra_matriz()
