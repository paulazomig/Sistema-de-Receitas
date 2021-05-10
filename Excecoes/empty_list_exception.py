import PySimpleGUI as sg


class EmptyListException(Exception):
    def __init__(self):
        sg.Popup("Lista Vazia", "Ainda não há nenhum registro desse item no sistema.", location=(500,300))
        return
