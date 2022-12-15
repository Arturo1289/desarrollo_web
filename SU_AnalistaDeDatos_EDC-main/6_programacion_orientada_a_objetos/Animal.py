class Animal:
    def __init__(self,especie,dieta,habitad):
        self.especie=especie
        self.dieta=dieta
        self.habitad=habitad
        
    def comer(self):
        print(f"Comiendo:{self.especie}")
    
    def que_soy(self):
        return f"soy un {self.especie} y vivo en {self.habitad}"

    def __str__(self):
        return f"hola soy un {self.especie}"