import random

numeros_aleatorios = []




numero = int(input('forneça o numero: '))
print()



for i in range(numero):
        numeros_aleatorios.append(random.randint(1, 30))

print(numeros_aleatorios)
