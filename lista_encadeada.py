class No:

    def __init__(self, valor):
        self.valor =  valor
        self.proximo = None

    def obter_valor(self):
        return self.valor
    
    def set_proximo(self, proximo):
        self.proximo = proximo

    def obter_proximo(self):
        return self.proximo
    

no1 = No(4)
no2 = No(7)


print(no1.obter_valor())
print(no2.obter_valor())

no1.set_proximo(no2)


print(no1.obter_proximo())
print(no1.obter_proximo().obter_valor())