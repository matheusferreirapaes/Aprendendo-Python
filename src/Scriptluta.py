nome = input('Nome do lutador: ')
peso = int(input('Peso do lutador: '))


if peso <= 65:
    print(f'o lutador {nome} pesa {peso} e se enquadra na categoria pena')
elif peso >= 65 and peso <= 72:
    print(f'o lutador {nome} pesa {peso} e se enquadra na categoria leve')
elif peso >= 72 and peso <= 79:
    print(f'o lutador {nome} pesa {peso} e se enquadra na categoria ligeiro')
elif peso >= 79 and peso <= 86:
    print(f'o lutador {nome} pesa {peso} e se enquadra na categoria meio-médio')
elif peso >= 86 and peso <= 93:
    print(f'o lutador {nome} pesa {peso} e se enquadra na categoria médio')
elif peso >= 93 and peso <= 100:
    print(f'o lutador {nome} pesa {peso} e se enquadra na categoria meio-pesado')
else:
    print(f'o lutador {nome} pesa {peso} e se enquadra na categoria pesado')

