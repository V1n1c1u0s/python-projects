'''
() -> Tupla
[] -> Lista
{} -> Dicionário
'''

comidas = ('sushi','pizza','lasanha','parmegiana')

for cont1 in comidas:
    print(f'Eu cou comer {cont1}',end='\n')    #Aqui é pego os dados

for cont2 in range(0, len(comidas)):
    print(f'Eu vou comer {comidas[cont2]}')    #Aqui é pego a posição

for pos, lanche in enumerate(comidas):         #Aqui é pego tanto a posição como os dados, a primeira variável pega a posição ...
    print(f'Eu vou comer {lanche} - Posição[{pos}]')

print(sorted(comidas)) #Mostra a tupla em ordem
a = (2,66,3,1,4,55,11,74,1000)
print(sorted(a))
b = (22,5,22,3,5,1,22)
print(b.count(22))      #.count é o método do objeto que diz quantas vezes uma determinada coisa aparece na tupla
c = ('Caio','Caio','Caio')
print(c.count('Caio'))
d = a+b+c       #Concatenação das tuplas, formando uma nova tupla
print(d)
print(b.index(1))   #.index é o método que diz em que posição determinada coisa se encontra
print(b.index(5,3)) #Procura o elemento 5 a partir da posição 3
del(d)  #Deleta a tupla d