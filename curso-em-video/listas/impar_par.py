numeros = [[],[]]
valor = 0

for i in range(1,8):
    valor = int(input(f'Digite o valor {i}: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
numeros[0].sort(); numeros[1].sort()
print(numeros[0])
print(numeros[1])