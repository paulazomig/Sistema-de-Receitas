from Telas.abstract_tela import AbstractTela
import PySimpleGUI as sg


class TelaIngrediente(AbstractTela):

    def __init__(self):
        self.__window = None
        self.init_components(None)

    def init_components(self, cb_lista):
        layout = [[sg.Text('Selecione uma opção:')],
                  [sg.Text('Ingredientes:'), sg.InputCombo(cb_lista, size=(30,1), key='cb_opcao')],
                  [sg.Button('Cadastrar Ingrediente', key='cadastro'),
                   sg.Button('Alterar Ingrediente', key='alteracao'),
                   sg.Button('Excluir Ingrediente', key='exclusao'),
                   sg.Button('Ver Estoque', key='estoque')],
                  [sg.Button('Retornar ao Menu Principal', key='retorna')]]

        self.__window = sg.Window('Opções Ingredientes', location=(400,300), element_justification='center').Layout(layout)

    def abre_tela(self, cb_lista):
        self.init_components(cb_lista)
        button, values = self.__window.Read()
        return button, values

    def fecha_tela(self):
        self.__window.Close()

    # ------ MÉTODOS TRATAMENTO EXCEÇÕES ------

    def erro_ja_cadastrado(self, nome):
        pass
