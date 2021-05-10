import pickle


class RelatorioDAO():
    def __init__(self):
        self.__datasource = 'relatorio.pkl'
        self.__cache = []

        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource, 'rb'))

    def add(self, log):
        self.__cache.append(log)
        self.__dump()

    def get(self):
        return self.__cache



