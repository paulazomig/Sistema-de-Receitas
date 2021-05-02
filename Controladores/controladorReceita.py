from Entidades.receita import Receita
from Telas.telaReceita import TelaReceita
from Entidades.ingredienteReceita import IngredienteReceita
from datetime import date


class ControladorReceita:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_ingrediente = self.__controlador_sistema.controlador_ingrediente
        self.__tela_receitas = TelaReceita()
        self.__lista_receitas = []
        self.__eventos_receita = []

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_receita, 2: self.alterar_receita, 3: self.pesquisar_receita, 4: self.fazer_receita,
                        5: self.listar_receitas, 6: self.ver_relatorio_receita, 7: self.excluir_receita, 0: self.retornar_menu_principal}
        while True:
            try:
                lista_opcoes[self.__tela_receitas.tela_opcoes()]()
            except ValueError:
                self.__tela_receitas.erro_menu()
                self.abre_tela()

    def cadastrar_receita(self):
        dados_receita = self.__tela_receitas.obter_dados_receita()
        ingredientes_receita = self.criar_lista_ingredientes(dados_receita["ingredientes_e_quantidades"])

        nova_receita = Receita(dados_receita["titulo"], ingredientes_receita, dados_receita["preparo"])

        if nova_receita in self.__lista_receitas:
            self.__tela_receitas.erro_ja_cadastrado(nova_receita.titulo)
            self.abre_tela()
        self.__lista_receitas.append(nova_receita)
        self.__tela_receitas.feedback_sucesso()

        self.registra_evento("Cadastro de receita", nova_receita.titulo)

    def alterar_receita(self):
        titulo_receita_alterada = self.__tela_receitas.alterar_receita()
        receita_alterada = self.pega_receita(titulo_receita_alterada)
        dados_receita = self.__tela_receitas.obter_dados_receita()
        receita_alterada.titulo = dados_receita["titulo"]
        receita_alterada.ingredientes_receita = self.criar_lista_ingredientes(dados_receita["ingredientes_e_quantidades"])
        receita_alterada.preparo = dados_receita["preparo"]
        self.__tela_receitas.feedback_sucesso()

        self.registra_evento("Alteração de receita", receita_alterada.titulo)

    def pesquisar_receita(self):
        titulo_receita_pesquisada = self.__tela_receitas.pesquisar_receita()
        receita = self.pega_receita(titulo_receita_pesquisada)
        ingredientes = ''
        for i in receita.ingredientes_receita:
            ingredientes += str(i.nome) + ' - ' + str(i.quantidade) + ' ' + str(i.unidade_medida) + '\n'

        self.__tela_receitas.exibir_receita_pesquisada({"titulo": receita.titulo, "ingredientes": ingredientes, "preparo": receita.preparo})

        self.registra_evento("Pesquisa de receita", receita.titulo)

    def fazer_receita(self):
        titulo_receita_feita = self.__tela_receitas.fazer_receita()
        receita = self.pega_receita(titulo_receita_feita)

        for i in receita.ingredientes_receita:
            ingrediente_estoque = self.__controlador_ingrediente.pega_ingrediente(i.nome)
            if ingrediente_estoque.quantidade < i.quantidade:
                self.__tela_receitas.erro_ingredientes_insuficientes(ingrediente_estoque.nome)
                self.abre_tela()
        for ingredientes_utilizados in receita.ingredientes_receita:
            ingrediente_deduzir = self.__controlador_ingrediente.pega_ingrediente(ingredientes_utilizados.nome)
            ingrediente_deduzir.quantidade -= ingredientes_utilizados.quantidade
        self.__tela_receitas.feedback_sucesso()

        self.registra_evento("Receita feita", titulo_receita_feita)

    def listar_receitas(self):
        if not self.__lista_receitas:
            self.__tela_receitas.erro_lista_vazia()
        else:
            lista_receitas = ''
            for receita in self.__lista_receitas:
                lista_receitas += str(receita.titulo.upper()) + '\n'
            self.__tela_receitas.exibir_lista_receitas(lista_receitas)

        self.registra_evento("Exibição de listagem de receitas", "Todas as receitas registradas")

    def ver_relatorio_receita(self):
        if not self.__eventos_receita:
            self.__tela_receitas.erro_lista_vazia()
        else:
            self.__tela_receitas.visualizar_relatorio(self.__eventos_receita)

    def excluir_receita(self):
        titulo_receita_deletada = self.__tela_receitas.excluir_receita()
        receita_deletada = self.pega_receita(titulo_receita_deletada)
        self.__lista_receitas.remove(receita_deletada)
        del receita_deletada
        self.__tela_receitas.feedback_sucesso()

        self.registra_evento("Exclusão de receita", titulo_receita_deletada)

    # ------ MÉTODOS INTERNOS ------

    def pega_receita(self, nome: str):
        try:
            for receita in self.__lista_receitas:
                if receita.titulo.lower() == nome.lower():
                    return receita
            raise ValueError
        except ValueError:
            self.__tela_receitas.erro_nao_cadastrado(nome)
            self.abre_tela()

    def registra_evento(self, acao, receita):
        registro = {"acao": acao, "receita": receita, "data": date.today()}
        self.__eventos_receita.append(registro)

    def criar_lista_ingredientes(self, dados_ingredientes: dict):
        ingredientes_receita = []
        for nome_ingrediente in dados_ingredientes:
            add_ingrediente = IngredienteReceita(self.__controlador_ingrediente.pega_ingrediente(nome_ingrediente), dados_ingredientes[nome_ingrediente])
            ingredientes_receita.append(add_ingrediente)
        return ingredientes_receita

    def retornar_menu_principal(self):
        self.__controlador_sistema.abre_tela()
