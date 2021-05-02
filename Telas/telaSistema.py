from Telas.abstractTelaExcecoes import AbstractTela


class TelaSistema(AbstractTela):
    def opcoes(self):
        print("Escolha Opção:\n1. Ingredientes\n2. Receitas\n0. Finalizar Sistema")
        opcao = int(input())
        return opcao

    def erro_ja_cadastrado(self, nome):
        pass

    def erro_nao_cadastrado(self, nome):
        pass