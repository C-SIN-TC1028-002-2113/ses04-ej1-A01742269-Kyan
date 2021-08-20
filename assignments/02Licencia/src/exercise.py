def main():
    #escribe tu código abajo de esta línea
    edad = int(input("Ingresa tu edad: "))
    Ido = int(input("¿Tienes identificación oficial? (s/n): "))

    if edad<18 or edad>=18:
        if edad<18:
           print("No cumples requisitos")
        elif edad>=18:
            print("¿Tienes identificación oficial? (s/n): ")

if __name__ == '__main__':
    main()
