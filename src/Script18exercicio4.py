
numero_inicio = int(input('Número de Inicio: '))
numero_fim = int(input('Número fim: '))


if numero_inicio > numero_fim:
    temporario = numero_inicio
    numero_inicio = numero_fim
    numero_fim = temporario

    print(numero_inicio, numero_fim)

print()

for i in range(numero_inicio, numero_fim + 1):
    if i % 5 == 0:
        print(i)