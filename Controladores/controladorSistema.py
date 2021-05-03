from Controladores.controladorIngrediente import ControladorIngrediente
from Controladores.controladorReceita import ControladorReceita
from Telas.telaSistema import TelaSistema


class ControladorSistema:
    def __init__(self):
        self.__controlador_ingredientes = ControladorIngrediente(self)
        self.__controlador_receitas = ControladorReceita(self)
        self.__tela_sistema = TelaSistema()

    def inicializa_sistema(self):
        self.abre_tela()

    def encerrar_sistema(self):
        exit(0)

    def abre_tela(self):
        while True:
            try:
                opcao_escolhida = self.__tela_sistema.init_components()

                if opcao_escolhida == 'Ingredientes':
                    self.__controlador_ingredientes.abre_tela()

                if opcao_escolhida == 'Receitas':
                    self.__controlador_receitas.abre_tela()

                if opcao_escolhida == 'Finalizar Sistema':
                    self.encerrar_sistema()
                else:
                    raise ValueError
            except Exception:
                self.__tela_sistema.erro_menu()
                self.abre_tela()

    @property
    def controlador_ingrediente(self):
        return self.__controlador_ingredientes
