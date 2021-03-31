from Entidades.receita import Receita
from Entidades.ingrediente import Ingrediente
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
        dados_receita = self.__tela_receitas.obter_dados_receita()

        ingredientes = {}
        for nome_ingrediente in dados_receita["ingredientes_quantidades"]:
            ingredientes[Ingrediente(nome_ingrediente, unidade_medida), dados_receita["ingredientes_quantidades"][nome_ingrediente])]

        nova_receita = Receita(dados_receita["titulo"], ingredientes, dados_receita["preparo"], )

        if nova_receita in self.__receitas:
            print("Receita já cadastrada")
            return
        self.__receitas.append(nova_receita)
        print(self.__receitas) #DELETAR O PRINT DPS


    def alterar_receita(self):
        pass

    def listar_receita(self):
        pass

    def excluir_receita(self):
        titulo_receita_deletada = self.__tela_receitas.excluir_receita()
        for receita in self.__receitas:
            if receita.titulo == titulo_receita_deletada:
                self.__receitas.remove(receita)
                del receita
                print(self.__receitas) #DELETAR O PRINT DPS

    def retornar_menu_principal(self):
        self.__controlador_sistema.abre_tela()