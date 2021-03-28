class Ingrediente:
    def __init__(self, nome: str, unidade_medida: str):
        self.__nome = nome
        self.__unidade_medida = unidade_medida

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def unidade_medida(self):

        return self.__unidade_medida

    @unidade_medida.setter
    def unidade_medida(self, unidade_medida: str):
        self.__unidade_medida = unidade_medida

    def __eq__(self, other):
        if isinstance(other, Ingrediente):
            return (self.__nome == other.nome) and (self.__unidade_medida == other.unidade_medida)
        return False

    #é necessário lista de ingredientes??
