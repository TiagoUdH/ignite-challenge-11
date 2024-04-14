from abc import ABC, abstractmethod

class AprovaExame(ABC):
    @abstractmethod
    def aprovar_solicitacao(self, exame):
        pass
    
    @abstractmethod
    def verifica_condicoes(self, exame):
        pass

class AprovaExameSangue(AprovaExame):
    def aprovar_solicitacao(self, exame):
        if self.verifica_condicoes(exame):
            print("Exame sanguíneo aprovado!")

    def verifica_condicoes(self, exame):
        pass

class AprovaRaioX(AprovaExame):
    def aprovar_solicitacao(self, exame):
        if self.verifica_condicoes(exame):
            print("Raio-X aprovado!")

    def verifica_condicoes(self, exame):
        pass

class Exame:
    def __init__(self, tipo):
        self.tipo = tipo

exame_sangue = Exame("sangue")
exame_raio_x = Exame("raio-x")

aprovador_sangue = AprovaExameSangue()
aprovador_raio_x = AprovaRaioX()

aprovador_sangue.aprovar_solicitacao(exame_sangue)
aprovador_raio_x.aprovar_solicitacao(exame_raio_x)