from Telas.abstractTela import AbstractTela
import PySimpleGUI as sg


class TelaSistema(AbstractTela):

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [[sg.Text('Selecione uma opção:', justification='center')],
                  [sg.Button('Ingredientes', key='ingredientes'), sg.Button('Receitas', key='receitas'), sg.Button('Finalizar Sistema', key='finalizar')]]

        self.__window = sg.Window('Menu Inicial', location=(500,300)).Layout(layout)

    def abre_tela(self):
        button, values = self.__window.Read()
        return button

    def fecha_tela(self):
        self.__window.Close()

    def erro_ja_cadastrado(self, nome):
        pass

    def erro_nao_cadastrado(self, nome):
        pass
