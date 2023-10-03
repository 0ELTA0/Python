frase = "Son las 8 de la noche y ya me quiero ir"
numero = "7"
if numero in frase:
    numeroNew = int(numero)
    if numeroNew < 8 :
        print("Es hora de irnos son las :", numeroNew)
else :
    print("Ya son mas de las 7 ")
