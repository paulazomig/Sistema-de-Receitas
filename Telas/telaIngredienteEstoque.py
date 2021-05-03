from Telas.abstractTela import AbstractTela
import PySimpleGUI as sg


class TelaIngredienteEstoque(AbstractTela):
    sg.ChangeLookAndFeel('LightGreen')

    def init_components(self, lista_ingredientes):
        layout = [[sg.Text(lista_ingredientes)],
                  [sg.Button('Retornar ao Menu de Ingredientes')]]

        self.__window = sg.Window('Estoque de Ingredientes', default_element_size=(40, 1)).Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()

    def erro_ja_cadastrado(self, nome):
        pass

    def erro_nao_cadastrado(self, nome):
        pass