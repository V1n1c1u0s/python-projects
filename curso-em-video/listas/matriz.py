matriz = [[],[],[]]
soma_pares = soma_terc_coluna = maior_valor_seg_coluna = 0

for x in range(3):
    for y in range(3):
        numero = int(input(f'Digite um valor para [{x}][{y}]: '))
        matriz[x].append(numero)

for c in range(3):
    for d in range(3):
        print(f'[{matriz[c][d]:^5}]',end='')
        if matriz[c][d] % 2 == 0:
            soma_pares += matriz[c][d]
        if d == 2:
            soma_terc_coluna += matriz[c][d]
        if matriz[1][d] > maior_valor_seg_coluna:
            maior_valor_seg_coluna = matriz[1][d]
    print()

print(f'Soma de todos os valores pares: {soma_pares}')
print(f'Soma dos valores da terceira coluna: {soma_terc_coluna}')
print(f'Maior valor da segunda linha: {maior_valor_seg_coluna}')