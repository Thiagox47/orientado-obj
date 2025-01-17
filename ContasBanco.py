from datetime import datetime
import pytz
from random import randint


class ContaCorrente:
    """
    Cria uma objeto ContaCorrente para gerenciar as contas dos clientes.

    Atributos:
        nome (str): Nome do cliente
        cpf (str): CPF do cliente. Deve ser inserido com pontos e traços
        _agencia (str): _Agencia responsável pela conta do cliente
        _num_conta (str): Número da conta corrente do cliente
        _saldo (int): _Saldo disponivel na conta do cliente
        _limite (int): _Limite de cheque especial daquele cliente
        _transacoes (str): Histórico de transações do cliente
    """


    @staticmethod
    def _data_hora():
        fuso_Br = pytz.timezone('Brazil/East')
        horario_Br = datetime.now(fuso_Br)
        return horario_Br.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, _agencia, _num_conta):
        self.nome = nome
        self.cpf = cpf
        self._saldo = 0
        self._limite = None
        self._agencia = _agencia
        self._num_conta = _num_conta
        self._transacoes = []
        self.cartoes = []

    def consultar__saldo(self):
        print('Seu _saldo atual é R${:,.2f}'.format(self._saldo))

    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))

    def __limite_conta(self):
        self._limite = -1000
        return self._limite

    def sacar_dinheiro(self, valor):
        if self._saldo - valor < self.__limite_conta():
            print('Você não tem _saldo suficiente para sacar esse valor!')
            self.consultar__saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))

    def consultar__limite_chequesespecial(self):
        print('Seu _limite de Cheque Especial é de R${:,.2f}'.format(self.__limite_conta()))

    def consultar_historico__transacoes(self):
        print('Histórico de Transações')
        for transacao in self._transacoes:
            print(transacao)

    def transferir(self,valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))


class CartaoCredito:
        

    @staticmethod
    def _data_hora():
        fuso_Br = pytz.timezone('Brazil/East')
        horario_Br = datetime.now(fuso_Br)
        return horario_Br

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        self.cod_seguranca = '{}{}{}'.format(randint(0, 9),randint(0, 9),randint(0, 9))
        self.limite = 1000
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print('Nova senha invalida!')

            