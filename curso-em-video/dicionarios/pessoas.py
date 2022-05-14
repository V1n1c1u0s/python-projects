pessoa = dict()
pessoas = list()
mulheres = list()
acima_media = list()
soma = media = 0
while True:
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('[ERRO] Digite apenas M ou F')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    pessoas.append(pessoa.copy())
    while True:
        resp = str(input('Deseja continuar cadastrando? ')).upper()[0]
        if resp in 'SN':
            break
        print('Responda apenas com S ou N')
    if resp == 'N':
        break
media = soma/len(pessoas)
for y in pessoas:
    if y['Sexo'] == 'F':
        mulheres.append(y['Nome'])
    if y['Idade'] > media:
        acima_media.append(y['Nome'])
print(f'Foram cadastradas {len(pessoas)} pessoas!')
print(f'A média de idade do grupo é: {media:.1f} anos!')
print(f'Mulheres cadastradas: {mulheres}')
print(f'Pessoas acima da média de idade: {acima_media}')