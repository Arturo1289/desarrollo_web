import instrucciones
import juego as jugar

def main():
    menu_principal()

def menu_principal():
    menu = """
1. Jugar
2. Instrucciones
3. Salir
Seleccione: """
    eleccion = int(input(menu))
    if eleccion <= 0 or eleccion >= 3:
        exit()
    if eleccion == 1:
        jugar()
    elif eleccion == 2:
        instrucciones()

main()