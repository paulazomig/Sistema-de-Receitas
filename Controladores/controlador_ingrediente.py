from Entidades.ingrediente import Ingrediente
from Telas.tela_ingrediente import TelaIngrediente
from Telas.tela_ingrediente_estoque import TelaIngredienteEstoque
from Telas.tela_ingrediente_acoes import TelaIngredienteAcoes
from DAOs.ingrediente_dao import IngredienteDAO


class ControladorIngrediente:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.dao = IngredienteDAO()
        self.__tela_ingredientes = TelaIngrediente()
        self.__tela_ingredientes_estoque = TelaIngredienteEstoque()
        self.__tela_ingredientes_acoes = TelaIngredienteAcoes()

    def abre_tela(self):
        lista_opcoes = {'cadastro': self.cadastrar_ingrediente,
                        'alteracao': self.alterar_ingrediente,
                        'exclusao': self.excluir_ingrediente,
                        'estoque': self.ver_estoque,
                        'retorna': self.retornar_menu_principal}

        while True:
            opcao_menu, valor_menu = self.__tela_ingredientes.abre_tela(self.dao.get_all_names())
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

        if novo_ingrediente in self.dao.get_all():
            self.__tela_ingredientes_acoes.erro_ja_cadastrado(novo_ingrediente.nome)
            return
        self.dao.add(novo_ingrediente.nome, novo_ingrediente)

        self.__tela_ingredientes.feedback_sucesso()

    def alterar_ingrediente(self, nome):
        ingrediente_alterado = self.dao.get(nome)
        infos_tela = {'nome': ingrediente_alterado.nome, 'quantidade': ingrediente_alterado.quantidade}

        dados_alteracao = self.__tela_ingredientes_acoes.abre_tela(infos_tela)
        self.__tela_ingredientes_acoes.fecha_tela()
        if dados_alteracao is None:
            self.abre_tela()

        self.dao.remove(dados_alteracao['nome'])

        ingrediente_alterado.nome = dados_alteracao["nome"]
        ingrediente_alterado.unidade_medida = dados_alteracao["unidade_medida"]
        ingrediente_alterado.quantidade = dados_alteracao["quantidade"]

        self.dao.add(ingrediente_alterado.nome, ingrediente_alterado)
        self.__tela_ingredientes.feedback_sucesso()

    def excluir_ingrediente(self, nome):
        self.dao.remove(nome)
        self.__tela_ingredientes_acoes.feedback_sucesso()

    def ver_estoque(self):
        infos_estoque = ''
        for ingrediente in self.dao.get_all():
            infos_estoque += ingrediente.nome.upper() + ' - ' + str(ingrediente.quantidade) + ' ' + ingrediente.unidade_medida.upper() + '\n'
        self.__tela_ingredientes_estoque.abre_tela(infos_estoque)
        self.abre_tela()

    # ------ MÉTODOS INTERNOS ------

    def retornar_menu_principal(self):
        self.__tela_ingredientes.fecha_tela()
        self.__controlador_sistema.inicializa_sistema()
