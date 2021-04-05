class Ingrediente:
    def __init__(self, nome: str, unidade_medida: str, quantidade: int):
        self.__nome = nome
        self.__unidade_medida = unidade_medida
        self.__quantidade = quantidade

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

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade: int):
        self.__quantidade = quantidade

    def __eq__(self, other):
        if isinstance(other, Ingrediente):
            return (self.__nome == other.nome)
        return False
