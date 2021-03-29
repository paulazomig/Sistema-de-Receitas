from Entidades.receita import Receita
from Telas.telaReceita import TelaReceita

class ControladorReceita:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_receitas = TelaReceita()
        self.__receitas = []

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_receita, 2: self.alterar_receita, 3: self.listar_receita, 4: self.excluir_receita,
                        0: self.retornar_menu_principal}
        while True:
            lista_opcoes[self.__tela_receitas.tela_opcoes()]()

    def cadastrar_receita(self):
        obter_dados_receita = self.__tela_receitas.obter_dados_receita()

        nova_receita = Receita(obter_dados_receita["titulo"], obter_dados_receita["ingredientes_quantidades"], obter_dados_receita["preparo"])

        if nova_receita in self.__receitas:
            print("Receita já cadastrada")
            return
        self.__receitas.append(nova_receita)

    def alterar_receita(self):
        pass

    def listar_receita(self):
        pass

    def fazer_receita:
        pass

    def excluir_receita(self):
        titulo_receita_deletada = self.__tela_receitas.excluir_receita()
        for receita in self.__receitas:
            if receita.titulo == titulo_receita_deletada:
                self.__receitas.remove(receita)
                del receita

    def retornar_menu_principal(self):
        self.__controlador_sistema.abre_tela()




