from Telas.abstractTela import AbstractTela
import PySimpleGUI as sg


class TelaIngredienteAcoes(AbstractTela):

    def __init__(self):
        self.__window = None
        self.init_components(None)

    def init_components(self, infos_tela):
        if not infos_tela:
            layout = [[sg.Text('Novo Ingrediente')],
                      [sg.Text('Nome:'), sg.InputText('Ingrediente',key='nome')],
                      [sg.Text('Unidade de Medida:')],
                      [sg.Radio('Unidades', 'RADIO1', default=True, key='unidades'),
                       sg.Radio('Kg', 'RADIO1', key='kg'),
                       sg.Radio('Gramas', 'RADIO1', key='gramas'),
                       sg.Radio('Ml', 'RADIO1', key='ml'),
                       sg.Radio('Litros', 'RADIO1', key='litros')],
                      [sg.Text('Quantidade em Estoque:'), sg.InputText(key='quantidade')],
                      [sg.Submit(), sg.Cancel(key='cancel')]]

        else:
            layout = [[sg.Text('Novo Ingrediente')],
                      [sg.Text('Nome:'), sg.InputText(infos_tela['nome'], key='nome')],
                      [sg.Text('Unidade de Medida:')],
                      [sg.Radio('Unidades', 'RADIO1', default=True, key='unidades'),
                       sg.Radio('Kg', 'RADIO1', key='kg'),
                       sg.Radio('Gramas', 'RADIO1', key='gramas'),
                       sg.Radio('Ml', 'RADIO1', key='ml'),
                       sg.Radio('Litros', 'RADIO1', key='litros')],
                      [sg.Text('Quantidade em Estoque:'), sg.InputText(infos_tela['quantidade'], key='quantidade')],
                      [sg.Submit(), sg.Cancel(key='cancel')]]

        self.__window = sg.Window('Cadastro de Ingrediente', default_element_size=(40, 1)).Layout(layout)

    def abre_tela(self, infos_tela):
        self.init_components(infos_tela)
        button, values = self.__window.Read()
        if button == 'cancel':
            return None
        elif not button:
            exit(0)

        medida = ''
        if values['unidades']:
            medida = 'Unidades'

        elif values['kg']:
            medida = 'Kg'

        elif values['gramas']:
            medida = 'Gramas'

        elif values['ml']:
            medida = 'Ml'

        elif values['litros']:
            medida = 'Litros'

        try:
            int(values['quantidade'])

        except Exception:
            self.erro_valor()
            return None

        if values['nome'] != '' and int(values['quantidade']) >= 0:
            return {"nome": values['nome'], "unidade_medida": medida, "quantidade": int(values['quantidade'])}
        else:
            self.erro_cadastro()
            return None

    def fecha_tela(self):
        self.__window.Close()

    # ------ MÉTODOS TRATAMENTO EXCEÇÕES ------

    def erro_cadastro(self):
        sg.Popup("Erro de Cadastro", "Atenção! Os valores de nome e quantidade não devem ser vazios e "
                                     "o valor de quantidade deve ser >= 0. Tente novamente.")

    def erro_ja_cadastrado(self, nome):
        sg.Popup("Item Já Cadastrado", "Não é possível completar a operação -  o ingrediente {} já foi cadastrado.".format(nome))

    def erro_nao_cadastrado(self, nome):
        sg.Popup("Item Não Cadastrado", "O ingrediente {} não foi encontrado. Por favor cadastrar ou selecionar o ingrediente.".format(nome))

