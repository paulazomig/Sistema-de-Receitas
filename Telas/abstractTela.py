from abc import ABC, abstractmethod
import PySimpleGUI as sg


class AbstractTela(ABC):
    def feedback_sucesso(self):
        sg.Popup("Sucesso", "Ação realizada com sucesso.")

    def erro_menu(self):
        sg.Popup("ATENÇÃO", "O valor inserido não é válido. Por favor digite um valor indicado no menu.")

    def erro_lista_vazia(self):
        sg.Popup("Lista Vazia", "Não há nenhum registro deste item.")

    def erro_valor(self):
        sg.Popup("Erro de Valor", "O valor inserido deve ser um número.")

    def erro_branco(self):
        sg.Popup("Espaço em Branco", "Por favor preencher todos os campos")

    @abstractmethod
    def erro_nao_cadastrado(self, nome):
        pass

    @abstractmethod
    def erro_ja_cadastrado(self, nome):
        pass