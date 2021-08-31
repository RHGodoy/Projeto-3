from datetime import datetime, timedelta

class Locadora(object):
    def __init__(self, estoque, custoHora, custoDia, custoSemana):
        self.estoque = estoque
        self.numClientes = 0 # Número de clientes cadastrados
        self.alugueisAtivos = {} # Dict de dict que armazena os aluguéis ativos
        self.custoHora = custoHora
        self.custoDia = custoDia
        self.custoSemana = custoSemana
        self.clientes = {} # dict que armazena clientes onde a chave é o idCliente

    def criaCliente(self,nome):
        """
        Cria cliente e atribui um id para controle, adciona novo cliente a listas de clientes da locadora
        :param nome: str
        :param qtdeBikes: int
        :return: objeto da classe cliente
        """
        self.numClientes += 1
        self.clientes[self.numClientes] = Cliente(nome=nome, idCliente=self.numClientes)
        print(f'O cliente {nome} foi criado com sucesso!')
        return self.clientes[self.numClientes]

    def novoAluguel(self, idCliente,nome, modalidade,qtdeBikes,dataInicio):
        """
        Cria novo aluguel e armazena dados em self.alugueisAtivos
        :param idCliente: int
        :param modalidade: str
        :param qtdeBikes: int
        :param dataInicio: datetime
        :return: bool
        """
        try:
            if qtdeBikes <= 0:
                raise ValueError("Quantidade invalida")

            if qtdeBikes > self.estoque:
                raise SystemError("Estoque indisponivel")

            self.estoque -= qtdeBikes
            self.alugueisAtivos[idCliente] = {'nome': nome,
                                              'modalidade': modalidade,
                                              'qtdeBikes': qtdeBikes,
                                              'inicio':dataInicio}

        except ValueError:
            print(f"Locadora - Aluguel de {qtdeBikes} bicicletas não efetuado por quantidade inválida. Estoque: {self.estoque}")
            return 0
        except SystemError:
            print(f"Locadora - Aluguel de {qtdeBikes} biciletas não efetuado por falta de estoque. Estoque: {self.estoque}")
            return 0
        except:
            print(f"Locadora - Aluguel de {qtdeBikes} biciletas não efetuado. Estoque: {self.estoque}")
            return 0

        return True

    def encerraAluguel(self, idCliente, dataFim, numBikes=1):
        """
        Encerra o aluguel e retorna valor a ser cobrado
        :param idCliente: int
        :param dataFim: datetime
        :return: float or False
        """
        dadosAluguel = self.alugueisAtivos[idCliente]
        dataInicio = dadosAluguel['inicio']
        modalidade = dadosAluguel['modalidade']
        qtdeBikesAlugadas = dadosAluguel['qtdeBikes']

        # Calcula tempo do aluguel
        tempoAluguel = dataFim - dataInicio
        if tempoAluguel.total_seconds() < 0:
            print("Data de entrega menor que data de início")
            return False


        if modalidade == 'hora':
            horasAlugadas, restoSegundos = divmod(tempoAluguel.total_seconds(),3600) # retorna horas
            minutosAlugados = restoSegundos // 60 # retorna minutos que exceram número inteiro de horas
            # Se exceder quinze minutos é cobrado a próxima hora
            if minutosAlugados > 15:
                horasAlugadas += 1
            custo = horasAlugadas * self.custoHora * numBikes
        elif modalidade == 'dia':
            diasAlugados = tempoAluguel.days
            horasAlugadas = tempoAluguel.seconds // 3600 # horas que excederam número inteiro de dias
            # Se exceder duas horas ou se entregar antes de um dia cobra um novo dia
            if horasAlugadas > 2 or diasAlugados == 0:
                diasAlugados += 1
            custo = diasAlugados * self.custoDia * numBikes
        elif modalidade == 'semana':
            semanasAlugados = tempoAluguel.days // 7
            diasAlugados = tempoAluguel.days % 7
            # Se exceder um dia ou se entregar antes de uma seman cobra uma nova semana
            if diasAlugados > 1 or semanasAlugados == 0:
                semanasAlugados += 1
            custo = semanasAlugados * self.custoSemana * numBikes

        # Aplica desconto se qtde de bikes alugadas for maior que 3
        if qtdeBikesAlugadas >= 3:
            custo = custo * 0.7

        # Devolve bicicleta para estoque
        self.estoque += numBikes
        return custo

