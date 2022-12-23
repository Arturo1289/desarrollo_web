import random

nivel_1 = ["Esternocleidomastoideo",
"Otorrinolaringólogo",
"Idiosincrasia",
"Desoxirribonucleico",
"Paralelepípedo",
"Ovovivíparo",
"Caleidoscopio",
"Electroencefalografista"]

nivel_2 = ["Galactus",
"Google",
"Catalogo",
"Zapato",
"Raton",
"Reaccion",
"Misterios",
"Mercado"]
PAL={1:nivel_1, 2:nivel_2}

def seleccionar_palabra(nivel:int)->str:
    tamañonivel:int = len(PAL.get(nivel))
    palabra_random:int = random.randint(0,tamañonivel-1)
    recuperarListaPalabra:list=PAL.get(nivel)
    return recuperarListaPalabra[palabra_random]