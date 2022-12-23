import dibujo as dibujarIntentos
import dibujo as imprimirAhorcado
import desarrollo as descubrirLetra
import desarrollo as haGanado
import desarrollo as imprimirPalabra
import desarrollo as prepararPalabra
import desarrollo as imprimirPalabraOriginal
import ajustes as obtenerPalabra
import ajustes as grupos
import ajustes as obtenerGrupos
import ajustes as palabras

def jugar():
    global letrasEscritas
    global intentos
    intentos = 6
    letrasEscritas = []
    grupos.obtenerGrupos = obtenerGrupos.obtenerGrupos()
    obtenerGrupos.obtenerGrupos = palabras.obtenerPalabrasDeGrupo(palabras)
    palabras.palabra = obtenerPalabra.obtenerPalabrasDeGrupo()
    prepararPalabra(palabras)
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