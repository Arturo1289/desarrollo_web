class Persona:

    # constructor, no me construyes si no tengo nombre
    def __init__(self,nombre,edad,dni):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni