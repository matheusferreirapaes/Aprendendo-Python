nomes = ["matheus", "alberto"]
numeros = [7, 10, 23, 45, 51]
print(numeros[0] + numeros[1] + numeros[2] + numeros[3] + numeros[4])

livros = [
    {
        "nomes": "o homem mais rico da babilonia",
        "paginas": 298,
    },
    {
        "nomes": "pai rico e pai pobre",
        "paginas": 286,
    },
    {
        "nomes": "desperte seu gigante interior",
        "paginas": 623,
    },
    {
        "nomes": "o poder do subconsciente",
        "paginas": 323,
    },
    {
        "nomes": "psicologia financeira",
        "paginas": 236,
    },
]


for livro in livros:
    print(livro['nomes'])





for numero in numeros:
    print(numero*2)