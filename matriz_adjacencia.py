class Grafo:



    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]


    def adiconar_aresta(self, u, v):
        #grafo direcionado não 
        self.grafo[u-1][v-1] += 1 #trocar o += por = se não for grafo multiplo
        if u != v:
            self.grafo[v-1][u-1] += 1
        


    def mostra_matriz(self):
        print('A Matriz de adjacencia é:')
        for i in range(self.vertices):
            print(self.grafo[i])
    
    def tem_aresta(self, u, v):
        if self.grafo[u-1][v-1] == 0:
            print(f'Não tem entre aresta entre os vertices {u} e {v}')
        else:
            print(f'Existe {self.grafo[u-1][v-1]} de aresta entre os vertices {u} e {v}')





        
v = int(input('Quantidade de vertices: '))

g = Grafo(v)

a = int(input('numero de arestas: '))
for x in range(a):
   u = int(input('De qual vertice parte essa aresta: '))
   v = int(input('Para qual vertice chega essa aresta: ')) 
   g.adiconar_aresta(u,v)





g.mostra_matriz()

