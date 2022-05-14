lista = []
'''cont = 0
cont2 = 0
expressao = str(input("Digite uma expressão: "))
for y in expressao:
    if y == '(':
        lista.append(y)
    elif y == ')':
        lista.append(y)
for x in lista:
    if x == '(':
        cont += 1
    elif x == ')':
        cont2 += 1
if cont2 == cont and cont2 > 0:
    print("Expressão válida...")
else:
    print("Expressão inválida...")'''
expressao = str(input("Digite uma expressão: "))
for y in expressao:
    if y == '(':
        lista.append(y)
    if y == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(y)
            break
if len(lista) == 0:
    print("Expressão válida...")
else:
    print("Expressão inválida!")