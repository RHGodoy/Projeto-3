import unittest
from locadora import Locadora
from locadora import Cliente

class testes(unittest.TestCase):
    def setUp(self):
        self.locadora = Locadora(10, 5, 25, 100)
        self.cliente = Cliente("Ricardo", 1)

    def testaCriaNovoCliente(self):
        pass

    def testaNovoAluguel(self):
        pass

    def testaEncerraAluguelCasoIdeal(self):
        pass

