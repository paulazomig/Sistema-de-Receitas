from Entidades.ingrediente import Ingrediente

class Receita:
    def __init__(self, titulo: str, ingredientes: dict, preparo: str):
        self.__titulo = titulo
        self.__ingredientes = ingredientes
        self.__preparo = preparo

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @property
    def ingredientes(self):
        return self.__ingredientes

    #ingredientes setter??

    @property
    def preparo(self):
        return self.__preparo

    @preparo.setter
    def preparo(self, preparo: str):
        self.__preparo = preparo