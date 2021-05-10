import PySimpleGUI as sg


class NoKeyException(Exception):
    def __init__(self):
        sg.Popup("Erro de Valor", 'Não foi encontrado nenhum item com esse nome. '
                                  'Por favor selecionar um item válido no menu.', location=(500,300))