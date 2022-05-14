lista = []

while True:
    '''numero = int(input("Digite um número: "))
    lista.append(numero)'''
    lista.append(int(input("Digite um número: ")))
    resposta = str(input("Deseja continuar adicionando? [S/N] "))
    if resposta in "Nn":
        break

quantidade = len(lista)
print(f"Foi digitado {quantidade} números...")

lista.sort(reverse=True)
print(lista)

if 5 in lista:
    print("O número 5 foi digitado está na lista...")
else:
    print("O valor 5 não foi digitado e não está na lista")