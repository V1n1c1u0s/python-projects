lista = []
listaPar = []
listaImpar = []
while True:
    numero = int(input("Digite um número: "))
    lista.append(numero)
    if numero % 2 == 0:
        listaPar.append(numero)
    else:
        listaImpar.append(numero)
    resposta = str(input("Deseja continuar adicionando? [S/N] "))
    if resposta in "Nn":
        break
print(f"Lista: {lista}")
print(f"Lista Ímpar: {listaImpar}")
print(f"Lista Par: {listaPar}")