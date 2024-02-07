livros = [
    {
        "titulo": "pai rico pai pobre",
        "ano":1997,
        "paginas": 192,
        "escritor": 'robert kiyosaki',
        "vendas": 26000000,
    },

     {
        'titulo': 'o poder do subconsciente',
        'ano': 1963,
        'paginas': 320,
        'escritor': 'dr joseph murphy',
        'vendas': 12658,
    },

     {
        'titulo': 'desperte seu gigante interior',
        'ano': 1992,
        'paginas': 616,
        'escritor': 'tony robbins',
        'vendas': 1400000,
    },

     {
        'titulo': 'engenharia interior',
        'ano': 2008,
        'paginas': 272,
        'escritor': 'sadhguru',
        'vendas': 7982,
    },

     {
        'titulo': 'o que todo corpo fala',
        'ano': 2021,
        'paginas':240,
        'escritor': 'joe navarro',
        'vendas':1200000,
    },

     {
        'titulo': 'psicologia financeira',
        'ano': 2021,
        'paginas': 260,
        'escritor': 'morgan housel',
        'vendas': 8369,
    },

     {
        'titulo': 'nós queremos que voce fique rico',
        'ano': 2004,
        'paginas': 352,
        'escritor': 'donald trump',
        'vendas': 8126,
    },

     {
        'titulo': 'poder do habito',
        'ano': 2012,
        'paginas': 408,
        'escritor': 'charles duhigg',
        'vendas': 10265,
    },

     {
        'titulo': 'o poder da acao',
        'ano': 2015,
        'paginas': 256,
        'escritor': 'paulo vieira',
        'vendas': 9383,
    },

]

#livro está acessando os dados do array, que é livros
for livro in livros:
#no if eu acesso a lista de objetos do array e chamo a chave que eu quero, que é vendas e dou a ordem para que seja maior que 9000
    if livro['vendas'] > 9000:
        print(livro)

#print vazio para quebrar linha
print()

#mais uma vez crio uma variavel para acessar os dados do array
for livro1 in livros:
#acesso essa variavel, onde terá os dados e faço duas solicitações uma que acesse a chave ano e a proxima a chave paginas
    if livro1['ano'] > 1900 and livro1['paginas'] > 300:
        print(livro1) 


print()

#eu quis apenas as paginas do livros 
for pagina in livros:
    print(pagina['paginas'])

print()


for livros2 in livros:
    if livros2['vendas'] > 5000 and livros2['ano'] > 2010:
        print(livros2)
        

for autor in livros:
    print(autor['escritor'])


print()


#criei uma variavel vazia, depois criei o livros3 para acessar os dados do livro e adicionei valor a variavel pelo append
vendido = []
for livros3 in livros:
    vendido.append(livros3['vendas'])

#aqui eu criei uma outra variavel e pedi para ela pegar o valor maximo da variavel vendido
maior_venda = max(vendido)
for livros3 in livros:
    if livros3['vendas'] >= maior_venda: #chamei o if e pedi para ele acessar o for, puxando os dados do array, principalmente em vendas
        print(livros3['escritor'])

print()

paginas = []
for livros4 in livros:
    paginas.append(livros4['paginas'])



maior_pagina = max(paginas)
for livros4 in livros:
    if livros4['paginas'] >= maior_pagina:
        print(livros4['paginas'])