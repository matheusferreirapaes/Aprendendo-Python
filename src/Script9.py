filmes = [
    {
        "titulo": "O Segredo dos Diamantes",
        "ano": 2014,
        "diretor": "Helvécio Ratton",
        "genero": "Aventura",
        "classificacao": 12
    },
    {
        "titulo": "Estrelas Além do Tempo",
        "ano": 2016,
        "diretor": "Theodore Melfi",
        "genero": "Drama",
        "classificacao": 10
    },
    {
        "titulo": "A Origem",
        "ano": 2010,
        "diretor": "Christopher Nolan",
        "genero": "Ficção Científica",
        "classificacao": 14
    },
    {
        "titulo": "Os Vingadores",
        "ano": 2012,
        "diretor": "Joss Whedon",
        "genero": "Ação",
        "classificacao": 12
    },
    {
        "titulo": "Coco",
        "ano": 2017,
        "diretor": "Lee Unkrich",
        "genero": "Animação",
        "classificacao": 6
    },
    {
        "titulo": "O Senhor dos Anéis: A Sociedade do Anel",
        "ano": 2001,
        "diretor": "Peter Jackson",
        "genero": "Aventura",
        "classificacao": 12
    },
    {
        "titulo": "Pulp Fiction: Tempo de Violência",
        "ano": 1994,
        "diretor": "Quentin Tarantino",
        "genero": "Crime",
        "classificacao": 18
    },
    {
        "titulo": "Jurassic Park",
        "ano": 1993,
        "diretor": "Steven Spielberg",
        "genero": "Aventura",
        "classificacao": 10
    },
    {
        "titulo": "A Bela e a Fera",
        "ano": 1991,
        "diretor": "Gary Trousdale e Kirk Wise",
        "genero": "Animação",
        "classificacao": 6
    },
    {
        "titulo": "Matrix",
        "ano": 1999,
        "diretor": "The Wachowskis",
        "genero": "Ficção Científica",
        "classificacao": 14
    },
    {
        "titulo": "Titanic",
        "ano": 1997,
        "diretor": "James Cameron",
        "genero": "Romance",
        "classificacao": 12
    },
    {
        "titulo": "O Rei Leão",
        "ano": 1994,
        "diretor": "Roger Allers e Rob Minkoff",
        "genero": "Animação",
        "classificacao": 6
    }
]



for dados in filmes:
    if dados['classificacao'] < 8:
        print(dados)

print()

for filme in filmes:
    if filme['ano'] > 2015:
        print(filme)


print()


for teste in filmes:
    if teste['classificacao'] > 8 and teste['ano'] > 1999:
        print(teste)


print()


for teste1 in filmes:
    if teste1['diretor'] == 'Quentin Tarantino':
        print(teste1['titulo'])


print()


for teste2 in filmes:
    if teste2['titulo'] == 'O Rei Leão':
        print(teste2['diretor'])