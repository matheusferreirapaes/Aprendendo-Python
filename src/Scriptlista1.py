
frutas = ["apple", "banana", "cherry", "morango", "manga"]

for f in range(len(frutas)):
    print(f'as frutas que tem na lista é {frutas[f]}')

    print()

for f1 in range(len(frutas)):
    print(f'a primeira fruta da lista é {frutas[0]} e a última fruta da lista é {frutas[4]}')


print()

print()


sacolao = [
    {
        'fruta': 'maça',
        'preço_kg': 7.22,
    },
    {
        'fruta': 'banana',
        'preço_kg': 3.25,
    },
    {
        'fruta': 'cereja',
        'preço_kg': 79.00,
    },
    {
        'fruta': 'morango',
        'preço_kg': 13.19,

    },
    {
        'fruta': 'manga',
        'preço_kg': 3.90,

    },
]


for p in range(len(sacolao)):
    print(f'o preço a pagar por maça foi {sacolao[2*0]}')
    print()
    print(f'o preço a pagar pela banana é {sacolao[1*1]}')
    print()
    print(f'o preço a pagar pela cereja é{sacolao[1*2]}')
    print()
    print(f'o preço a pagar pelo morango é {sacolao[1*3]}')
    print()
    print(f'o preço a pagar pela manga é {sacolao[1*4]}')
    print()

valores = [7.22, 3.25, 79.0, 13.19, 3.9]


def sum_list(some_list):
    total = 0
    for valores in some_list:
        total += valores
    return total

    
total = sum_list(valores)
total
