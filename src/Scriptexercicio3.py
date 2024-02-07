import random

numeros_aleatorios = []




numero = int(input('forneça um número: '))
print()


for i in range(numero):
    numeros_aleatorios.append(random.randint(-20, 20))


print(numeros_aleatorios)

soma_negativos = 0
soma_positivos = 0

for num in numeros_aleatorios:
    if num >0:
        soma_positivos = soma_positivos + num
    if num <0:
        soma_negativos = soma_negativos + num

print(soma_positivos)
print(soma_negativos)


