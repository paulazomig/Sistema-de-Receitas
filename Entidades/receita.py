from Entidades.ingrediente import Ingrediente

class Receita:
    def __init__(self, titulo: str, ingredientes_receita: dict, preparo: str):
        self.__titulo = titulo
        self.__ingredientes_receita = ingredientes_receita
        self.__preparo = preparo

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @property
    def ingredientes_receita(self):
        return self.__ingredientes_receita

    @property
    def preparo(self):
        return self.__preparo

    @preparo.setter
    def preparo(self, preparo: str):
        self.__preparo = preparo

    @ingredientes_receita.setter
    def ingredientes_receita(self, ingredientes_receita: dict):
        self.__ingredientes_receita = ingredientes_receita

    def __eq__(self, other):
        if isinstance(other, Receita):
            return self.__titulo == other.titulo
        return False
