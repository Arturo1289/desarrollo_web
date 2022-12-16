from persona import persona
class cuenta:

    def __init__(self,titular:persona,cantidad=0.0):
        self.__titular = titular
        self.__cantidad = cantidad

    def mostrar(self):
        print(f'titular: {self.__titular.mostrar}\nCantidad:')

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self,titular):
        self.__titular = titular

    @property
    def cantidad(self):
        return self.__cantidad