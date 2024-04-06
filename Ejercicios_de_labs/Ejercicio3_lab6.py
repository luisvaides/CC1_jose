n = int(input("Ingrese número de lineas a escribir: "))
if n>0:
    with open("resultado.txt", "w") as file:
        for i in range(1, n + 1):
            linea = input(f"Ingrese linea # {i}: ")
            file.write(linea+"\n")
    print("Las lineas se han escrito en el archivo 'resultado.txt'.")
else:
    print("El número de las lineas deve sers mayor a cero.")
