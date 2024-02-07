lista_de_numeros = []
while True:
    entrada = input('forneça um numero: ')

    if entrada == 'x':
        break

    numero = int(entrada)

    if numero > 0:
        lista_de_numeros.append(numero)


print(lista_de_numeros)

for i in lista_de_numeros:
    if i % 2 == 0 or i % 3 == 0:
        print(i)
  
