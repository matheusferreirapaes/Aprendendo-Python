jogadores = [
    {
        'nome': 'neymar',
        'gols': 79,
    },
    {
        'nome': 'pele',
        'gols': 77,
    },
    {
        'nome': 'ronaldo',
        'gols': 62,
    },
    {
        'nome': 'romario',
        'gols': 55,
    },
    {
        'nome': 'zico',
        'gols': 48,
    },
    {
        'nome': 'bebeto',
        'gols': 39,
    },
    {
        'nome': 'rivaldo',
        'gols': 35,
    },
    {
        'nome': 'jairzinho',
        'gols': 33,
    },
    {
        'nome': 'ronaldinho',
        'gols': 33,
    },
    {
        'nome': 'ademir',
        'gols': 32,
    },
    {
        'nome': 'tostao',
        'gols': 32,
    },
]

gols = []
for jogador in jogadores:
    gols.append(jogador['gols'])


maior_gol = max(gols)
for jogador in jogadores:
    if jogador['gols'] >= maior_gol:
        print(jogador['nome'])
    




