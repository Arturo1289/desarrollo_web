from cuenta import cuenta

def main ():
    p1 = cuenta("Polaco",5233.89)
    print("Nombre de la cuenta:",p1.titular)
    print("Dinero en cuenta: $",p1.cantidad)
if __name__ == "__main__":
    main()