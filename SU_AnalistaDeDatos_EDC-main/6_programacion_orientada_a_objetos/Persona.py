class Persona:

    # constructor, no me construyes si no tengo nombre
    def __init__(self,nombre,edad,estatura,mascota=None):
        self.__nombre = nombre
        self.__edad = edad
        self.__estatura = estatura
        self.__mascota = mascota

    def saludar(self):
        print(f"Hola soy {self.__nombre}")

    def hablar(self,mensaje):
        print(f"{self.__nombre}: {mensaje}")

    def adoptarMascota(self,mascota):
        self.__mascota = mascota

    def quien_es_mi_mascota(self):
        print("mascota:",self.__mascota.que_soy())


    @property #getter
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
        if(edad>17):
            self.__edad = edad
        else:
            print("menor de edad")

    @property
    def estatura(self):
        return self.__estatura
    
    @estatura.setter
    def estatura(self,estatura):
        self.__estatura = estatura
    
    @property
    def mascota(self):
        return self.__mascota
    
    @mascota.setter
    def mascota(self,mascota):
        self.__mascota = mascota
        
    def __str__(self):
        return f""" 

******* {self.__nombre} ****** 

edad:{self.__edad}

estatura: {self.__estatura}
"""

"""

"setYget":{

		"prefix":"setget",

		"body":[

			"@property",

    		"def $CLIPBOARD(self):",

        	"\treturn self.__$CLIPBOARD",

    		"@$CLIPBOARD.setter",

    		"def $CLIPBOARD(self,$CLIPBOARD):",

        	"\tself.__$CLIPBOARD = $CLIPBOARD",

		],

		"description": "Crear setters y getter"

	},
"""