pessoas = list()
dados = list()
pessoaPesada = ''
pessoaLeve = ''
maiorpeso = menorpeso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maiorpeso = menorpeso = dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        if dados[1] < menorpeso:
            menorpeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resposta = str(input('Deseja continuar? [S/N] '))
    if resposta in 'Nn':
        break
for y in pessoas:
    if y[1] == maiorpeso:
        pessoaPesada += f'[{y[0]}] '
    elif y[1] == menorpeso:
        pessoaLeve += f'[{y[0]}]'
print(f'Foram cadastradas {len(pessoas)} pessoas...')
print(f'O maior peso foi de {maiorpeso:.1f}Kg. Peso de {pessoaPesada}')
print(f'O menor peso foi de {menorpeso:.1f}Kg. Peso de {pessoaLeve}')