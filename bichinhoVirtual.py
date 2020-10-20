class BichinhoVirtual:
    def __init__(self,nome,fome=0,saude=30,idade=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alimentar(self):
        self.fome = self.fome + 10

    def remedio(self):
        self.saude = self.saude + 15

    def trocarNome(self,novoNome):
        self.nome = novoNome

    def envelhecer(self):
        self.idade = self.idade + 10

    def adoecer(self):
        self.saude = self.saude - 15
