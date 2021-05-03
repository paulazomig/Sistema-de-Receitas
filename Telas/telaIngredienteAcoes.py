from Telas.abstractTela import AbstractTela
import PySimpleGUI as sg


class TelaIngredienteAcoes(AbstractTela):
    sg.ChangeLookAndFeel('LightGreen')

    def init_components_cadastro(self):
        layout = [[sg.Text('Novo Ingrediente')],
                  [sg.Text('Nome:'), sg.InputText(key='nome')],
                  [sg.Text('Unidade de Medida:'), sg.InputText(key='unidade_medida')],
                  [sg.Text('Quantidade em Estoque:'), sg.InputText(key='quantidade')],
                  [sg.Submit(), sg.Cancel()]]

        self.__window = sg.Window('Cadastro de Ingrediente', default_element_size=(40, 1)).Layout(layout)
        button, values = self.__window.Read()
        try:
            quantidade = float(values['quantidade'])
        except ValueError:
            self.__window.Close()
            self.erro_valor()

        if values['nome'] != '' and values['unidade_medida'] != '' and quantidade >= 0:
            self.__window.Close()
            return {"nome": values['nome'], "unidade_medida": values['unidade_medida'], "quantidade": int(values['quantidade'])}
        else:
            self.__window.Close()
            self.erro_cadastro()

    def init_alteracao(self):
        pass

    # ------ MÉTODOS TRATAMENTO EXCEÇÕES ------

    def erro_cadastro(self):
        sg.Popup("Erro de Cadastro", "Atenção! Os valores de nome e unidade de medida não devem ser vazios e "
                                     "o valor de quantidade deve ser >= 0.")

    def erro_ja_cadastrado(self, nome):
        sg.Popup("Item Já Cadastrado", "Não é possível completar a operação -  o ingrediente {} já foi cadastrado.".format(nome))

    def erro_nao_cadastrado(self, nome):
        sg.Popup("Item Não Cadastrado", "O ingrediente {} não foi encontrado. Por favor cadastrar ou selecionar o ingrediente.".format(nome))

