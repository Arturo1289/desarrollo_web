import os
palabraSecretaAjustes = "1"
nombreArchivoGrupos = "grupos.txt"

def ajustes():
    if input("Ingrese la contraseña: ") != palabraSecretaAjustes:
        print("Contraseña incorrecta")
        return
    menu = """
1. Eliminar grupo de palabras
2. Crear grupo de palabras
3. Modificar grupo de palabras
"""
    grupos = obtenerGrupos()

    eleccion = int(input(menu))
    if eleccion <= 0 or eleccion > 3:
        print("No válido")
        return
    if eleccion == 1:
        eliminarGrupoDePalabras(grupos)
    elif eleccion == 2:
        crearGrupoDePalabras(grupos)
    elif eleccion == 3:
        modificarGrupoDePalabras(grupos)


def eliminarGrupoDePalabras(grupos):
    indice = imprimirGruposYSolicitarIndice(grupos)
    grupoEliminado = grupos[indice]
    del grupos[indice]
    os.unlink(grupoEliminado + ".txt")
    escribirGrupos(grupos)


def imprimirGruposYSolicitarIndice(grupos):
    for i, grupo in enumerate(grupos):
        print(f"{i + 1}. {grupo}")
    return int(input("Seleccione el grupo: ")) - 1


def crearGrupoDePalabras(grupos):
    grupo = input("Ingrese el nombre del grupo: ")
    palabras = solicitarPalabrasParaNuevoGrupo()
    escribirPalabrasDeGrupo(palabras, grupo)
    grupos.append(grupo)
    escribirGrupos(grupos)
    print("Grupo creado correctamente")


def escribirGrupos(grupos):
    with open(nombreArchivoGrupos, "w") as archivo:
        for grupo in grupos:
            archivo.write(grupo + "\n")


def escribirPalabrasDeGrupo(palabras, grupo):
    with open(grupo + ".txt", "w") as archivo:
        for palabra in palabras:
            archivo.write(palabra + "\n")


def solicitarPalabrasParaNuevoGrupo():
    palabras = []
    while True:
        palabra = input("Ingrese la palabra. Deje la cadena vacía si quiere terminar: ")
        if palabra == "":
            return palabras
        palabras.append(palabra)


def modificarGrupoDePalabras(grupos):
    indice = imprimirGruposYSolicitarIndice(grupos)
    grupoQueSeCambia = grupos[indice]
    palabras = obtenerPalabrasDeGrupo(grupoQueSeCambia)
    menu = """
1. Cambiar una palabra
2. Agregar una palabra
3. Eliminar una palabra
Seleccione: """
    eleccion = int(input(menu))
    if eleccion <= 0 or eleccion > 3:
        print("No válido")
        return
    if eleccion == 1:
        cambiarUnaPalabra(grupoQueSeCambia, palabras)
    elif eleccion == 2:
        agregarUnaPalabra(grupoQueSeCambia, palabras)
    elif eleccion == 3:
        eliminarUnaPalabra(grupoQueSeCambia, palabras)


def cambiarUnaPalabra(grupo, palabras):
    indice = imprimirPalabrasYSolicitarIndice(palabras)
    palabraCambiada = palabras[indice]
    print("Se cambia la palabra " + palabraCambiada)
    nuevaPalabra = input("Ingrese la nueva palabra: ")
    palabras[indice] = nuevaPalabra
    escribirPalabrasDeGrupo(palabras, grupo)
    print("Palabra cambiada correctamente")


def agregarUnaPalabra(grupo, palabras):
    palabra = input("Ingrese la palabra que se agrega: ")
    palabras.append(palabra)
    escribirPalabrasDeGrupo(palabras, grupo)
    print("Palabra agregada correctamente")


def eliminarUnaPalabra(grupo, palabras):
    indice = imprimirPalabrasYSolicitarIndice(palabras)
    del palabras[indice]
    escribirPalabrasDeGrupo(palabras, grupo)
    print("Palabra eliminada correctamente")


def imprimirPalabrasYSolicitarIndice(palabras):
    for i, palabra in enumerate(palabras):
        print(f"{i + 1}. {palabra}")
    return int(input("Seleccione la palabra: ")) - 1


def obtenerGrupos():
    grupos = []
    with open(nombreArchivoGrupos) as archivo:
        for linea in archivo:
            linea = linea.rstrip()
            grupos.append(linea)
    return grupos


def obtenerPalabrasDeGrupo(grupo):
    palabras = []
    with open(grupo + ".txt") as archivo:
        for linea in archivo:
            linea = linea.rstrip()
            palabras.append(linea)
    return palabras


def prepararArchivo():
    if not os.path.isfile(nombreArchivoGrupos):
        with open(nombreArchivoGrupos, "w") as archivo:
            archivo.write("")