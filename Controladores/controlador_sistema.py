from Controladores.controlador_ingrediente import ControladorIngrediente
from Controladores.controlador_receita import ControladorReceita
from Telas.tela_sistema import TelaSistema


class ControladorSistema:
    def __init__(self):
        self.__controlador_ingredientes = ControladorIngrediente(self)
        self.__controlador_receitas = ControladorReceita(self)
        self.__tela_sistema = TelaSistema()

    def inicializa_sistema(self):
        self.abre_tela()

    def abre_tela(self):
        lista_opcoes = {'ingredientes': self.abre_tela_ingredientes,
                        'receitas': self.abre_tela_receitas,
                        'finalizar': self.encerrar_sistema}

        while True:
            opcao_menu = self.__tela_sistema.abre_tela()
            self.__tela_sistema.fecha_tela()
            if opcao_menu is None:
                self.abre_tela()
            else:
                lista_opcoes[opcao_menu]()

    def abre_tela_ingredientes(self):
        self.__controlador_ingredientes.abre_tela()

    def abre_tela_receitas(self):
        self.__controlador_receitas.abre_tela()

    def encerrar_sistema(self):
        exit(0)

    @property
    def dao_ingrediente(self):
        return self.__controlador_ingredientes.dao
