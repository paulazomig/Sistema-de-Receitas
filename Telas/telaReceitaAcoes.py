from Telas.abstractTela import AbstractTela
import PySimpleGUI as sg


class TelaReceitaAcoes(AbstractTela):

    def __init__(self):
        self.__window = None
        self.init_components(None)
        self.ingredientes_receita = []
        self.ingredientes_tela = ''

    def init_components(self, lista_ingredientes):
        layout = [[sg.Text('Nova Receita')],
                  [sg.Text('Nome:'), sg.InputText(key='titulo')],
                  [sg.Text('Ingredientes:')],
                  [sg.Text('Modo de Preparo:')],
                  [sg.Multiline(size=(70,7), key='preparo')],
                  [sg.Button('Adicionar Ingredientes'), sg.Cancel(key='cancel')]]

        layout_ingredientes = [[sg.Text('Cadastro de Ingrediente da Receita')],
                               [sg.Listbox(lista_ingredientes, size=(70,10), select_mode='single', key='ingrediente')],
                               [sg.Text('Quantidade'), sg.InputText(key='quantidade')],
                               [sg.Button('Adicionar Mais Ingredientes', key='adicionar'),
                                sg.Button('Finalizar Cadastro da Receita', key='finalizar')]]

        self.__window = sg.Window('Cadastro de Receita',
                                  location=(450,300),
                                  default_element_size=(60, 1)).Layout(layout)

        self.__window_ingrediente = sg.Window('Cadastro de Ingredientes da Receita',
                                              location=(450, 300),
                                              default_element_size=(60, 1)).Layout(layout_ingredientes)

    def abre_tela(self, lista_ingredientes):
        self.init_components(lista_ingredientes)
        button, values = self.__window.Read()
        self.__window.Close()
        if button == 'cancel':
            return None
        elif not button:
            exit(0)
        else:
            ingredientes_receita = {}
            loop = True
            while loop:
                button_ing, values_ing = self.__window_ingrediente.Read()
                self.__window_ingrediente.Close()
                print(values_ing['ingrediente'][0], values_ing['quantidade'])
                ingredientes_receita = {values_ing['ingrediente'][0]: values_ing['quantidade']}
                print(ingredientes_receita)

                if button == 'finalizar':
                    loop = False

            return {'titulo': values['titulo'], 'ingredientes_receita': ingredientes_receita, 'preparo': values['preparo']}


        '''try:
            int(values['quantidade'])

        except Exception:
            self.erro_valor()
            return None

        if values['nome'] != '' and int(values['quantidade']) >= 0:
            return {"nome": values['nome'], "unidade_medida": medida, "quantidade": int(values['quantidade'])}
        else:
            self.erro_cadastro()
            return None'''

    def fecha_tela(self):
        self.__window.Close()

        '''
        #if not infos_tela:
        else:
            pass
            layout = [[sg.Text('Novo Ingrediente')],
                      [sg.Text('Nome:'), sg.InputText(infos_tela['nome'], key='nome')],
                      [sg.Text('Unidade de Medida:')],
                      [sg.Radio('Unidades', 'RADIO1', default=True, key='unidades'),
                       sg.Radio('Kg', 'RADIO1', key='kg'),
                       sg.Radio('Gramas', 'RADIO1', key='gramas'),
                       sg.Radio('Ml', 'RADIO1', key='ml'),
                       sg.Radio('Litros', 'RADIO1', key='litros')],
                      [sg.Text('Quantidade em Estoque:'), sg.InputText(infos_tela['quantidade'], key='quantidade')],
                      [sg.Submit(), sg.Cancel(key='cancel')]]'''

    def erro_ja_cadastrado(self, nome):
        print("Não é possível completar a operação -  a receita {} já foi cadastrada.\n".format(nome))

    def erro_nao_cadastrado(self, nome):
        print("A receita {} não foi encontrada. Por favor cadastrar a receita.\n".format(nome))
        return