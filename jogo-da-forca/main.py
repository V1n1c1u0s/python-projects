from pegar_palavra import dica,dados
import random

palavra_secreta = random.choice(dados).upper()
letras_escolhidas = []
tentativas = 6
acertos = 0

for cont in range(0, len(palavra_secreta)):
    letras_escolhidas.append("-")

acertei = False
tamanho_palavra_secreta = len(palavra_secreta)

while acertei == False:
    print("\x1b[2J\x1b[1;1H")
    print("Jogo da Forca!")
    print(f"\nDica: \033[31m{dica}\033[m")
    print(f"N° de chances restantes: {tentativas}")
    print(' '.join(letras_escolhidas))

    letra = str(input("\nDigite um letra: ")).upper()

    if letra in palavra_secreta:
        tentativas = tentativas
    else:
        tentativas -= 1

    for cont2 in range(0, tamanho_palavra_secreta):
        if letra == palavra_secreta[cont2]:
            letras_escolhidas[cont2] = letra
    acertei = True
    for cont3 in range(0, len(letras_escolhidas)):
        if letras_escolhidas[cont3] == "-":
            acertei = False 
    
    if tentativas == 0 :
        print("\nVocê perdeu!")
        exit()

print("\x1b[2J\x1b[1;1H")
print("Jogo da Forca!")
print(f"\nDica: \033[31m{dica}\033[m")
print(f"N° de chances restantes: {tentativas}")
print(' '.join(letras_escolhidas))
print(f"Parabéns você venceu!")