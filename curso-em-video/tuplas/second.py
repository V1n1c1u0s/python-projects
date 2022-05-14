'''
numero1 = int(input())
numero2 = int(input())
numero3 = int(input())
numero4 = int(input())

tupla = (numero1,numero2,numero3,numero4)
'''
tupla = (int(input()),int(input()),int(input()),int(input()))

print(tupla.count(9))
'''
if tupla.count(3) == 0:
    print('Num 3 não tá presente')
else:
    print(tupla.index(3))
'''
if 3 in tupla:
    print(tupla.index(3))
else:
    print('3 não tá presente')

for x in tupla:
    if x % 2 == 0:
        print(x, end=' ')

'''
for x in range(0,len(tupla)):
    if tupla[x] % 2 == 0:
        print(tupla[x],end=' ')
'''
teste = 0.4   #40/100
print('\n{:.0%}'.format(teste))
print(f'{teste:.0%}')