CONSFOME = 10
CONSSAUDE = 15
CONSIDADE = 10

class BichinhoVirtual:
    def __init__(self,nome,fome=0,saude=30,idade=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alimentar(self):
        self.fome = self.fome + CONSFOME

    def remedio(self):
        self.saude = self.saude + CONSSAUDE

    def trocarNome(self,novoNome):
        self.nome = novoNome

    def envelhecer(self):
        self.idade = self.idade + CONSIDADE

    def adoecer(self):
        self.saude = self.saude - CONSSAUDE
