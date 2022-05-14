from random import randint

'''lista = []

def sortear(x,y):
    return randint(x,y)

def somar(x, y):
    soma = 0
    for b in range(1,7):
        lista.append(int(sortear(x,y)))
    for m in lista:
        if m % 2 == 0:
            soma += m
    return soma

print(f"Somando os valores pares de {lista[:]}, temos {somar(1,9)}")
print(lista[:])
lista.clear()
print('Somando os valores pares de {}, temos {}'.format(lista, somar(1,9)))'''

def sorteia(lista):
    for x in range(1,7):
        lista.append(randint(1,10))

def somapar(lista):
    soma = 0
    for x in lista:
        if x % 2 == 0:
            soma += x
    print(f'Somando os valores pares de {lista}, temos {soma}')

num = []
sorteia(num)
somapar(num)