import dibujo as dibujarIntentos
import dibujo as imprimirAhorcado
import desarrollo as descubrirLetra
import desarrollo as haGanado
import desarrollo as imprimirPalabra
import desarrollo as prepararPalabra
import desarrollo as imprimirPalabraOriginal
import select_palabra as obtenerPalabra

def jugar():
    global letrasEscritas
    global intentos
    intentos = 6
    letrasEscritas = []
    palabra = obtenerPalabra()
    prepararPalabra(palabra)
    while True:
        imprimirAhorcado()
        dibujarIntentos()
        imprimirPalabra()
        descubrirLetra(input("Ingresa la letra: "))
        if intentos <= 0:
            print("Perdiste. La palabra era: ")
            imprimirPalabraOriginal()
            return
        if haGanado():
            print("Ganaste")
            return