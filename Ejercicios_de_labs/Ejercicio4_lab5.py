"""Complete el programa definido en el archivo ejercicio3.py con la siguiente subrutina:

Una funcion llamada generarPlaca la cual genere un número de placa aleatoriamente y lo devuelva en formato String. El número de placa debe cumplir con las siguientes características:

Debe tener un length = 6
Los primeros 3 caracteres deben ser dígitos del 0 al 9. Los tres dígitos deben ser generados aleatoriamente cada uno por separado (es decir que pueden o no ser iguales).
Los siguientes 3 caracteres deben ser letras mayúsculas entre la A y la Z, cumpliendo con los mismos requisitos que los dígitos.
		Ejemplo de placas válidas: 257NGH, 099AGK, 364PLT"""
import re
import random 
def generarPlaca():
  
  val_letra= ""
  val_digito = ""

  for i in range(1,4):
    numero = random.randint(0,9)
    val_digito += str(numero)

  for e in range(1,4):
    letra_al = random.randint(65,90)
    letra = chr(letra_al)
    val_letra += letra
  val_placa = val_digito + val_letra
  return val_placa
 
  # por el momento retornaremos 'x' para que el programa funcione
  # --------------------------

# **********************************************************
# ********** NO MODIFIQUE CODIGO DESDE ACA ******************
def generarListaDePlacas(n):
    placas = []
    for count in range(n):
        placas.append(generarPlaca())
    return placas

def datoscuriosos(lista):
    digits = [0]*10
    outd = 0
    outl = 0
    notstr = 0
    letters = [0]*26
    nolength = 0
    for count in range(len(lista)):
        current = lista[count]
        if isinstance(current, str):
            if len(current) == 6:
                for pos in range(3):
                    try :
                        c = int(current[pos])
                        if (c >= 0) and (c <= 9):
                            digits[c] = digits[c] + 1
                        else:
                            outd += 1
                    except ValueError:
                        outd = outd + 1
                for pos in range(3,6):
                    c = ord(current[pos])
                    if (c >= 65) and (c <= 90):
                        letters[c - 65] = letters[c - 65] + 1
                    else:
                        outl += 1
            else:
                nolength += 1
        else:
            notstr += 1

    print('\nDATOS IMPORTANTES:\n------------------------')
    if notstr != 0:
        print('Cantidad de placas que no son Strings:', notstr)
    if nolength != 0:
        print('Cantidad de placas que no tienen length = 6:', nolength)

    if not(notstr == len(lista)) and not(nolength == len(lista)):
        for pos in range(len(digits)):
            if digits[pos] == 0:
                print('El digito',pos,'no se genero ninguna vez')
        if outd != 0:
            print('Cantidad de digitos invalidos:',outd)
        for pos in range(len(letters)):
            if letters[pos] == 0:
                print('La letra',chr(65 + pos),'no se genero ninguna vez')
        if (outl != 0):
            print('Cantidad de letras invalidas:',outl)

def isValid(sstr):
    if isinstance(sstr,str):
        match = re.search('^\d{3}[A-Z]{3}$', sstr)
        if match:
            return True
    return False

def autoevaluacion():
    print("----------------------------")
    print(" MODO AUTOEVALUACION")
    print("----------------------------")
    cantidad = 100
    listaDePlacas = generarListaDePlacas(cantidad)
    print('Se generaron',cantidad,"placas")
    notcorrect = []
    incorrect = 0
    for count in range(cantidad):
        if not(isValid(listaDePlacas[count])) :
            notcorrect.append(listaDePlacas[count])
            incorrect += 1
    print('De estas',(cantidad - incorrect),'cumplen con el formato correcto.')
    if incorrect != 0:
        print('Placas generadas con formato incorrecto:')
        print(notcorrect)

    nota = round(100 * ((cantidad - incorrect) / cantidad ), 0)
    print('Usted sacaria',nota,'% en este ejercicio (aprox)')
    datoscuriosos(listaDePlacas)

def interactiva():
    print("----------------------------")
    print(" MODO INTERACTIVO")
    print("----------------------------")
    try:
        cantidad = int(input('Ingrese cantidad de placas a generar:'))
        listaDePlacas = generarListaDePlacas(cantidad)
        print('Placas generadas: ')
        print(listaDePlacas)
    except ValueError:
        print('ERROR! Cantidad Ingresada invalida\n')

def menu():
	print(' CC1 - 2022 - Lab 05 - Ejercicio3')
	print('---------------------------------')
	opcion = 0
	while(opcion != 3) :
		print('\nOpciones de testing:')
		print('(1) Modo autoevaluacion\n(2) Modo interactivo\n(3) Salir del programa\n')
		try:
			opcion = int(input("Ingrese su opcion: "))
			if opcion == 1:
				autoevaluacion()
			elif opcion == 2:
				interactiva()
			elif opcion == 3:
				print("Saliendo del programa ...")
			else:
				print("ERROR: Opcion invalida! Solo hay opciones 1, 2 o 3\n")
		except ValueError:
			print("ERROR: Opcion invalida! No ingreso un numero entero\n")
			opcion = 0

menu()