nome = 'carlos' 
nomes = ['calor', 'alberto', 'matheus']
pessoa = {
    'altura': 1.80,
    'peso': 80,
} 
clientes = [ #array
    {'id': 1, 'nome': 'matheus', 'cliente': True},#objeto dentro do array
    {'id': 2, 'nome': 'alberto', 'cliente': False},
]



if clientes[1]['nome'] == 'matheus': 
    print('essa pessoa é o matheus')
else: 
    print('essa pessoa não é o matheus')