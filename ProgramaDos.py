print("Ingresa tu nombre")
nombre = input()
nombreDividido = nombre.split('-')
nombreCompleto = ''
for palabra in nombreDividido:
    nombreCompleto += palabra.capitalize() + ' '

print('Hola '+nombreCompleto)
