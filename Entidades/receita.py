from Entidades.ingrediente import Ingrediente

class Receita:
    def __init__(self, titulo: str, ingredientes_quantidades: dict, preparo: str):
        self.__titulo = titulo
        self.__ingredientes_quantidades = ingredientes_quantidades
        self.__preparo = preparo

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @property
    def ingredientes_quantidades(self):
        return self.__ingredientes_quantidades

    @property
    def preparo(self):
        return self.__preparo

    @preparo.setter
    def preparo(self, preparo: str):
        self.__preparo = preparo

    def __eq__(self, other):
        if isinstance(other, Receita):
            return self.__titulo == other.titulo
        return False

    #ingredientes_quantidades setter??
    #é necessário lista das receitas?