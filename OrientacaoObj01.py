# Primeira Classe

class TV:
    
    cor = 'preta'

    def __init__(self,tamanho):
        self.ligada = True
        self.tamanho = tamanho
        self.canal = 'Netflix'
        self.volume = 10
    
    def mudar_canal(self, novo_canal):
        self.canal = novo_canal

tv_sala = TV(50)
tv_quarto = TV(55)

print(tv_quarto.tamanho)
print(tv_sala.tamanho)

print(tv_sala.cor)