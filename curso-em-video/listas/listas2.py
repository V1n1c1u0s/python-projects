'''dados = list()
dados.append('oi')
dados.append(56)
print(dados)

teste = list()
teste.append('Caio')
teste.append(18)
galera = list()
galera.append(teste[:])
teste[0]='Laís'
teste[1]=17
galera.append(teste)
print(galera)'''

galera = list()
dados = list()
totmai = totmen = 0

for p in range(0,4):
    dados.append(str(input('Digite um nome: ')))
    dados.append(int(input('Digite umaa idade: ')))
    galera.append(dados[:])
    dados.clear()

print(galera)

for i in galera:
    if i[1] >= 21:
        print(f'{i[0]} é maior de idade...')
        totmai += 1
    else:
        print(f'{i[0]} é menor de idade...')
        totmen += 1
print(f'Há {totmai} maiores de 21 e {totmen} menores de 21')