lista = []

for x in range(5):
    numero = int(input("Digite um número: "))
    if x == 0 or lista[-1] < numero:
        lista.append(numero)
        print(f"Adicionado na posição {x}...")
        print(lista)
    else:
        pos = 0
        while pos <= len(lista):
            if numero <= lista[pos]:
                lista.insert(pos,numero)
                print(f"Adicionado na posição {pos}...")
                break
            pos += 1
print(lista)