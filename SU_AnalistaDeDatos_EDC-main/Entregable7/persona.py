class Persona:

    def __init__(self,nombre,edad,dni):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self,edad):
        if(edad>=18):
            self.__edad = edad
        else:
            print("menor de edad")

    @property
    def dni(self):
        return self.__dni

    @nombre.setter
    def dni(self,dni):
        self.__dni = dni