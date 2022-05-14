lista = []
'''resposta = 's'
while resposta == 's':
    numero = int(input("Digite um número: "))
    if numero in lista:
        print("Valor duplicado! Não vou adicionar...")
    else:
        lista.append(numero)
        print("Valor adicionado com sucesso...")
    resposta = str(input("Deseja continuar? [S/N] ")).lower()
lista.sort()
print(f"Você digitou os valores {lista}")'''
while True:
    n = int(input("Digite um número: "))
    if n not in lista:
        lista.append(n)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado! Não vou adicionar...")
    resposta = str(input("Deseja continuar? [S/N] "))
    if resposta in 'NnNAOnaoNaoNãonãoNÃO':
        break
lista.sort()
print(f"Você digitou os valores {lista}")