lista = []
informacoes = []
boletim = []
while True:
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    informacoes.extend((nome,[nota1,nota2]))
    lista.append(informacoes[:])
    informacoes.clear()
    resposta = str(input('Deseja continuar cadastrando? [S/N]'))
    if resposta in 'Nn':
        break
for x in lista:
    nota = 0
    for y in x[1]:
        nota += y
    nota = nota/2
    informacoes.extend((lista[x][0],nota))
    boletim.append(informacoes[:])
    informacoes.clear()
for x in range(len(boletim)):
    print(f'{x}  {boletim[x][0]}   {boletim[x][1]}')
while True:
    opcao = int(input('Mostrar nota de qual aluno? [999 interrompe] '))
    if opcao == 999:
        break
    novaLista = [lista[opcao][1],lista[opcao][2]]
    print(f'Notas de {lista[opcao][0]} é {novaLista}')