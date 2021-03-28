from Controladores.controladorIngrediente import ControladorIngrediente
from Telas.telaSistema import TelaSistema


class ControladorSistema:
    def __init__(self):
        self.__controlador_ingredientes = ControladorIngrediente(self)
        self.__tela_sistema = TelaSistema()

    def inicializa_sistema(self):
        self.abre_tela()

    def encerrar_sistema(self):
        exit(0)

    def abre_tela(self):
        opcao_escolhida = self.__tela_sistema.opcoes()

        if opcao_escolhida == 1:
            self.__controlador_ingredientes.abre_tela()

        if opcao_escolhida == 2:
            pass

        if opcao_escolhida == 0:
            self.encerrar_sistema()



