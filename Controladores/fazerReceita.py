class FazerReceita:

    def fazer_receita(self, receita):
        for checagem_quantidades in receita.ingredientes_receita:
            ingrediente_check = self.__controlador_ingrediente.pega_ingrediente(checagem_quantidades)
            if ingrediente_check.quantidade < receita.ingredientes_receita[checagem_quantidades]:
                pass #exception não há ingredientes

        #printar receita

        for ingredientes_utilizados in receita.ingredientes_receita:
            ingrediente_deduzir = self.__controlador_ingrediente.pega_ingrediente(ingredientes_utilizados)
            ingrediente_deduzir.quantidade -= receita.ingredientes_receita[ingredientes_utilizados]

        #printar receita realizada
        #log