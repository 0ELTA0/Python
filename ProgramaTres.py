numeros = [1, 2, 2, 3, 4, 4]
numerosSet = set(numeros)
sumaLista = sum(numeros)
sumaSet = sum(numerosSet)
len(numerosSet)
max(numeros)
min(numeros)

diccionario= {"Numeros Unicos:":len(numerosSet) , "Suma de la Lista: ": sumaLista, "Suma del Set: ":sumaSet, "Valor Maximo: ":max(numeros), "Valor Minimo: ": min(numeros) }

print(diccionario)
