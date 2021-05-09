from Entidades.ingrediente import Ingrediente


class IngredienteReceita:
    def __init__(self, ingrediente: Ingrediente, quantidade: int):
        self.__ingrediente = ingrediente
        self.__quantidade = quantidade

    @property
    def ingrediente(self):
        return self.__ingrediente

    @ingrediente.setter
    def ingrediente(self, ingrediente: Ingrediente):
        self.__ingrediente = ingrediente

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade: int):
        self.__quantidade = quantidade

    @property
    def nome(self):
        return self.__ingrediente.nome

    @property
    def unidade_medida(self):
        return self.__ingrediente.unidade_medida
