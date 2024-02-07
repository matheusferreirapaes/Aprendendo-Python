numero = int(input('forneça um numero: '))
print(f'a tabuada do {numero} é: ')
for i in range(1,11):
    print(f'{numero} x {i} = {i*numero}')
    if numero % 5 == 0:
        print(numero)