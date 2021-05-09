import PySimpleGUI as sg


class NoKeyException(Exception):
    def __init__(self):
        sg.Popup('Não foi encontrado nenhum item com esse nome. Por favor selecionar um item válido no menu.')