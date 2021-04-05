from Telas.abstractTelaExcecoes import AbstractTelaExcecoes


class TelaSistema(AbstractTelaExcecoes):
    def opcoes(self):
        print("Escolha Opção:\n1. Ingredientes\n2. Receitas\n0. Finaliza Sistema")
        opcao = int(input())
        return opcao

    def erro_ja_cadastrado(self):
        pass

    def erro_nao_cadastrado(self):
        pass