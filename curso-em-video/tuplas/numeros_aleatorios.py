from random import randint
from random import randint

tupla = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

print('Valores sorteados: ', end='')

for x in tupla:
    print(f'{x} ', end='')
print(f'\nMaior valor sorteado foi: {max(tupla)}')
print(f'Menor valor sorteado foi: {min(tupla)}')


'''
tupla_ordenada = sorted(tupla)
print(f'Menor valor da tupla - {tupla_ordenada[0]}',end='\n')
print(f'Maior valor da tupla - {tupla_ordenada[len(tupla_ordenada)-1]}')
'''