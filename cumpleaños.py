def cumplir_100_años():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    año_actual = 2024
    año_cumplir_100 = año_actual + (100 - edad)
    print(f"{nombre} cumplirá 100 años en el año {año_cumplir_100}")

cumplir_100_años()
