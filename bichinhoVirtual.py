CONSFOME = 10
CONSSAUDE = 15
CONSIDADE = 10

class BichinhoVirtual:
    def __init__(self,nome,fome=0,saude=30,idade=0):
        self.__nome = nome
        self.__fome = fome
        self.__saude = saude
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @property
    def fome(self):
        return self.__fome

    def alimentar(self):
        self.__fome = self.__fome + CONSFOME



    @property
    def saude(self):
        return self.__saude

    def remedio(self):
        self.__saude = self.__saude + CONSSAUDE



    def trocarNome(self,novoNome):
        self.__nome = novoNome



    @property
    def idade(self):
        return self.__idade

    def envelhecer(self):
        self.__idade = self.__idade + CONSIDADE


    def adoecer(self):
        self.__saude = self.__saude - CONSSAUDE




