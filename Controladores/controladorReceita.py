from Entidades.receita import Receita
from Telas.telaReceita import TelaReceita
from datetime import date


class ControladorReceita:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_ingrediente = self.__controlador_sistema.controlador_ingrediente
        self.__tela_receitas = TelaReceita()
        self.__lista_receitas = []
        self.__eventos_receita = []

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_receita, 2: self.alterar_receita, 3: self.pesquisar_receita, 4: self.excluir_receita, 5: self.fazer_receita, 6: self.ver_relatorio_receita,
                        0: self.retornar_menu_principal}
        while True:
            try:
                lista_opcoes[self.__tela_receitas.tela_opcoes()]()
            except Exception:
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

        self.registra_evento("Cadastro de receita", nova_receita.titulo)

    def alterar_receita(self):
        titulo_receita_alterada = self.__tela_receitas.alterar_receita()
        receita_alterada = self.pega_receita(titulo_receita_alterada)
        dados_receita = self.__tela_receitas.obter_dados_receita()
        receita_alterada.titulo = dados_receita["titulo"]
        receita_alterada.ingredientes_receita = self.criar_lista_ingredientes(dados_receita["ingredientes_e_quantidades"])
        receita_alterada.preparo = dados_receita["preparo"]

        self.registra_evento("Alteração de receita", receita_alterada.titulo)

    def pesquisar_receita(self):
        titulo_receita_pesquisada = self.__tela_receitas.pesquisar_receita()
        receita = self.pega_receita(titulo_receita_pesquisada)
        ingredientes = ''
        for nome_ingrediente in receita.ingredientes_receita:
            ingrediente = self.__controlador_ingrediente.pega_ingrediente(nome_ingrediente)
            ingredientes += str(ingrediente.nome) + ' - ' + str(receita.ingredientes_receita[nome_ingrediente]) + ' ' + ingrediente.unidade_medida + '\n'

        self.__tela_receitas.exibir_receita_pesquisada({"titulo": receita.titulo, "ingredientes": ingredientes, "preparo": receita.preparo})

        self.registra_evento("Pesquisa de receita", receita.titulo)

    def excluir_receita(self):
        titulo_receita_deletada = self.__tela_receitas.excluir_receita()
        receita_deletada = self.pega_receita(titulo_receita_deletada)
        self.__lista_receitas.remove(receita_deletada)
        del receita_deletada

        self.registra_evento("Exclusão de receita", titulo_receita_deletada)

    def fazer_receita(self):
        titulo_receita_feita = self.__tela_receitas.fazer_receita()
        receita = self.pega_receita(titulo_receita_feita)

        for checagem_quantidades in receita.ingredientes_receita:
            ingrediente_check = self.__controlador_ingrediente.pega_ingrediente(checagem_quantidades)
            if ingrediente_check.quantidade < receita.ingredientes_receita[checagem_quantidades]:
                self.__tela_receitas.erro_ingredientes_insuficientes(ingrediente_check.nome)
                self.abre_tela()
        for ingredientes_utilizados in receita.ingredientes_receita:
            ingrediente_deduzir = self.__controlador_ingrediente.pega_ingrediente(ingredientes_utilizados)
            ingrediente_deduzir.quantidade -= receita.ingredientes_receita[ingredientes_utilizados]

        self.registra_evento("Receita feita", titulo_receita_feita)

    def ver_relatorio_receita(self):
        self.__tela_receitas.visualizar_relatorio(self.__eventos_receita)

    def criar_lista_ingredientes(self, dados_ingredientes: dict):
        ingredientes_receita = {}
        for nome_ingrediente in dados_ingredientes:
            add_ingrediente = self.__controlador_ingrediente.pega_ingrediente(nome_ingrediente)
            ingredientes_receita[add_ingrediente.nome] = dados_ingredientes[nome_ingrediente]
        return ingredientes_receita

    def pega_receita(self, nome: str):
        try:
            for receita in self.__lista_receitas:
                if receita.titulo == nome:
                    return receita
            raise ValueError
        except ValueError:
            self.__tela_receitas.erro_nao_cadastrado(nome)
            self.abre_tela()

    def registra_evento(self, acao, receita):
        registro = {"acao": acao, "receita": receita, "data": date.today()}
        self.__eventos_receita.append(registro)

    def retornar_menu_principal(self):
        self.__controlador_sistema.abre_tela()