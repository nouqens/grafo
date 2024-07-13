class No:

    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def obter_valor(self):
        return self.valor

    def set_esquerda(self, esquerda):
        self.esquerda = esquerda

    def set_direita(self, direita):
        self.direita = direita

    def obter_esquerda(self):
        return self.esquerda

    def obter_direta(self):
        return self.direita


class ArvoreBinariaBusca:

    def __init__(self):
        self.raiz = None

    def obter_raiz(self):
        return self.raiz

    def insere(self, valor):
        no = No(valor)
        if self.raiz == None:
            self.raiz = no
        else:
            no_atual = self.raiz
            no_pai = None
            while True:
                if no_atual != None:
                    no_pai = no_atual
                    if no.obter_valor() < no_atual.obter_valor():
                        no_atual = no_atual.obter_esquerda()
                    else:
                        no_atual = no_atual.obter_direta()
                else:
                    if no.obter_valor() < no_pai.obter_valor():
                        no_pai.set_esquerda(no)
                    else:
                        no_pai.set_direita(no)
                    break

    def mostra_arvore(self, no_atual): # percurso em ordem simetrica
        if no_atual != None:
            self.mostra_arvore(no_atual.obter_esquerda())
            print(f'{no_atual.obter_valor()}', end='  ')
            self.mostra_arvore(no_atual.obter_direta())




t = ArvoreBinariaBusca()

t.insere(8)
t.insere(3)
t.insere(6)
t.insere(10)
t.insere(14)
t.insere(1)
t.insere(7)
t.insere(13)
t.insere(4)

t.mostra_arvore(t.obter_raiz())
