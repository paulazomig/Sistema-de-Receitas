from Telas.abstractTela import AbstractTela


class TelaReceita(AbstractTela):
    def tela_opcoes(self):
        print("Escolha Opção:\n1. Cadastrar Receitas\n2. Alterar Cadastro de Receita\n3. Pesquisar "
              "Receita\n4. Fazer Receita\n5. Listar Receitas\n6. Visualizar Relatório de Receitas\n7. Excluir Receita\n0. Retornar ao Menu Principal")
        opcao = int(input())
        return opcao

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
