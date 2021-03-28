class TelaIngrediente:
    def tela_opcoes(self):
        print("Escolha Opção:\n1. Cadastrar Ingredientes\n2. Alterar Cadastro de Ingrediente\n3. Listar "
              "Ingredientes\n0. Retornar ao Menu Principal")
        opcao = int(input())#tratar exceções
        return opcao

    def dados_ingrediente(self):
        print("INCLUIR INGREDIENTE:")
        nome = input("Nome: ")
        unidade_medida = input("Unidade de medida: ")

        return {"nome": nome, "unidade_medida": unidade_medida}

    def alterar_ingrediente(self):
        print("Dados atuais:")
        nome = input("Nome: ")
        unidade_medida = input("Unidade de medida: ")

        print("Novos dados:")
        novo_nome = input("Nome: ")
        nova_unidade_medida = input("Unidade de medida: ")

        return {"nome": nome, "unidade_medida": unidade_medida, "novo_nome": novo_nome, "nova_unidade_medida": nova_unidade_medida}

    def exibir_ingredientes(self, dados_ingrediente):
        print(dados_ingrediente["nome"], " - ", dados_ingrediente["unidade_medida"])