def main():
    #escribe tu código abajo de esta línea
    n1 = int(input("Ingresa el primer número: "))
    n2 = int(input("Ingresa el segundo número: "))
    n3 = int(input("Ingresa el tercer número: "))

    if n1>n2 and n1>n3:
        print(n1)
    elif n2>n1 and n2>n3:
        print(n2)
    else:
        print(n3)

if __name__=='__main__':
    main()
