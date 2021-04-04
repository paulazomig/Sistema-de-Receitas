class DadoNaoCadastradoException(Exception):
    def __init__(self):
        super().__init__("O ingrediente ou receita que você indicou não está cadastrada. Por favor realize o cadastro "
                         "antes de prosseguir.")

