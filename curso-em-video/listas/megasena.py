from random import randint
from time import sleep
lista = list()
jogo = []
print('MEGA SENA')
num_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1
while total <= num_jogos:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogo.append(lista[:])
    lista.clear()
    total += 1
print(f'Sorteando {num_jogos} jogos...')
for i, l in enumerate(jogo):
    print(f'Jogo {i+1}: {l}')
    sleep(1)