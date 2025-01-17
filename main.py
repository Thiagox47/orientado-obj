from ContasBanco import ContaCorrente
from ContasBanco import CartaoCredito

# Criando conta
conta_Thiago = ContaCorrente('Thiago', '111.222.333-45', 123, 12345)

cartao_Thiago = CartaoCredito('Thiago', conta_Thiago)

cartao_Thiago.senha = '1345'

print(conta_Thiago.consultar__saldo())