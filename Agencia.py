class Agencia:


    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nivel recomendado. Caixa atual: {}'.format(self.caixa))
        else:
            print('O Valor de caixa está ok. Caixa atual: {}'.format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Emprestimo não é possivel. Dinheiro não disponivel em caixa.')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))
    

class AgenciaVirtual(Agencia):
    pass


class AgenciaComum(Agencia):
    pass


class AgenciaPremium(Agencia):
    pass


agencia1 = Agencia(22222233333, 20000000000, 2567)

agencia_virtual = AgenciaVirtual(2222222221444, 45000000000, 6574)
agencia_virtual.caixa = 15000
agencia_virtual.verificar_caixa()

agencia_premium = AgenciaPremium(1265498746315, 46870000000, 6789)
agencia_premium.caixa = 5000000
agencia_premium.verificar_caixa()