from datetime import datetime
import unittest
from locadora import Locadora, Cliente

class testes(unittest.TestCase):
    def setUp(self):
        self.locadora = Locadora(10, 5, 25, 100)
        self.cliente = self.locadora.criaCliente("Ricardo")

    #Testes relacionados ao Cliente.

    def testeConsultaEstoque(self):
        print("\nTeste de cliente consultando estoque.")
        self.assertEqual(self.cliente.consultaEstoque(self.locadora), self.locadora.estoque)

    def testeAlugaBikeErrodeModalidade(self):
        print("\nTeste de aluguel solicitado com erro de modalidade.")
        self.assertEqual(self.cliente.alugaBike(self.locadora, 1, "minutos", datetime.now()), 0)

    def testeAlugaBikeSemData(self):
        print("\nTeste de aluguel sem colocar data de início.")
        self.assertEqual(self.cliente.alugaBike(self.locadora, 1, "hora", dataInicio=None), True)

    def testeAlugaBikeDataInvalida(self):
        print("\nTeste de aluguel solicitado com data inválida.")
        self.assertEqual(self.cliente.alugaBike(self.locadora, 1, "hora", "hoje"), False)

    def testeAlugaMaisBikeQueEstoque(self):
        print("\nTeste de aluguel solicitado com data inválida.")
        self.assertEqual(self.cliente.alugaBike(self.locadora, 11, "hora", "hoje"), False)

    def testeAlugaQtdeNegativa(self):
        print("\nTeste de aluguel solicitado com data inválida.")
        self.assertEqual(self.cliente.alugaBike(self.locadora, -1, "hora", "hoje"), False)

    def testeAlugaBike(self):
        print("\nTeste de aluguel feito corretamente.")
        self.assertEqual(self.cliente.alugaBike(self.locadora, 1, "hora", datetime.now()), True)
        print(self.locadora.alugueisAtivos)

    def testeDevolveBikeHora(self):
        print("\nTeste de devolução de bike de 1 hora.")
        self.cliente.alugaBike(self.locadora, 1, "hora", dataInicio=datetime(2021, 8, 30, 20, 14, 56, 828248))
        print(self.locadora.alugueisAtivos)
        self.assertEqual(self.cliente.devolveBike(self.locadora, dataFim=datetime(2021, 8, 30, 21, 14, 56, 828248)), True)

    def testeDevolveBikeDia(self):
        print("\nTeste de devolução de bike.")
        self.cliente.alugaBike(self.locadora, 1, "hora", dataInicio=datetime(2021, 8, 30, 20, 14, 56, 828248))
        print(self.locadora.alugueisAtivos)
        self.assertEqual(self.cliente.devolveBike(self.locadora, dataFim=datetime(2021, 8, 30, 21, 14, 56, 828248)), True)


    def testeDevolveBikeDataErrada(self):
        print("\nTeste de devolução de bike.")
        self.cliente.alugaBike(self.locadora, 1, "hora", dataInicio=datetime(2021, 8, 30, 20, 14, 56, 828248))
        print(self.locadora.alugueisAtivos)
        self.assertEqual(self.cliente.devolveBike(self.locadora, dataFim='aleatoria'), False)


    #Testes relacionados a Locadora

    def testaCriaNovoCliente(self):
        print("\nTeste de criação do cliente no sistema.")
        self.assertEqual(type(self.locadora.criaCliente("Ricardo")), type(self.cliente))

    def testaNovoAluguelSemEstoque(self):
        print("\nTeste de Locadora receber pedido de aluguel sem estoque.")
        self.assertEqual(self.locadora.novoAluguel(1, "Ricardo", "dia", 11, dataInicio=None), 0)

    def testaNovoAluguelQuantidadeInvalida(self):
        print("\nTeste de Locadora receber pedido de aluguel de quantidade inválida.")
        self.assertEqual(self.locadora.novoAluguel(1, "Ricardo", "dia", -2, dataInicio=None), 0)

    def testaNovoAluguel(self):
        print("\nTeste de Locadora receber pedido de aluguel.")
        self.assertEqual(self.locadora.novoAluguel(1, "Ricardo", "dia", 1, dataInicio=None), True)

    def testaEncerraAluguelHora(self):
        print("\nTeste de Locadora modalidade hora.")
        self.cliente.alugaBike(self.locadora, 1, "hora", dataInicio=datetime(2021, 8, 30, 20, 14, 56, 828248))
        self.assertEqual(self.locadora.encerraAluguel(idCliente=1, dataFim=datetime(2021, 8, 30, 22, 14, 56, 828248)), 10)

    def testaEncerraAluguelDia(self):
        print("\nTeste de Locadora modalidade dia.")
        self.cliente.alugaBike(self.locadora, 1, "dia", dataInicio=datetime(2021, 8, 30, 20, 14, 56, 828248))
        self.assertEqual(self.locadora.encerraAluguel(idCliente=1, dataFim=datetime(2021, 8, 31, 20, 14, 56, 828248)), 25)

    def testaEncerraAluguelSemana(self):
        print("\nTeste de Locadora modalidade semana.")
        self.cliente.alugaBike(self.locadora, 1, "semana", dataInicio=datetime(2021, 8, 30, 20, 14, 56, 828248))
        self.assertEqual(self.locadora.encerraAluguel(idCliente=1, dataFim=datetime(2021, 9, 6, 22, 14, 56, 828248)), 100)

    def testaEncerraAluguelSemanaFamilia(self):
        print("\nTeste de Locadora modalidade semana com desconto por ser família.")
        self.cliente.alugaBike(self.locadora, 4, "semana", dataInicio=datetime(2021, 8, 30, 20, 14, 56, 828248))
        self.assertEqual(self.locadora.encerraAluguel(idCliente=1, dataFim=datetime(2021, 9, 6, 22, 14, 56, 828248),
                                                      numBikes=4), 280)

    def testaEncerraAluguel(self):
        print("\nTeste de Locadora receber ecerramento de aluguel com a data inválida.")
        self.cliente.alugaBike(self.locadora, 1, "hora", dataInicio=datetime(2021, 8, 30, 20, 14, 56, 828248))
        print(self.locadora.alugueisAtivos)
        self.assertEqual(self.locadora.encerraAluguel(idCliente=1, dataFim=datetime(2021, 8, 30, 22, 14, 56, 828248)), 10)


