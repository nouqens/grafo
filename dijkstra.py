from math import log as l


class HeapMin:

    def __init__(self):
        self.nos = 0
        self.heap = []

    def adiciona_no(self, u, indice):
        self.heap.append([u, indice])
        self.nos +=1
        f = self.nos
        while True:
            if f == 1:
                break
            p = f // 2
            if self.heap[p-1][0] <= self.heap[f-1][0]: # trocar o ">=" para "<=" se for heapmin
                break
            else:
                self.heap[p-1], self.heap[f-1] = self.heap[f-1], self.heap[p-1]
                f = p

    def mostra_heap(self):
        # forma simples print(self.heap)
        print('A estrutura heap é:')
        nivel = int(l(self.nos, 2))
        a = 0
        for i in range(nivel):
            for j in range(2 ** i):
                print(f'{self.heap[a]}', end = '  ')
                a +=1
            print('')
        for i in range(self.nos - a):
            print(f'{self.heap[a]}', end = '  ')
            a +=1
        print()


    def remove_no(self):
        raiz = self.heap[0]
        self.heap[0] = self.heap[self.nos-1]
        self.heap.pop()
        self.nos -= 1
        p = 1
        while True:
            f = 2 * p
            if f > self.nos:
                break
            if f+1 <= self.nos:
                if self.heap[f+1-1][0] < self.heap[f-1][0]: # troca o ">" por "<" se for heap minimo
                    f +=1
            if self.heap[p-1][0] <= self.heap[f-1][0]:    # troca o ">=" por "<=" se for heap minimo
                break
            else:
                self.heap[f - 1], self.heap[p - 1] = self.heap[p - 1], self.heap[f - 1]
                p = f
        return raiz
    

    def tamanho(self):
        return self.nos


class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def adiconar_aresta(self, u, v, peso):
        self.grafo[u-1][v-1] = peso 
        self.grafo[v-1][u-1] = peso


    def mostra_matriz(self):
        print('A Matriz de adjacencia é:')
        for i in range(self.vertices):
            print(self.grafo[i])

    def dijkstra(self, origem):
        custo_vem = [[-1, 0] for i in range(self.vertices)]
        custo_vem[origem - 1] = [0, origem]

        h = HeapMin()

        h.adiciona_no(0, origem)
        while h.tamanho() > 0:
            dist, v = h.remove_no()
            for i in range(self.vertices):
                if self.grafo[v-1][i] != 0:
                    if custo_vem[i][0] == -1 or custo_vem[i][0] > dist + self.grafo[v-1][i]:
                        custo_vem[i] = [dist + self.grafo[v-1][i], v]
                        h.adiciona_no(dist + self.grafo[v-1][i], i+1)
        return custo_vem
    




g = Grafo(7)

g.adiconar_aresta(1, 2, 5)
g.adiconar_aresta(1, 3, 6)
g.adiconar_aresta(1, 4, 10)
g.adiconar_aresta(2, 5, 13)
g.adiconar_aresta(3, 4, 3)
g.adiconar_aresta(3, 5, 11)
g.adiconar_aresta(3, 6, 6)
g.adiconar_aresta(4, 5, 6)
g.adiconar_aresta(4, 6, 4)
g.adiconar_aresta(5, 7, 3)
g.adiconar_aresta(6, 7, 8)

g.mostra_matriz()
distancia = g.dijkstra(1)
print(distancia)