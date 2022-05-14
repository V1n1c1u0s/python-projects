palavras = ('Livro','Naruto','Taciturno','Sport','Palmeiras','Leonardo','Michelangelo','Donatello')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos ',end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')