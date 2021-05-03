from Telas.abstractTela import AbstractTela
import PySimpleGUI as sg


class TelaIngredienteAcoes(AbstractTela):
    def init_components_cadastro(self):
        sg.ChangeLookAndFeel('LightGreen')
        layout = [[sg.Text('Novo Ingrediente')],
                  [sg.Text('Nome:'), sg.InputText(key='nome')],
                  [sg.Text('Unidade de Medida:'), sg.InputText(key='unidade_medida')],
                  [sg.Text('Quantidade em Estoque:'), sg.InputText(key='quantidade')],
                  [sg.Submit(), sg.Cancel()]]

        self.__window = sg.Window('Cadastro de Ingrediente', default_element_size=(40, 1)).Layout(layout)
        button, values = self.__window.Read()
        if values['nome'] != '' and values['unidade_medida'] != '' and int(values['quantidade']) >= 0:
            self.__window.Close()
            return {"nome": values['nome'], "unidade_medida": values['unidade_medida'], "quantidade": int(values['quantidade'])}
        else:
            print("Erro nos valores inseridos! Os valores de nome e unidade de medida não devem ser vazios, "
                  "o valor de quantidade deve ser >= 0.")
            self.__window.Close()

    def erro_ja_cadastrado(self, nome):
        pass

    def erro_nao_cadastrado(self, nome):
        pass