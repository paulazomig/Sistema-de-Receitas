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
        dados_receita = self.__tela_receitas.dados_receita()

        nova_receita = Receita(dados_receita["titulo"], dados_receita["ingredientes_quantidades"], dados_receita["preparo"])

        if nova_receita in self.__receitas:
            print("Receita já cadastrada")
            return
        self.__receitas.append(nova_receita)

    def alterar_receita(self):
        pass

    def listar_receita(self):
        pass

    def excluir_receita(self):
        pass

    def retornar_menu_principal(self):
        self.__controlador_sistema.abre_tela()




