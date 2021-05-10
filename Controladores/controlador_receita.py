from Entidades.receita import Receita
from Telas.tela_receita import TelaReceita
from Telas.tela_receita_acoes import TelaReceitaAcoes
from Telas.tela_receita_view import TelaReceitaView
from Telas.tela_receita_relatorio import TelaReceitaRelatorio
from Entidades.ingrediente_receita import IngredienteReceita
from DAOs.receita_dao import ReceitaDAO
from DAOs.relatorio_dao import RelatorioDAO
from Excecoes.empty_list_exception import EmptyListException
from datetime import date


class ControladorReceita:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_ingrediente = self.__controlador_sistema.dao_ingrediente
        self.__dao = ReceitaDAO()
        self.__dao_relatorio = RelatorioDAO()
        self.__tela_receitas = TelaReceita()
        self.__tela_receitas_acoes = TelaReceitaAcoes()
        self.__tela_receita_view = TelaReceitaView()
        self.__tela_receita_relatorio = TelaReceitaRelatorio()
        self.__eventos_receita = []

    def abre_tela(self):
        lista_opcoes = {'cadastro': self.cadastrar_receita,
                        'alteracao': self.alterar_receita,
                        'view': self.visualizar_receita,
                        'relatorio': self.ver_relatorio_receita,
                        'exclusao': self.excluir_receita,
                        'retorna': self.retornar_menu_principal}

        while True:
            opcao_menu, valor_menu = self.__tela_receitas.abre_tela(self.__dao.get_all_names())
            self.__tela_receitas.fecha_tela()
            if opcao_menu is None:
                exit(0)

            if opcao_menu == 'alteracao' or opcao_menu == 'exclusao' or opcao_menu == 'view':
                lista_opcoes[opcao_menu](valor_menu['cb_opcao'])
            else:
                lista_opcoes[opcao_menu]()

    def cadastrar_receita(self):
        ingredientes_estoque = self.lista_ingredientes_menu()
        infos_tela = None
        button, dados_receita = self.__tela_receitas_acoes.abre_tela(ingredientes_estoque, infos_tela)

        if button == 'cancel':
            self.abre_tela()

        if dados_receita is None:
            self.cadastrar_receita()

        ingredientes_receita = self.criar_lista_ingredientes(dados_receita["ingredientes_receita"])

        nova_receita = Receita(dados_receita["titulo"], ingredientes_receita, dados_receita["preparo"])

        if nova_receita in self.__dao.get_all():
            self.__tela_receitas.erro_ja_cadastrado(nova_receita.titulo)
            self.abre_tela()
        self.__dao.add(nova_receita.titulo, nova_receita)
        self.registra_evento("Cadastro de receita", nova_receita.titulo)

    def alterar_receita(self, titulo):
        ingredientes_estoque = self.lista_ingredientes_menu()
        receita_alterada = self.__dao.get(titulo)

        if receita_alterada is None:
            self.abre_tela()

        infos_tela = {'titulo': receita_alterada.titulo,
                      'preparo': receita_alterada.preparo,
                      'ingredientes': receita_alterada.ingredientes_receita}

        button, dados_receita = self.__tela_receitas_acoes.abre_tela(ingredientes_estoque, infos_tela)

        if button == 'cancel':
            self.abre_tela()
        else:
            if dados_receita is None:
                self.alterar_receita(titulo)

            self.__dao.remove(receita_alterada.titulo)
            receita_alterada.titulo = dados_receita["titulo"]
            receita_alterada.ingredientes_receita = self.criar_lista_ingredientes(dados_receita["ingredientes_receita"])
            receita_alterada.preparo = dados_receita["preparo"]
            self.__dao.add(receita_alterada.titulo, receita_alterada)

            self.registra_evento("Alteração de receita", receita_alterada.titulo)
            self.abre_tela()

    def visualizar_receita(self, titulo):
        receita = self.__dao.get(titulo)

        if receita is None:
            self.abre_tela()

        ingredientes = ''
        for i in receita.ingredientes_receita:
            ingredientes += str(i.nome) + ' - ' + str(i.quantidade) + ' ' + str(i.unidade_medida) + '\n'
        titulo = receita.titulo
        preparo = receita.preparo

        button_value = self.__tela_receita_view.abre_tela(titulo, ingredientes, preparo)
        self.registra_evento("Pesquisa de receita", receita.titulo)
        if button_value is None:
            exit(0)
        elif button_value == 'retornar':
            self.abre_tela()
        else:
            self.fazer_receita(titulo)

    def fazer_receita(self, titulo):
        receita = self.__dao.get(titulo)

        for i in receita.ingredientes_receita:
            ingrediente_estoque = self.__controlador_ingrediente.get(i.nome)
            if ingrediente_estoque.quantidade < i.quantidade:
                self.__tela_receita_view.erro_ingredientes_insuficientes(i.nome)
                self.abre_tela()

        for i in receita.ingredientes_receita:
            ingrediente_deduzir = self.__controlador_ingrediente.get(i.nome)
            ingrediente_deduzir.quantidade -= i.quantidade
            self.__controlador_ingrediente.add(ingrediente_deduzir.nome, ingrediente_deduzir)
        self.__tela_receitas.feedback_sucesso()

        self.registra_evento("Receita feita", titulo)

    def ver_relatorio_receita(self):
        try:
            if not self.__dao_relatorio.get():
                raise EmptyListException()

            relatorio = ''
            for i in self.__dao_relatorio.get():
                relatorio += i + '\n'
            self.__tela_receita_relatorio.abre_tela(relatorio)

        except EmptyListException:
            self.abre_tela()

    def excluir_receita(self, titulo):
        valor = self.__dao.remove(titulo)
        if valor == 'exception':
            self.abre_tela()
        self.__tela_receitas_acoes.feedback_sucesso()
        self.registra_evento("Exclusão de receita", titulo)

    # ------ MÉTODOS INTERNOS ------

    def registra_evento(self, acao, receita):
        registro = ''
        registro += 'Ação: ' + acao + " - Receita: " + receita + " - Data: " + str(date.today())
        self.__dao_relatorio.add(registro)

    def criar_lista_ingredientes(self, dados_ingredientes: dict):
        ingredientes_receita = []
        for nome_ingrediente in dados_ingredientes:
            add_ingrediente = IngredienteReceita(self.__controlador_ingrediente.get(nome_ingrediente),
                                                 dados_ingredientes[nome_ingrediente])
            ingredientes_receita.append(add_ingrediente)
        return ingredientes_receita

    def lista_ingredientes_menu(self):
        lista_ingredientes = self.__controlador_ingrediente.get_all()
        lista_menu = []
        for i in lista_ingredientes:
            ing = i.nome + ', [{}]'.format(i.unidade_medida)
            lista_menu.append(ing)
        return lista_menu

    def retornar_menu_principal(self):
        self.__controlador_sistema.abre_tela()
