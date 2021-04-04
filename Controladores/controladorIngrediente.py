from Entidades.ingrediente import Ingrediente
from Telas.telaIngrediente import TelaIngrediente
from Excecoes.DadoNaoCadastrado import DadoNaoCadastradoException


class ControladorIngrediente:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_ingredientes = TelaIngrediente()
        self.listagem_ingredientes = []

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_ingrediente, 2: self.alterar_ingrediente, 3: self.listar_ingredientes, 0: self.retornar_menu_principal}

        while True:
            try:
                lista_opcoes[self.__tela_ingredientes.tela_opcoes()]()
            except Exception:
                self.__tela_ingredientes.excecoes_ingrediente()
                self.abre_tela()

    def cadastrar_ingrediente(self) -> Ingrediente:
        dados_ingrediente = self.__tela_ingredientes.dados_ingrediente()
        novo_ingrediente = Ingrediente(dados_ingrediente["nome"], dados_ingrediente["unidade_medida"])
        if novo_ingrediente in self.listagem_ingredientes:
            print("Ingrediente já cadastrado")
            return
        self.listagem_ingredientes.append(novo_ingrediente)

    def alterar_ingrediente(self):
        dados_alteracao_ingrediente = self.__tela_ingredientes.alterar_ingrediente()
        ingrediente = self.pega_ingrediente(dados_alteracao_ingrediente["nome"])
        ingrediente.nome = dados_alteracao_ingrediente["novo_nome"]
        ingrediente.unidade_medida = dados_alteracao_ingrediente["nova_unidade_medida"]
        #exception

    def listar_ingredientes(self):
        for ingrediente in self.listagem_ingredientes:
            self.__tela_ingredientes.exibir_ingredientes({"nome": ingrediente.nome, "unidade_medida": ingrediente.unidade_medida})

    def retornar_menu_principal(self):
        self.__controlador_sistema.abre_tela()

    def pega_ingrediente(self, nome: str):
        for ingrediente in self.listagem_ingredientes:
            if ingrediente.nome == nome:
                return ingrediente

    @property
    def lista_ingredientes(self):
        return self.listagem_ingredientes
