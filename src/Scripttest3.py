dados_futebol = [
    {
        'nome': 'Neymar Jr.',
        'posicao': 'Atacante',
        'idade': 29,
        'clube': 'Paris Saint-Germain',
        'valor_mercado': 160000000,
        'gols_na_temporada': 25
    },
    {
        'nome': 'Lionel Messi',
        'posicao': 'Atacante',
        'idade': 34,
        'clube': 'Paris Saint-Germain',
        'valor_mercado': 180000000,
        'gols_na_temporada': 30
    },
    {
        'nome': 'Cristiano Ronaldo',
        'posicao': 'Atacante',
        'idade': 36,
        'clube': 'Manchester United',
        'valor_mercado': 120000000,
        'gols_na_temporada': 20
    },
    {
        'nome': 'Kevin De Bruyne',
        'posicao': 'Meio-campista',
        'idade': 30,
        'clube': 'Manchester City',
        'valor_mercado': 140000000,
        'gols_na_temporada': 10
    },
    {
        'nome': 'Virgil van Dijk',
        'posicao': 'Defensor',
        'idade': 30,
        'clube': 'Liverpool',
        'valor_mercado': 100000000,
        'gols_na_temporada': 3
    },
    {
        'nome': 'Kylian Mbappé',
        'posicao': 'Atacante',
        'idade': 22,
        'clube': 'Paris Saint-Germain',
        'valor_mercado': 200000000,
        'gols_na_temporada': 35
    },
    {
        'nome': 'Joshua Kimmich',
        'posicao': 'Meio-campista',
        'idade': 26,
        'clube': 'Bayern de Munique',
        'valor_mercado': 110000000,
        'gols_na_temporada': 8
    },
    {
        'nome': 'Trent Alexander-Arnold',
        'posicao': 'Defensor',
        'idade': 23,
        'clube': 'Liverpool',
        'valor_mercado': 90000000,
        'gols_na_temporada': 5
    },
    {
        'nome': 'Erling Haaland',
        'posicao': 'Atacante',
        'idade': 21,
        'clube': 'Borussia Dortmund',
        'valor_mercado': 150000000,
        'gols_na_temporada': 28
    },
    {
        'nome': 'Bruno Fernandes',
        'posicao': 'Meio-campista',
        'idade': 27,
        'clube': 'Manchester United',
        'valor_mercado': 120000000,
        'gols_na_temporada': 15
    }
]

valor = []
for mercado in dados_futebol:
    valor.append(mercado['valor_mercado'])

maior_valor = max(valor)
for mercado in dados_futebol:
    if mercado['valor_mercado'] >= maior_valor:
        print(mercado['nome'])


gols = []
for gol in dados_futebol:
    gols.append(gol['gols_na_temporada'])


maior_gol = max(gols)
for gol in dados_futebol:
    if gol['gols_na_temporada'] >= maior_gol:
        print(gol['nome'])