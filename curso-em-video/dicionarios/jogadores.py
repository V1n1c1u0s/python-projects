from random import randint
from time import sleep
from operator import itemgetter
resultados = dict()
print('Valores sorteados:')
for i in range(1,5):
    resultados[f'jogador{i}'] = randint(1,6)
    sleep(1)
    print(f'    Jogador {i} tirou {resultados[f"jogador{i}"]}')
ranking = {}
ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
print('Ranking:')
for x,y in enumerate(ranking):
    sleep(1)
    print(f'    {x+1}° Lugar - {y[0]} com {y[1]} pontos!')