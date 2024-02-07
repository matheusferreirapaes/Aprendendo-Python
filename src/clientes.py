clientes = [
    {'id': 1, 'nome': 'matheus', 'cliente': True},
    {'id': 2, 'nome': 'alberto', 'cliente': False},
    {
        "id": 3,
        "nome": "Maria Silva",
        "cliente": True,
    },
    {
        "id": 4,
        "nome": "João Pereira",
        "cliente": False,
    },
    {
        "id": 5,
        "nome": "Pedro Santos",
        "cliente": True,
    },
    {
        "id": 6,
        "nome": "Ana Costa",
        "cliente": False,
    },
    {
        "id": 7,
        "nome": "Luísa Sousa",
        "cliente": True,
    },
    {
        "id": 8,
        "nome": "José Martins",
        "cliente": False,
    },
    {
        "id": 9,
        "nome": "Carlos Oliveira",
        "cliente": True,
    },
    {
        "id": 10,
        "nome": "Pedro Silva",
        "cliente": False,
    },
]

for elemento in clientes:
    if elemento['cliente'] == True:
        print(f'nome do cliente {elemento["nome"]}')