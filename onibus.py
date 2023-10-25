from abstractOnibus import AbstractOnibus
from onibusJahCheioException import OnibusJahCheioException
from onibusJahVazioException import OnibusJahVazioException
from onibusJahLigadoException import OnibusJahLigadoException
from onibusJahDesligadoException import OnibusJahDesligadoException


class Onibus(AbstractOnibus):
    def __init__(self, capacidade: int, total_passageiros: int, ligado: bool):
        self.__capacidade = None
        self.__total_passageiros = None
        self.__ligado = None
        if isinstance(capacidade, int):
            self.__capacidade = capacidade
        if isinstance(total_passageiros, int):
            self.__total_passageiros = total_passageiros
        if isinstance(ligado, bool):
            self.__ligado = ligado

    @property
    def capacidade(self) -> int:
        return self.__capacidade

    @capacidade.setter
    def capacidade(self, capacidade: int):
        if isinstance(capacidade, int):
            self.__capacidade = capacidade

    @property
    def total_passageiros(self):
        return self.__total_passageiros

    @total_passageiros.setter
    def total_passageiros(self, total_passageiros: int):
        if isinstance(total_passageiros, int):
            self.__total_passageiros = total_passageiros

    @property
    def ligado(self) -> bool:
        return self.__ligado

    @ligado.setter
    def ligado(self, ligado: bool):
        if isinstance(ligado, bool):
            self.__ligado = ligado

    def ligar(self):
        '''
        Liga o onibus.
        Lanca uma excecao caso jah esteja ligado.
        Caso ligue, retorna "Ligando o onibus!".
        '''
        if self.ligado:
            raise OnibusJahLigadoException()
        else:
            self.ligado = True
            return "Ligando o onibus!"

    def desligar(self):
        '''
        Desliga o onibus.
        Lanca uma excecao caso jah desligado.
        Caso desligue retorna "Desligando o onibus!".
        '''
        desligado = not self.ligado
        if desligado:
            raise OnibusJahDesligadoException()
        else:
            self.ligado = False
            return "Desligando o onibus!"

    def embarca_pessoa(self) -> str:
        '''
        Acrescenta 1 no numero de passageiros do onibus.
        Lanca excecao se estiver cheio.
        '''
        lotado = self.capacidade == self.total_passageiros
        if lotado:
            raise OnibusJahCheioException()
        else:
            self.total_passageiros += 1
            return "Embarcando passageiro!"

    def desembarca_pessoa(self) -> str:
        '''
        Descrescenta 1 no numero de passageiros do onibus.
        Lanca excecao se estiver vazio.
        '''
        if self.total_passageiros == 0:
            raise OnibusJahVazioException()
        else:
            self.total_passageiros -= 1
            return "Desembarcando passageiro!"
