from Entidades.receita import Receita
from Controladores.controladorIngrediente import ControladorIngrediente
from Telas.telaReceita import TelaReceita


class ControladorReceita:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_ingrediente = self.__controlador_sistema.controlador_ingrediente
        self.__tela_receitas = TelaReceita()
        self.__lista_receitas = []

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_receita, 2: self.alterar_receita, 3: self.listar_receita, 4: self.excluir_receita,
                        0: self.retornar_menu_principal}
        while True:
            lista_opcoes[self.__tela_receitas.tela_opcoes()]()

    def cadastrar_receita(self):
        dados_receita = self.__tela_receitas.obter_dados_receita()

        ingredientes_receita = {}
        print(self.__controlador_ingrediente.listaaa_ingredientes)

        for nome_ingrediente in dados_receita["ingredientes_e_quantidades"]:

            for i in self.__controlador_ingrediente.listaaa_ingredientes:
                add_ingrediente = None
                if i.nome == nome_ingrediente:
                    add_ingrediente = i
                    ingredientes_receita[add_ingrediente.nome] = dados_receita["ingredientes_e_quantidades"][nome_ingrediente]
        print(ingredientes_receita)
        nova_receita = Receita(dados_receita["titulo"], ingredientes_receita, dados_receita["preparo"])

        if nova_receita in self.__lista_receitas:
            print("Receita já cadastrada")
            return
        self.__lista_receitas.append(nova_receita)
        print(self.__lista_receitas) #DELETAR O PRINT DPS

    def alterar_receita(self):
        alterar_receita = self.__tela_receitas.alterar_receita()
        for receita in self.__lista_receitas:
            if receita.titulo == alterar_receita["titulo"]:
                dados_receita = self.__tela_receitas.obter_dados_receita()
                receita.titulo = dados_receita["titulo"]
                receita.ingredientes_quantidades = dados_receita["ingredientes_e_quantidades"]
                receita.preparo = dados_receita["preparo"]


    def listar_receita(self):
        pass

    def excluir_receita(self):
        titulo_receita_deletada = self.__tela_receitas.excluir_receita()
        for receita in self.__lista_receitas:
            if receita.titulo == titulo_receita_deletada:
                self.__lista_receitas.remove(receita)
                del receita
                print(self.__lista_receitas) #DELETAR O PRINT DPS

    def retornar_menu_principal(self):
        self.__controlador_sistema.abre_tela()