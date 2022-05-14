tabela = []
jogador = dict()
partidas = list()
while True:
    print('-'*30)
    jogador.clear()
    partidas.clear()
    jogador['Nome'] = str(input("Digite o nome do jogador: "))
    tot = int(input("Digite o número de partidas que ele jogou: "))
    for c in range(0, tot):
        partidas.append(int(input(f'Número de gols na partida {c+1}: ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    tabela.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar cadastrando? ')).upper()[0]
        if resp in 'SN':
            break
        print('Responda apenas com S ou N')
    if resp == 'N':
        break
print('-='*30)
print('cod ',end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for x,y in enumerate(tabela):
    print(f'{str(x):>3} ',end='')
    for z in y.values():
        print(f'{str(z):<15}',end='')
    print()
while True:
    print('-'*40)
    resp = int(input('Mostrar dados de qual jogador: (999 pra parar) '))
    if resp == 999:
        break
    if resp >= len(tabela):
        print(f'    Não existe jogador com código {resp}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {tabela[resp]["Nome"]}')
        for m,k in enumerate(tabela[resp]["Gols"]):
            print(f'    Na partida {m+1} fez {k} gols')
print('-'*40)