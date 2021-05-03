from Telas.abstractTela import AbstractTela
import PySimpleGUI as sg


class TelaIngrediente(AbstractTela):
    def init_components(self, lista):
        sg.ChangeLookAndFeel('LightGreen')
        layout = [[sg.Text('Selecione uma opção:')],
                  [sg.InputCombo(lista, size=(20,3), key='cb_opcoes')],
                  [sg.Button('Cadastrar Ingrediente'), sg.Button('Alterar Ingrediente'), sg.Button('Excluir Ingrediente'), sg.Button('Ver Estoque')],
                  [sg.Button('Retornar ao Menu Principal')]]

        self.__window = sg.Window('Opções Ingredientes').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        return button, values

    '''def dados_ingrediente(self):
        print("INCLUIR INGREDIENTE:")
        nome = input("Nome: ")
        unidade_medida = input("Unidade de medida: ")
        try:
            quantidade = int(input("Quantidade em estoque: "))
        except ValueError:
            self.erro_valor()
            return
        while True:
            if nome != '' and unidade_medida != '' and quantidade >= 0:
                return {"nome": nome, "unidade_medida": unidade_medida, "quantidade": quantidade}
            else:
                print("Erro nos valores inseridos! Os valores de nome e unidade de medida não devem ser vazios, "
                      "o valor de quantidade deve ser >= 0.")
                return'''

    def alterar_ingrediente(self):
        print("Qual ingrediente deseja alterar?")
        nome = input("Nome: ")

        print("Novos dados:")
        novo_nome = input("Nome: ")
        nova_unidade_medida = input("Unidade de medida: ")
        nova_quantidade = int(input("Quantidade em estoque: "))

        return {"nome": nome, "novo_nome": novo_nome, "nova_unidade_medida": nova_unidade_medida,
                "nova_quantidade": nova_quantidade}

    def exibir_ingredientes(self, dados_ingrediente):
        print(dados_ingrediente["nome"].upper(), " - ", dados_ingrediente["quantidade"], ' ',
              dados_ingrediente["unidade_medida"])

    def excluir_ingrediente(self):
        print("Qual ingrediente deseja excluir?")
        nome = input("Nome: ")
        return nome

    # ------ MÉTODOS TRATAMENTO EXCEÇÕES ------

    def erro_ja_cadastrado(self, nome):
        print("Não é possível completar a operação -  o ingrediente {} já foi cadastrado.\n".format(nome))
        return

    def erro_nao_cadastrado(self, nome):
        print("O ingrediente {} não foi encontrado. Por favor cadastrar o ingrediente.\n".format(nome))
        return
