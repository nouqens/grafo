from math import log as l
class HeapMax:

    def __init__(self):
        self.nos = 0
        self.heap = []

    def adiciona_no(self, u):
        self.heap.append(u)
        self.nos +=1
        f = self.nos
        while True:
            if f == 1:
                break
            p = f // 2
            if self.heap[p-1] >= self.heap[f-1]: # trocar o ">=" para "<=" se for heapmin
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
                if self.heap[f+1-1] > self.heap[f-1]: # troca o ">" por "<" se for heap minimo
                    f +=1
            if self.heap[p-1] > self.heap[f-1]:
                break
            else:
                self.heap[f - 1], self.heap[p - 1] = self.heap[p - 1], self.heap[f - 1]
                p = f
        return raiz


    def tamanho(self):
        return self.nos


    def maior_elemento(self):
        if self.nos != 0:
            return self.heap[0]
        return "A árvore esta vazia!"

    def filho_esquerda(self, i):
        if self.nos >= 2 * i:
            return self.heap[i*2-1]
        return f"Esse nó não tem filho à esquerda!"

    def filho_direita(self, i):
        if self.nos >= 2 * i + 1:
            return self.heap[i*2]
        return f"Esse nó não tem filho à direta!"

    def no_pai(self, j):
        return self.heap[j//2]




h = HeapMax()

h.adiciona_no(17), h.adiciona_no(36), h.adiciona_no(25)
h.adiciona_no(7), h.adiciona_no(3), h.adiciona_no(100)
h.adiciona_no(1), h.adiciona_no(2), h.adiciona_no(19)

elementomax = h.remove_no()
print(f'o elemento maximo é: {elementomax}')

h.mostra_heap()

print(f'tamanho: {h.tamanho()}')

print(f'Filho a esquerda de 17: {h.filho_esquerda(4)}')
print(f'Filho à direta de 17: {h.filho_direita(4)}')

