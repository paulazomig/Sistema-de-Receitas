from DAOs.abstract_dao import AbstractDAO
from Entidades.receita import Receita


class ReceitaDAO(AbstractDAO):
    def __init__(self):
        super().__init__('receitas.pkl')

    def add(self, key: str, receita: Receita):
        if receita is not None and isinstance(receita, Receita) and isinstance(receita.titulo, str):
            super().add(receita.titulo, receita)

    def get(self, key=str):
        #implementar testes (not none, etc)
        return super().get(key)

    def remove(self, key: str):
        return super().remove(key)
