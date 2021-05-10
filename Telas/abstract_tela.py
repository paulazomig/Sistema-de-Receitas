from abc import ABC, abstractmethod
import PySimpleGUI as sg


class AbstractTela(ABC):
    sg.ChangeLookAndFeel('LightGreen')

    def feedback_sucesso(self):
        sg.Popup("Sucesso", "Ação realizada com sucesso.",location=(500,300))

    def erro_valor(self):
        sg.Popup("Erro de Valor", "O valor inserido deve ser um número. Tente novamente.", location=(500,300))

    def erro_branco(self):
        sg.Popup("Espaço em Branco", "Por favor preencher todos os campos", location=(500,300))

    @abstractmethod
    def erro_ja_cadastrado(self, nome):
        pass
