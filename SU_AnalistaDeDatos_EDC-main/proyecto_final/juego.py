import os
import random

palabraAdivinada = []
letrasEscritas = []
intentos = 6
palabraSecretaAjustes = "1"
nombreArchivoGrupos = "grupos.txt"


def prepararPalabra(original):
    global palabraAdivinada
    original = original.lower()
    palabraAdivinada = []
    for letra in original:
        palabraAdivinada.append({
            "letra": letra,
            "adivinada": False,
        })


def imprimirPalabra():
    for letraCompuesta in palabraAdivinada:
        if letraCompuesta["adivinada"]:
            print(letraCompuesta["letra"], end="")
        else:
            print("-", end="")
    print("")


def imprimirPalabraOriginal():
    for letraCompuesta in palabraAdivinada:
        print(letraCompuesta["letra"], end="")


def descubrirLetra(letraDeUsuario):
    global palabraAdivinada
    global letrasEscritas
    global intentos
    letraDeUsuario = letraDeUsuario.lower()
    if letraDeUsuario in letrasEscritas:
        return
    else:
        letrasEscritas.append(letraDeUsuario)
    if not letraEstaEnPalabra(letraDeUsuario):
        intentos -= 1
    else:
        for letraCompuesta in palabraAdivinada:
            if letraCompuesta["letra"] == letraDeUsuario:
                letraCompuesta["adivinada"] = True


def letraEstaEnPalabra(letra):
    global palabraAdivinada
    for letraCompuesta in palabraAdivinada:
        if letraCompuesta["letra"] == letra:
            return True
    return False


def imprimirAhorcado():
    if intentos == 1:
        print("""
                       ___
                      |   |
                     _O/  |
                      |   |
                     / \  |
                    ______|
        """)
    elif intentos == 2:
        print("""
                       ___
                      |   |
                     _O/  |
                      |   |
                       \  |
                    ______|
        """)
    elif intentos == 3:
        print("""
                       ___
                      |   |
                     _O/  |
                      |   |
                          |
                    ______|
        """)
    elif intentos == 4:
        print("""
                       ___
                      |   |
                     _O/  |
                          |
                          |
                    ______|
        """)
    elif intentos == 5:
        print("""
                       ___
                      |   |
                      O/  |
                          |
                          |
                    ______|
        """)
    elif intentos == 6:
        print("""
                       ___
                      |   |
                      O   |
                          |
                          |
                    ______|
        """)


def dibujarIntentos():
    print("Intentos restantes: " + str(intentos))


def haGanado():
    global palabraAdivinada
    for letra in palabraAdivinada:
        if not letra["adivinada"]:
            return False
    return True