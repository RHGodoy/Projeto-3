from datetime import datetime
import unittest
from Locadora import Locadora
from Cliente_Locadora import Cliente

class testes(unittest.TestCase):
    def setUp(self):
        self.locadora = Locadora(10, 5, 25, 100)
        self.cliente = Cliente("Ricardo", 1)

    #Testes relacionados ao Cliente.

    def testeConsultaEstoque(self):
        print("\nTeste de cliente consultando estoque.")
        self.assertEqual(self.cliente.consultaEstoque(self.locadora), 0)

    def testeAlugaBikeErrodeModalidade(self):
        print("\nTeste de aluguel solicitado com erro de modalidade.")
        self.assertEqual(self.cliente.alugaBike(self.locadora, 1, "minutos", datetime.now()), 0)

    def testeAlugaBikeSemData(self):
        print("\nTeste de aluguel sem colocar data de início.")
        self.assertEqual(self.cliente.alugaBike(self.locadora, 1, "hora", None), 0)

    def testeAlugaBikeDataInvalida(self):
        print("\nTeste de aluguel solicitado com erro de modalidade.")
        self.assertEqual(self.cliente.alugaBike(self.locadora, 1, "hora", "hoje"), 0)

    def testeAlugaBike(self):
        print("\nTeste de aluguel feito corretamente.")
        self.assertEqual(self.cliente.alugaBike(self.locadora, 1, "hora", datetime.now()), 0)

    def testeDevolveBike(self):
        print("\nTeste de devolução de bike.")
        self.assertEqual(self.cliente.devolveBike(self.locadora, datetime.now()), 0)


    #Testes relacionados a Locadora

    def testaCriaNovoCliente(self):
        print("\nTeste de criação do cliente no sistema.")
        self.assertEqual(self.locadora.criaCliente("Ricardo"), 0)

    def testaNovoAluguelSemEstoque(self):
        print("\nTeste de Locadora receber pedido de aluguel sem estoque.")
        self.assertEqual(self.locadora.novoAluguel(1, "Ricardo", "dia", 11, datetime), 0)

    def testaNovoAluguelQuantidadeInvalida(self):
        print("\nTeste de Locadora receber pedido de aluguel de quantidade inválida.")
        self.assertEqual(self.locadora.novoAluguel(1, "Ricardo", "dia", -2, datetime), 0)

    def testaNovoAluguel(self):
        print("\nTeste de Locadora receber pedido de aluguel.")
        self.assertEqual(self.locadora.novoAluguel(1, "Ricardo", "dia", 1, datetime), 0)

    def testaEncerraAluguelDataInvalida(self):
        print("\nTeste de Locadora receber ecerramento de aluguel com a data inválida.")
        self.assertEqual(self.locadora.encerraAluguel(1, datetime), 0)

    def testaEncerraAluguelDataInvalida(self):
        print("\nTeste de Locadora receber ecerramento de aluguel com a data inválida.")
        self.assertEqual(self.locadora.encerraAluguel(1, datetime), 0)
