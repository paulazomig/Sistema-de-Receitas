from Telas.abstractTela import AbstractTela
import PySimpleGUI as sg


class TelaSistema(AbstractTela):
    def init_components(self):
        sg.ChangeLookAndFeel('LightGreen')
        layout = [[sg.Text('Selecione uma opção:')],
                  [sg.Button('Ingredientes'), sg.Button('Receitas'), sg.Button('Finalizar Sistema')]]

        self.__window = sg.Window('Menu Inicial').Layout(layout)

        button, values = self.__window.Read()
        self.__window.Close()
        return button

    def erro_ja_cadastrado(self, nome):
        pass

    def erro_nao_cadastrado(self, nome):
        pass