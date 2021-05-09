from DAOs.abstract_dao import AbstractDAO
from Entidades.ingrediente import Ingrediente


class IngredienteDAO(AbstractDAO):
    def __init__(self):
        super().__init__('ingredientes.pkl')

    def add(self, key: str, ingrediente: Ingrediente):
        if ingrediente is not None and isinstance(ingrediente, Ingrediente) and isinstance(ingrediente.nome, str):
            super().add(ingrediente.nome, ingrediente)

    def get(self, key=str):
        try:
            return super().get(key)
        except Exception:
            return None

    def remove(self, key: str):
        try:
            return super().remove(key)
        except Exception:
            return 'exception'
