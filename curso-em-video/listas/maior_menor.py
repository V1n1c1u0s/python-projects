lista = []
menor_numero = 0
maior_numero = 0

for i in range(0,5):
    lista.append(int(input(f"Digite um número na posição {i}: ")))
    if i == 0:
        maior_numero = menor_numero = lista[i]
    else:
        if lista[i] > maior_numero:
            maior_numero = lista[i]
        if lista[i] < menor_numero:
            menor_numero = lista[i]

posicao_menor = ""
posicao_maior = ""

for x,y in enumerate(lista):
    if y == maior_numero:
        posicao_maior += f'{x}... '
    if y == menor_numero:
        posicao_menor += f'{x}... '

print(f"Menor número: {menor_numero}, Posição(ões): {posicao_menor}")
print(f"Maior número: {maior_numero}, Posição(ões): {posicao_maior}")