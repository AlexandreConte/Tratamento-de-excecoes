from abstractControladorOnibus import AbstractControladorOnibus
from comandoInvalidoException import ComandoInvalidoException
from onibus import Onibus


class ControladorOnibus(AbstractControladorOnibus):
    def __init__(self):
        self.__onibus = None
        super().__init__()

    @property
    def onibus(self) -> Onibus:
        return self.__onibus

    @onibus.setter
    def onibus(self, onibus: Onibus):
        if isinstance(onibus, Onibus):
            self.__onibus = onibus

    def inicializar_onibus(self, capacidade: int, total_passageiros: int, ligado: bool):
        '''
        Instancia um onibus e atualiza o onibus atual
        Parametros invalidos lanca excecao ComandoInvalidoException
        '''
        if not isinstance(capacidade, int) or \
            not isinstance(total_passageiros, int) or \
                not isinstance(ligado, bool):
            raise ComandoInvalidoException()
        else:
            self.onibus = Onibus(
                capacidade, total_passageiros, ligado
            )

    def ligar(self) -> str:
        return self.onibus.ligar()

    def desligar(self) -> str:
        return self.onibus.desligar()

    def embarca_pessoa(self) -> str:
        return self.onibus.embarca_pessoa()

    def desembarca_pessoa(self) -> str:
        return self.onibus.desembarca_pessoa()
