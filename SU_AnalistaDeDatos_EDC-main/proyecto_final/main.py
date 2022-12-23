import instrucciones as instrucciones
import juego as jugar
import ajustes as ajustes
import ajustes as prepararArchivo

def menu_principal():
    menu = """
1. Jugar
2. Instrucciones
3. Ajustes
4. Salir
Seleccione: """
    eleccion = int(input(menu))
    if eleccion <= 0 or eleccion >= 4:
        exit()
    if eleccion == 1:
        jugar()
    elif eleccion == 2:
        instrucciones()
    elif eleccion == 3:
        ajustes()


def main():
    prepararArchivo()
    while True:
        menu_principal()
main()