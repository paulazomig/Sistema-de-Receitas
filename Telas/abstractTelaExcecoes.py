from abc import ABC, abstractmethod


class AbstractTelaExcecoes(ABC):
    def erro_menu(self):
        print("ATENÇÃO\nO valor inserido não é válido. Por favor digite um número indicado no menu.\n")
        return

    @abstractmethod
    def erro_nao_cadastrado(self):
        pass

    @abstractmethod
    def erro_ja_cadastrado(self):
        pass