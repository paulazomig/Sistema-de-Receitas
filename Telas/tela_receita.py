from Telas.abstract_tela import AbstractTela
import PySimpleGUI as sg


class TelaReceita(AbstractTela):
    def __init__(self):
        self.__window = None
        self.init_components(None)

    def init_components(self, cb_lista):
        layout = [[sg.Text('Selecione uma opção:')],
                  [sg.Text('Receitas:'), sg.InputCombo(cb_lista, size=(30,1), key='cb_opcao')],
                  [sg.Button('Cadastrar Receita', key='cadastro'),
                   sg.Button('Alterar Receita', key='alteracao'),
                   sg.Button('Visualizar Receita', key='view'),
                   sg.Button('Ver Relatório', key='relatorio'),
                   sg.Button('Excluir Receita', key='exclusao')],
                  [sg.Button('Retornar ao Menu Principal', key='retorna')]]

        self.__window = sg.Window('Opções Receitas', location=(400,300), element_justification='center').Layout(layout)

    def abre_tela(self, cb_lista):
        self.init_components(cb_lista)
        button, values = self.__window.Read()
        return button, values

    def fecha_tela(self):
        self.__window.Close()

    # ------ MÉTODOS TRATAMENTO EXCEÇÕES ------

    def erro_ja_cadastrado(self, nome):
        sg.Popup("Item Já Cadastrado",
                 "Não é possível completar a operação -  a receita {} já foi cadastrada.\n".format(nome), location=(500,300))
