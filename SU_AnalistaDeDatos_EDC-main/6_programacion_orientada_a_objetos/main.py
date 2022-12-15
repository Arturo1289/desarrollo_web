from Persona import Persona
from Mascota import Mascota
from Animal import Animal
def main():
    animal1 = Mascota("Perro","Obnivoro","Casa")
    animal2 = Mascota("Cocodrilo","Carnivoro","Pantano")
    animal3 = Animal("Elefante","Hervivoro","Sabana")
    animal1.setNombre("Firulais")
    animal2.setNombre("Coco")
    
    p1 = Persona("Alfonso",30,1.75)
    p2 = Persona("Diego",20,1.80)
    p3 = Persona("Karina",15,1.70)
    
    p1.saludar()
    p1.hablar("Hola a todos, como estan?")
    p1.adoptarMascota(animal1)
    p1.quien_es_mi_mascota()
    p2.hablar("Que tal todos")
    p3.adoptarMascota(animal2)
    p3.hablar("mi mascota es:")
    p3.quien_es_mi_mascota()
    
    # print("preguntas animales")
    # print(p1.mascota.nombre)
    # print(p3.mascota.nombre)
    
    print(p2)
    print(animal1)
    print("---------------------------------------")
    print(p3.nombre)
    p3.edad = 18
if __name__ == "__main__":
    main()