class Cliente(object):
    def __init__(self, nome, idCliente):
        self.nome = nome
        self.idCliente = idCliente

    def consultaEstoque(self,Locadora):
        """
        Retorna número de bicicletas disponíveis
        :param objetoLocadora: object Cliente
        :return: int
        """
        return Locadora.estoque

    def alugaBike(self,objLocadora,qtdeBikes,modalidade,dataInicio=None):
        """
        ALuga bicicletas
        :param Locadora: objeto Locadora
        :param dataInicio: datetime
        :param qtdeBikes: int
        :param modalidade: str
        :return: bool
            Retorno indica sucesso na tentativa de aluguel
        """
        # Verifica se modalidade é válida
        if modalidade.lower() not in ['hora','dia','semana']:
            print('Modalidade inválida')
            return False

        # se não for passado nenhuma data a data inicio será o momento de chamada do método
        if dataInicio == None:
            self.dataInicio = datetime.now()
        # verifica se a dataInicio é um objeto datetime
        elif isinstance(dataInicio,datetime):
            self.dataInicio = dataInicio
        else:
            print('Data inválida')
            return False

        # Verifica disponibilidade de bicicletas
        if qtdeBikes < objLocadora.estoque:
            self.qtdeBikes = qtdeBikes
        else:
            print('Quantidade de bicicletas indisponível')
            print('Quantidade disponível na loja é:',objLocadora.estoque)
            return False

        self.modalidade = modalidade

        return Locadora.novoAluguel(idCliente=self.idCliente,
                                    nome=self.nome,
                                    modalidade=self.modalidade,
                                    qtdeBikes=self.qtdeBikes,
                                    dataInicio=self.dataInicio)

    def devolveBike(self,objLocadora, dataFim=None):
        if dataFim == None:
            self.dataFim = datetime.now()
        elif isinstance(dataFim,datetime):
            self.dataFim = dataFim
        else:
            print('Data inválida')
            return False

        custo = objLocadora.encerraAluguel(idCliente=self.idCliente, dataFim=self.dataFim, numBikes = self.qtdeBikes)
        print("O valor do aluguel foi de R$",custo)

        return True

def validaEntradaNovoAluguel(objLocadora):
    """

    :param Locadora: objeto da classe Locadora
    :return:
            idCliente: int
            qtdeBikes: int
            modalidade: str
    """
    # Recebe id do cliente
    while True:
        try:
            idCliente = int(input('Digite id do cliente (caso não saiba digite 0 para listar clientes):\n'))
        except:
            print('Entrada deve ser um número inteiro')
        if idCliente in Locadora.clientes:
            break
        elif idCliente == 0:
            for key,value in Locadora.clientes.items():
                print(f'Id do cliente: {value.idCliente}\nNome do cliente: {value.nome}')
        else:
            print('Cliente inexistente')
    # Recebe quantidade de bicicletas
    while True:
        try:
            qtdeBikes = int(input('Digite número de bikes para aluguar:\n'))
        except:
            print('Digite um número inteiro')
        if qtdeBikes > Locadora.estoque:
            print(f'Quantidade desejada menor que quantidade disponível: {Locadora.estoque}')
        elif qtdeBikes <= 0:
            print('Quantidade inválida, digite novamente')
        else:
            break
    # Recebe modalidade:
    while True:
        modalidade = input('Selecione uma das modalidades (hora, dia e semana):\n')
        if modalidade.lower() in ['hora', 'dia', 'semana']:
            break
        else:
            print('Modalidade inválida')

    return idCliente,qtdeBikes,modalidade


def validaEntradaEncerraAluguel(Locadora):
    """

    :param Locadora: objeto da classe Locadora
    :return:
            idCliente: int
    """
    # Recebe id do cliente
    while True:
        try:
            idCliente = int(input('Digite id do cliente (caso não saiba digite 0 para listar clientes:\n'))
        except:
            print('Entrada deve ser um número inteiro')
        if idCliente in Locadora.clientes:
            break
        elif idCliente == 0:
            for key,value in Locadora.clientes.items():
                print(f'Id do cliente: {value.idCliente}\nNome do cliente: {value.nome}')
        else:
            print('Cliente inexistente')

    return idCliente


def main():
    # Cria locadora
    estoque = 10
    custoHora = 5                   # retirado do enunciado do projeto
    custoDia = 25                   # retirado do enunciado do projeto
    custoSemana = 100               # retirado do enunciado do projeto
    locadora = Locadora(estoque=estoque,custoHora=custoHora,custoDia=custoDia,custoSemana=custoSemana)

    # Menu de opções
    while True:
        while True:
            try:
                entradaUsuario = int(input("""
                Selecione uma das opções abaixo (digite o número):
                1 - Criar novo cliente;
                2 - Alugar bicicleta;
                3 - Devolver bicicleta;
                4 - Imprimir dados aluguéis ativos
                5 - Imprimir dados clientes 
                6 - Encerrar programa.
                
                Sua opção: """))
                if entradaUsuario in range(1,7):
                    break
            except:
                print('Entrada inválida')

        # Cria Cliente
        if entradaUsuario == 1:
            nome = input('Digite o nome do cliente:\n')
            locadora.criaCliente(nome=nome)

        # NovoAluguel
        elif entradaUsuario == 2:
            idCliente, qtdeBikes, modalidade = validaEntradaNovoAluguel(locadora)
            # Cria data de início:
            dataInicio = datetime.now()
            # Cria novo aluguel
            locadora.clientes[idCliente].alugaBike(objLocadora=locadora,
                                                   qtdeBikes=qtdeBikes,
                                                   modalidade=modalidade,
                                                   dataInicio=dataInicio)
        # Encerra aluguel
        elif entradaUsuario == 3:
            idCliente = validaEntradaEncerraAluguel(locadora)
            dataFim = datetime.now()
            locadora.clientes[idCliente].devolveBike(objLocadora=locadora, dataFim=dataFim)

        # Imprime dados aluguéis ativos
        elif entradaUsuario == 4:
            print(locadora.alugueisAtivos)

        # Imprime dados clientes
        elif entradaUsuario == 5:
            for key,value in locadora.clientes.items():
                print(f'Id do cliente: {value.idCliente}\nNome do cliente: {value.nome}')

        # Encerra o Programa
        elif entradaUsuario == 6:
            exit("Obrigado por utilizar o programa!")


if __name__ == '__main__':
    main()