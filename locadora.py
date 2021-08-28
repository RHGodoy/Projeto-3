import datetime

class locadora(object):
    def __init__(self, estoque, taxaAluguel):
        self.estoque = estoque
        self.taxaAluguel = taxaAluguel
       
    # mostra o estoque
    # recebe o pedido   
    # calcula a conta
 

class cliente(object):
    def __init__(self, nome, modalidade, numBikes):   # modalidade = hora / dia / semana
        self.nome = nome
        self.modalidade = modalidade
        self.numBikes = numBikes

    # olhaEstoque
    # aluguelFamily
    def alugaBike(self, nome, modalidade, numBikes):   