'''jogador = {
    'Nome': str(input("Digite o nome do jogador: ")),
    'Partidas': int(input("Digite o número de partidas que ele jogou: ")),
    'Gols': [],
    'Total': 0
}
for x in range(0,jogador['Partidas']):
    jogador['Gols'].append(int(input(f'Número de gols na partida {x+1}: ')))
    jogador['Total'] += jogador['Gols'][x]
print(jogador)'''
jogador = dict()
partidas = list()
jogador['Nome'] = str(input("Digite o nome do jogador: "))
tot = int(input("Digite o número de partidas que ele jogou: "))
for c in range(0, tot):
    partidas.append(int(input(f'Número de gols na partida {c+1}: ')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)
jogador['Partidas'] = len(jogador['Gols'])
print(jogador)