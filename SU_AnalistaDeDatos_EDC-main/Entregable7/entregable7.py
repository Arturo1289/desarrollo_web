from persona import Persona

def main():
    n=input("Nombre", )
    e=int(input("Edad", ))
    if(e>=18):
        print ("Mayor de edad")
    else:
        print("Menor de edad")
    
    p1 = Persona(n,e,192837465)
    print (p1.nombre)
if __name__ == "__main__":
    main()