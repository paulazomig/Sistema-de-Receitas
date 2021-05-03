from abc import ABC, abstractmethod


class AbstractTela(ABC):
    def feedback_sucesso(self):
        print("Ação realizada com sucesso.\n")
        return

    def erro_menu(self):
        print("ATENÇÃO\nO valor inserido não é válido. Por favor digite um valor indicado no menu.\n")
        return

    def erro_lista_vazia(self):
        print("Lista vazia - Não há nenhum registro.\n")
        return

    def erro_valor(self):
        print("O valor inserido deve ser inteiro.\n")
        return

    @abstractmethod
    def erro_nao_cadastrado(self, nome):
        pass

    @abstractmethod
    def erro_ja_cadastrado(self, nome):
        pass