from Telas.abstract_tela import AbstractTela
import PySimpleGUI as sg


class TelaReceitaRelatorio(AbstractTela):

    def __init__(self):
        self.__window = None

    def init_components(self, relatorio):
        layout = [[sg.Text('LOG DE RECEITAS')],
                  [sg.Text(relatorio)],
                  [sg.Button('Retornar ao Menu de Receitas', key='retornar')]]

        self.__window = sg.Window('Tela de Relatório', location=(500, 300)).Layout(layout)

    def abre_tela(self, relatorio):
        self.init_components(relatorio)
        button, values = self.__window.Read()
        if button is None:
            exit(0)
        self.__window.Close()
        return

    # ------ MÉTODOS TRATAMENTO EXCEÇÕES ------

    def erro_ja_cadastrado(self, nome):
        pass
