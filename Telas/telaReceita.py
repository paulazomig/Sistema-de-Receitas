from Telas.abstractTela import AbstractTela
import PySimpleGUI as sg


class TelaReceita(AbstractTela):
    def __init__(self):
        self.__window = None
        self.init_components(None)

    def init_components(self, cb_lista):
        layout = [[sg.Text('Selecione uma opção:')],
                  [sg.Text('Receitas:'), sg.InputCombo(cb_lista, size=(30,1), key='cb_opcao')],
                  [sg.Button('Cadastrar Receita', key='cadastro'),
                   sg.Button('Alterar Receita', key='alteracao'),
                   sg.Button('Visualizar Receita', key='view'),
                   sg.Button('Ver Relatório', key='relatorio'),
                   sg.Button('Excluir Receita', key='exclusao')],
                  [sg.Button('Retornar ao Menu Principal', key='retorna')]]

        self.__window = sg.Window('Opções Receitas', location=(400,300), element_justification='center').Layout(layout)

    def abre_tela(self, cb_lista):
        self.init_components(cb_lista)
        button, values = self.__window.Read()
        return button, values

    def fecha_tela(self):
        self.__window.Close()

    def obter_dados_receita(self):
        print("CADASTRO DE RECEITA:")
        titulo = input("Título da receita: ")

        print("Ingredientes:")
        continua = True
        ingredientes_e_quantidades = {}
        while continua:
            nome_ingrediente = input("Nome do ingrediente: ")
            try:
                quantidade_ingrediente = int(input("Quantidade do ingrediente: "))
            except ValueError:
                self.erro_valor()
            ingredientes_e_quantidades[nome_ingrediente] = quantidade_ingrediente

            mais_ingredientes = input("Deseja adicionar mais um ingrediente? (SIM ou NÃO)\n")
            if mais_ingredientes.lower() == "não" or mais_ingredientes.lower() == "nao":
                continua = False
            elif mais_ingredientes.lower() == "sim":
                continue
            else:
                self.erro_menu()

        preparo = input("Modo de preparo: ")
        return {"titulo": titulo, "ingredientes_e_quantidades": ingredientes_e_quantidades, "preparo": preparo}

    def alterar_receita(self):
        print("Qual receita deseja alterar?")
        titulo = input("Titulo: ")
        print("Cadastre as informações da receita alterada: ")
        return titulo

    def pesquisar_receita(self):
        print("Qual receita deseja visualizar?")
        titulo = input("Título: ")
        return titulo

    def exibir_receita_pesquisada (self, dados_receita):
        print(dados_receita["titulo"].upper())
        print("\nIngredientes:")
        print(dados_receita["ingredientes"])
        print("Modo de preparo:")
        print(dados_receita["preparo"], "\n")

    def exibir_lista_receitas(self, lista_receitas):
        print(lista_receitas)

    def excluir_receita(self):
        print("EXCLUIR RECEITA:")
        titulo_excluido = input("Nome da receita a ser excluída: ")
        return titulo_excluido

    def fazer_receita(self):
        print("Qual o titulo da receita que você deseja fazer?")
        titulo_fazer = input("Título: ")
        return titulo_fazer

    def visualizar_relatorio(self, eventos: list):
        print("AÇÃO - RECEITA - DATA\n")
        for evento_listado in eventos:
            print("{} - {} - {}".format(evento_listado['acao'], evento_listado['receita'], evento_listado['data']))
        print("\n")

    # ------ MÉTODOS TRATAMENTO EXCEÇÕES ------

    def erro_ja_cadastrado(self, nome):
        print("Não é possível completar a operação -  a receita {} já foi cadastrada.\n".format(nome))

    def erro_nao_cadastrado(self, nome):
        print("A receita {} não foi encontrada. Por favor cadastrar a receita.\n".format(nome))
        return

    def erro_ingredientes_insuficientes(self, nome):
        print("O ingrediente {} não possui quantidade suficiente para essa receita!\n".format(nome))
        return
