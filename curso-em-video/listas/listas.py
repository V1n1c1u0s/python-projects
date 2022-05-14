listas = ['a','i']
listas.append('o') #Insere no final
listas.insert(0,'c') #Insere na posição 0
print(listas)
listas.insert(0,"Eu sou")
listas.insert(1,"foda !")
listas.insert(2,"Eu sou")
listas.append("!")
print(listas)
del listas[0] #Deleta a posição informada
listas.pop(0)
listas.pop()   #Sem parâmetro, apaga o último elemento. Mas pode-se passar a posição que quer deletar
print(listas)
listas.remove('Eu sou') #Remove a posição que tiver esse valor
print(listas)
lista = list(range(4,11)) #Cria uma lista com valores de 4 até 10
print(lista)
lista2 = list(range(10,21,2)) #Cria uma lista com valores de 10 até 20 contando de 2 em 2
print(lista2)
lista3 = [8,2,5,4,9,3,0]
lista3.sort() #Ordena a lista
print(lista3)
lista3.sort(reverse=True) #Ordena e mostra de trás pra frente
print(lista3)

a = [2,3,4,7]
b = a    #Aqui o python cria uma ligação entre b e a, então se um dos 2 for alterado, a outra lista tbm será alterada. (Ponteiros)
b[2] = 8
print(a,b)
c = [2,3,4,7]
d = c[:]    #Agora foi criada uma cópia de c, e não uma ligação
c[2] = 8
print(c,d)