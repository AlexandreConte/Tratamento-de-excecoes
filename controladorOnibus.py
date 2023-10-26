from abstractControladorOnibus import AbstractControladorOnibus
from comandoInvalidoException import ComandoInvalidoException
from onibus import Onibus


class ControladorOnibus(AbstractControladorOnibus):
    def __init__(self):
        self.__onibus = None

    @property
    def onibus(self) -> Onibus:
        return self.__onibus

    @onibus.setter
    def onibus(self, onibus: Onibus):
        if isinstance(onibus, Onibus):
            self.__onibus = onibus

    def inicializar_onibus(
        self,
        capacidade: int, 
        total_passageiros: int, 
        ligado: bool
    ):
        '''
        Instancia um onibus e atualiza o onibus atual
        Parametros invalidos lanca excecao ComandoInvalidoException
        '''
        self.__valida_parametros_onibus(
            capacidade=capacidade,
            total_passageiros=total_passageiros,
            ligado=ligado
        )
        self.__onibus = Onibus(
            capacidade, total_passageiros, ligado
        )

    def __valida_parametros_onibus(
        self,
        capacidade: int,
        total_passageiros: int,
        ligado: int
    ):
        if (
            not isinstance(capacidade, int) or
            not isinstance(total_passageiros, int) or
            not isinstance(ligado, bool) or
            capacidade <= 0 or
            total_passageiros < 0 or
            total_passageiros > capacidade
        ):
            raise ComandoInvalidoException()

    def ligar(self) -> str:
        return self.__onibus.ligar()

    def desligar(self) -> str:
        return self.__onibus.desligar()

    def embarca_pessoa(self) -> str:
        return self.__onibus.embarca_pessoa()

    def desembarca_pessoa(self) -> str:
        return self.__onibus.desembarca_pessoa()
