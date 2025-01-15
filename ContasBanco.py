class ContaCorrente:

    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta

    def consultar_saldo(self):
        print('Seu saldo atual é R${:,.2f}'.format(self.saldo))

    def depositar(self, valor):
        self.saldo += valor
        self.consultar_saldo()

    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self, valor):
        if self.saldo - valor < self._limite_conta():
            print('Você não tem saldo suficiente para sacar esse valor!')
            self.consultar_saldo()
        else:
            self.saldo -= valor

    def consultar_limite_chequesespecial(self):
        print('Seu limite de Cheque Especial é de R${:,.2f}'.format(self._limite_conta()))


# Criando conta
conta_Thiago = ContaCorrente('Thiago', '111.222.333-45', 123, 12345)

# Mostrar saldo
conta_Thiago.consultar_saldo()

# Depositando dinheiro na conta
conta_Thiago.depositar(10000)

# Sacar dinheiro na conta
conta_Thiago.sacar_dinheiro(10020)

print('Saldo Final')
conta_Thiago.consultar_saldo()
conta_Thiago.consultar_limite_chequesespecial()