class TelaIngrediente:
    def tela_opcoes(self):
        print("Escolha Opção:\n1. Cadastrar Ingredientes\n2. Alterar Cadastro de Ingrediente\n3. Listar "
              "Ingredientes\n0. Retornar ao Menu Principal")
        opcao = int(input())
        return opcao

    def dados_ingrediente(self):
        print("INCLUIR INGREDIENTE:")
        nome = input("Nome: ")
        unidade_medida = input("Unidade de medida: ")
        while True:
            if nome != '' and unidade_medida != '':
                return {"nome": nome, "unidade_medida": unidade_medida}
            else:
                print("Os valores inseridos não devem ser nulos. Por favor, digite um nome e unidade de medida.")
                nome = input("Nome: ")
                unidade_medida = input("Unidade de medida: ")

    def alterar_ingrediente(self):
        print("Qual ingrediente deseja alterar?")
        nome = input("Nome: ")

        print("Novos dados:")
        novo_nome = input("Nome: ")
        nova_unidade_medida = input("Unidade de medida: ")

        return {"nome": nome, "novo_nome": novo_nome, "nova_unidade_medida": nova_unidade_medida}

    def exibir_ingredientes(self, dados_ingrediente):
        print("LISTA DE INGREDIENTES:")
        print(dados_ingrediente["nome"], " - ", dados_ingrediente["unidade_medida"])

    def excecoes_ingrediente(self, tipo_excecao):

        print("O valor inserido não é válido. Por favor digitar um número de 0 a 3.")
        return