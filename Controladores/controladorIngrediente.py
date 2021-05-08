from Entidades.ingrediente import Ingrediente
from Telas.telaIngrediente import TelaIngrediente
from Telas.telaIngredienteEstoque import TelaIngredienteEstoque
from Telas.telaIngredienteAcoes import TelaIngredienteAcoes


class ControladorIngrediente:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_ingredientes = TelaIngrediente()
        self.__tela_ingredientes_estoque = TelaIngredienteEstoque()
        self.__tela_ingredientes_acoes = TelaIngredienteAcoes()
        self.__lista_ingredientes = []
        self.lista_nome_ingredientes = []

    def abre_tela(self):
        lista_opcoes = {'cadastro': self.cadastrar_ingrediente,
                        'alteracao': self.alterar_ingrediente,
                        'exclusao': self.excluir_ingrediente,
                        'estoque': self.ver_estoque,
                        'retorna': self.retornar_menu_principal}

        while True:
            opcao_menu, valor_menu = self.__tela_ingredientes.abre_tela(self.lista_nome_ingredientes)
            self.__tela_ingredientes.fecha_tela()
            if opcao_menu is None:
                exit(0)

            if opcao_menu == 'alteracao' or opcao_menu == 'exclusao':
                lista_opcoes[opcao_menu](valor_menu['cb_opcao'])
            else:
                lista_opcoes[opcao_menu]()

    def cadastrar_ingrediente(self):
        infos_tela = None

        dados_ingrediente = self.__tela_ingredientes_acoes.abre_tela(infos_tela)
        self.__tela_ingredientes_acoes.fecha_tela()

        if dados_ingrediente is None:
            self.abre_tela()

        novo_ingrediente = Ingrediente(dados_ingrediente["nome"],
                                       dados_ingrediente["unidade_medida"],
                                       dados_ingrediente["quantidade"])

        if novo_ingrediente in self.__lista_ingredientes:
            self.__tela_ingredientes_acoes.erro_ja_cadastrado(novo_ingrediente.nome)
            return
        self.__lista_ingredientes.append(novo_ingrediente)
        self.lista_nome_ingredientes.append(novo_ingrediente.nome)
        self.__tela_ingredientes.feedback_sucesso()

    def alterar_ingrediente(self, nome):
        ingrediente_alterado = self.pega_ingrediente(nome)
        self.lista_nome_ingredientes.remove(ingrediente_alterado.nome)
        infos_tela = {'nome': ingrediente_alterado.nome, 'quantidade': ingrediente_alterado.quantidade}

        dados_alteracao = self.__tela_ingredientes_acoes.abre_tela(infos_tela)
        self.__tela_ingredientes_acoes.fecha_tela()
        if dados_alteracao is None:
            self.abre_tela()

        ingrediente_alterado.nome = dados_alteracao["nome"]
        ingrediente_alterado.unidade_medida = dados_alteracao["unidade_medida"]
        ingrediente_alterado.quantidade = dados_alteracao["quantidade"]
        self.lista_nome_ingredientes.append(ingrediente_alterado.nome)
        self.__tela_ingredientes.feedback_sucesso()

    def excluir_ingrediente(self, nome):
        ingrediente_deletado = self.pega_ingrediente(nome)
        print(ingrediente_deletado.nome)
        self.__lista_ingredientes.remove(ingrediente_deletado)
        self.lista_nome_ingredientes.remove(ingrediente_deletado.nome)
        del ingrediente_deletado
        self.__tela_ingredientes_acoes.feedback_sucesso()

    def ver_estoque(self):
        infos_estoque = ''
        for ingrediente in self.__lista_ingredientes:
            infos_estoque += ingrediente.nome.upper() + ' - ' + str(ingrediente.quantidade) + ' ' + ingrediente.unidade_medida.upper() + '\n'
        self.__tela_ingredientes_estoque.abre_tela(infos_estoque)
        self.abre_tela()

    # ------ MÉTODOS INTERNOS ------

    def pega_ingrediente(self, nome: str):
        try:
            for ingrediente in self.__lista_ingredientes:
                if ingrediente.nome.lower() == nome.lower():
                    return ingrediente
            raise ValueError
        except ValueError:
            self.__tela_ingredientes_acoes.erro_nao_cadastrado(nome)
            self.abre_tela()

    @property
    def lista_ingredientes(self):
        return self.__lista_ingredientes

    @property
    def listagem_nome_ingredientes(self):
        return self.lista_nome_ingredientes

    def retornar_menu_principal(self):
        self.__tela_ingredientes.fecha_tela()
        self.__controlador_sistema.inicializa_sistema()
