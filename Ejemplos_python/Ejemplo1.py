ejex = int(input("Ingrese la coordenada del eje x: "))
ejey = int(input("Ingrese la coordenada del eje y: "))

print()

if (ejex > 0) and (ejey > 0) :
    print("La coordenada se encuentra en el cuadrante I.")

elif (ejex < 0) and (ejey > 0):
    print("La coordenada se encuentra en el cuadrante II.")

elif (ejex < 0) and (ejey < 0) :
    print("La coordenada se encuentra en el cuadrante III.")

elif (ejex > 0) and (ejey < 0) :
    print("La coordenada se encuentra en el cuadrante IV.")

elif (ejex == 0) and (ejey == 0):
    print("La coordenada se encuentra en el centro de el plano cartesiano.")

else:
    print("El punto esta sobre los ejes.")

print()