from persona import Persona

def main():
    n=input("Indica tu nombre", )
    d=input("Introduce tu DNI", )
    e=int(input("¿Cual es tu edad?", ))
    if(e>=18):
        print ("Eres mayor de edad")
    else:
        print("Eres menor de edad")
    p1 = Persona(n,e,d)
    print ("Nombre:",p1.nombre)
    print ("Edad",p1.edad ,"años")
    print ("DNI:",p1.dni)
if __name__ == "__main__":
    main()