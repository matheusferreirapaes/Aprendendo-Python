nome = input('Nome do lutador(a): ')
peso = int(input('Peso do lutador(a): '))
libra = peso*2.2
altura = float(input('altura do lutador(a): '))

if peso <= 56:
    print(f'O lutador(a) {nome} pesa em kg {peso} e em libra {libra} com uma altura de {altura} metros e se enquadra na categoria mosca')
elif peso <= 61:
    print(f'o lutador(a) pesa em kg {peso} e seu peso em libras é {libra} sua altura em metros é {altura} e se enquadra na categoria galo')
elif peso <= 65:
    print(f'o lutador(a) pesa em kg {peso} e seu peso em libras é {libra} sua altura em metros é {altura} e se enquadra na categoria pena')
elif peso <= 70:
    print(f'O lutador(a) pesa em kg {peso} e seu peso em libra é {libra} e sua altura em mentros é {altura} e se enquadra na categoria leve')
elif peso <= 77:
    print(f'o lutador(a) pesa em kg {peso} e seu peso em libras é {libra} e sua altura em metros é {altura} se enquadra na categoria meio-médio')
elif peso <= 83:
    print(f'o lutador(a) pesa em kg {peso} e seu peso em libras é {libra} e sua altura em metros é {altura} se enquadra na categoria médio')
elif peso <= 92:
    print(f'o lutador(a) pesa em kg {peso} e seu peso em libras é {libra} e sua altura em metros é {altura} se enquadra na categoria meio-pesado')
elif peso <= 120:
    print(f'o lutador(a) pesa em kg {peso} e seu peso em libras é {libra} sua altura em metro é {altura} se enquadra na categoria pesado')
else:
    print(f'o lutador(a) pesa em kg {peso} sua altura em metros é {altura} e se enquadra na categoria superpesado') 