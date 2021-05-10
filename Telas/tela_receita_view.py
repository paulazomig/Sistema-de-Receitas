from Telas.abstract_tela import AbstractTela
import PySimpleGUI as sg


class TelaReceitaView(AbstractTela):

    def __init__(self):
        self.__window = None

    def init_components(self, titulo, ingredientes, preparo):
        layout = [[sg.Text('TÍTULO:'), sg.Text(titulo)],
                  [sg.Text('\nINGREDIENTES:')],
                  [sg.Text(ingredientes)],
                  [sg.Text('MODO DE PREPARO:')],
                  [sg.Text(preparo)],
                  [sg.Button('Retornar ao Menu de Receitas', key='retornar'),
                   sg.Button('Fazer Receita', key='fazer')]]

        self.__window = sg.Window('Visualização de Receita', location=(500, 300)).Layout(layout)

    def abre_tela(self, titulo, ingredientes, preparo):
        self.init_components(titulo, ingredientes, preparo)
        button, values = self.__window.Read()
        self.__window.Close()
        if button is None:
            exit(0)
        return button

    # ------ MÉTODOS TRATAMENTO EXCEÇÕES ------

    def erro_ja_cadastrado(self, nome):
        pass

    def erro_ingredientes_insuficientes(self, nome):
        sg.Popup("O ingrediente {} não possui quantidade "
                 "suficiente para essa receita!\n".format(nome), location=(500,300))
