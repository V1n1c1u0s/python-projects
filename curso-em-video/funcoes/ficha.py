def ficha(jogador='<desconhecido>', gol = 0):
    print(f"O jogador {jogador} fez {gols} gol(s) no campeonato.")

nome = input("Digite o nome do jogador: ")
gols = input("Digite o número de gols: ")

'''if nome == '':
    nome = '<desconhecido>'
if gols == '':
    gols = 0'''

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome,gols)