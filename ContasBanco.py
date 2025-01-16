from datetime import datetime
import pytz


class ContaCorrente:
    """
    Cria uma objeto ContaCorrente para gerenciar as contas dos clientes.

    Atributos:
        _nome (str): _Nome do cliente
        _cpf (str): _CPF do cliente. Deve ser inserido com pontos e traços
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

    def __init__(self, _nome, _cpf, _agencia, _num_conta):
        self._nome = _nome
        self._cpf = _cpf
        self._saldo = 0
        self._limite = None
        self._agencia = _agencia
        self._num_conta = _num_conta
        self._transacoes = []

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


# Criando conta
conta_Thiago = ContaCorrente('Thiago', '111.222.333-45', 123, 12345)

# Mostrar _saldo
conta_Thiago.consultar__saldo()

# Depositando dinheiro na conta
conta_Thiago.depositar(10000)

# Sacar dinheiro na conta
conta_Thiago.sacar_dinheiro(1000)

print('_Saldo Final')
conta_Thiago.consultar__saldo()
conta_Thiago.consultar__limite_chequesespecial()

print('-' *20)
conta_Thiago.consultar_historico__transacoes()

print('-' *20)
conta_Joao = ContaCorrente('João', '222.333.444-56', 5555, 4444444)
conta_Thiago.transferir(1000,conta_Joao)

conta_Thiago.consultar__saldo()
conta_Joao.consultar__saldo()

conta_Thiago.consultar_historico__transacoes()
conta_Joao.consultar_historico__transacoes()