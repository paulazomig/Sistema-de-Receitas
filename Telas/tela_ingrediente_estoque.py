from Telas.abstract_tela import AbstractTela
import PySimpleGUI as sg


class TelaIngredienteEstoque(AbstractTela):

    def __init__(self):
        self.__window = None
        self.init_components(None)

    def init_components(self, infos_estoque):
        layout = [[sg.Text(infos_estoque)],
                  [sg.Button('Retornar ao Menu de Ingredientes')]]

        self.__window = sg.Window('Estoque de Ingredientes', location=(500,300), size=(400, 300), resizable=True).Layout(layout)

    def abre_tela(self, infos_estoque):
        self.init_components(infos_estoque)
        button, values = self.__window.Read()
        if button is None:
            exit(0)

        self.__window.Close()

    # ------ MÉTODOS TRATAMENTO EXCEÇÕES ------

    def erro_ja_cadastrado(self, nome):
        pass
