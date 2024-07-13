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



no1 = No(4)
no2 = No(2)
no3 = No(7)

no1.set_esquerda(no2)
no1.set_direita(no3)

print(no1.obter_valor())
print(no1.obter_direta().obter_valor())
print(no1.obter_esquerda())
print(no1.obter_esquerda().obter_valor())