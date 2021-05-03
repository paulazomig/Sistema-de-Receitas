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
        self.listagem_ingredientes = []

    def abre_tela(self):
        lista_opcoes = {'Cadastrar Ingrediente': self.cadastrar_ingrediente, 'Alterar Ingrediente': self.alterar_ingrediente,
                        'Excluir Ingrediente': self.excluir_ingrediente, 'Ver Estoque': self.ver_estoque,
                        'Retornar ao Menu Principal': self.retornar_menu_principal}

        while True:
            try:
                lista = []
                if not self.listagem_ingredientes:
                    pass
                else:
                    for ingrediente in self.listagem_ingredientes:
                        lista.append(ingrediente.nome)
                opcao, valor = self.__tela_ingredientes.init_components(lista)

                if opcao == 'Alterar Ingrediente':
                    lista_opcoes[opcao](valor['cb_opcoes'])
                else:
                    lista_opcoes[opcao]()
            except Exception:
                self.__tela_ingredientes.erro_menu()
                self.abre_tela()

    def ver_estoque(self):
        ing = ''
        for ingrediente in self.listagem_ingredientes:
            ing += ingrediente.nome.upper() + ' - ' + str(ingrediente.quantidade) + ' ' + ingrediente.unidade_medida.upper() + '\n'
        self.__tela_ingredientes_estoque.init_components(ing)
        self.abre_tela()

    def cadastrar_ingrediente(self):
        dados_ingrediente = self.__tela_ingredientes_acoes.init_components_cadastro()
        novo_ingrediente = Ingrediente(dados_ingrediente["nome"], dados_ingrediente["unidade_medida"], dados_ingrediente["quantidade"])
        if novo_ingrediente in self.listagem_ingredientes:
            self.__tela_ingredientes.erro_ja_cadastrado(novo_ingrediente.nome)
            return
        self.listagem_ingredientes.append(novo_ingrediente)
        self.__tela_ingredientes.feedback_sucesso()

    def alterar_ingrediente(self):
        dados_alteracao_ingrediente = self.__tela_ingredientes.alterar_ingrediente()
        ingrediente = self.pega_ingrediente(dados_alteracao_ingrediente["nome"])
        ingrediente.nome = dados_alteracao_ingrediente["novo_nome"]
        ingrediente.unidade_medida = dados_alteracao_ingrediente["nova_unidade_medida"]
        ingrediente.quantidade = dados_alteracao_ingrediente["nova_quantidade"]
        self.__tela_ingredientes.feedback_sucesso()

    def excluir_ingrediente(self):
        nome_ingrediente_deletado = self.__tela_ingredientes.excluir_ingrediente()
        ingrediente_deletado = self.pega_ingrediente(nome_ingrediente_deletado)
        self.listagem_ingredientes.remove(ingrediente_deletado)
        del ingrediente_deletado
        self.__tela_ingredientes.feedback_sucesso()

    # ------ MÉTODOS INTERNOS ------

    def pega_ingrediente(self, nome: str):
        try:
            for ingrediente in self.listagem_ingredientes:
                if ingrediente.nome.lower() == nome.lower():
                    return ingrediente
            raise ValueError
        except ValueError:
            self.__tela_ingredientes.erro_nao_cadastrado(nome)
            self.abre_tela()

    @property
    def lista_ingredientes(self):
        return self.listagem_ingredientes

    def retornar_menu_principal(self):
        self.__controlador_sistema.abre_tela()