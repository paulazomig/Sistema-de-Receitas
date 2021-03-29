from Entidades.ingrediente import Ingrediente
from Telas.telaIngrediente import TelaIngrediente


class ControladorIngrediente:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_ingredientes = TelaIngrediente()
        self.__lista_ingredientes = []

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_ingrediente, 2: self.alterar_ingrediente, 3: self.listar_ingredientes, 0: self.retornar_menu_principal}

        while True:
            lista_opcoes[self.__tela_ingredientes.tela_opcoes()]()

    def cadastrar_ingrediente(self) -> Ingrediente:
        dados_ingrediente = self.__tela_ingredientes.dados_ingrediente()
        novo_ingrediente = Ingrediente(dados_ingrediente["nome"], dados_ingrediente["unidade_medida"])
        if novo_ingrediente in self.__lista_ingredientes:
            print("Ingrediente já cadastrado")
            return
        self.__lista_ingredientes.append(novo_ingrediente)

    def alterar_ingrediente(self):
        alterar_ingrediente = self.__tela_ingredientes.alterar_ingrediente()
        for ingrediente in self.__lista_ingredientes:
            if ingrediente.nome == alterar_ingrediente["nome"]:
                ingrediente.nome = alterar_ingrediente["novo_nome"]
                ingrediente.unidade_medida = alterar_ingrediente["nova_unidade_medida"]

    def listar_ingredientes(self):
        for ingrediente in self.__lista_ingredientes:
            self.__tela_ingredientes.exibir_ingredientes({"nome": ingrediente.nome, "unidade_medida": ingrediente.unidade_medida})

    def retornar_menu_principal(self):
        self.__controlador_sistema.abre_tela()

    @property
    def lista_ingredientes(self):
        return self.__lista_ingredientes