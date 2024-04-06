def parentesis(expresion): 

    if len(expresion) == 2:
        print("Error en la expresión")
        return

    par_abiertos = 0
    par_cerrados = 0
  
    for char in expresion:
        if char == '(':
            par_abiertos += 1
        elif char == ')':
            par_cerrados += 1

    if par_abiertos != par_cerrados or expresion[0] != '(' or expresion[-1] != ')':
        print("Error en la expresión")
        return
    
    quitar_par = expresion[1:-1]
    print(quitar_par)

val1 = input("Ingrese una expresión entre paréntesis: ")

parentesis(val1)