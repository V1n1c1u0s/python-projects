from time import sleep
#flush=True diz pra não ligar o buffer de tela, permitindo assim, a utilização correta do sleep()
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    if inicio < fim:
        while inicio <= fim:
            print(f'{inicio}', end=' ', flush=True)
            sleep(0.5)
            inicio += passo
        print('FIM')
    else:
        while inicio >= fim:
            print(f'{inicio}', end=' ', flush=True)
            sleep(0.5)
            inicio -= passo
        print('FIM')

contador(1,10,1)
contador(10,0,2)

num1 = int(input("Início: "))
num2 = int(input("Fim: "))
num3 = int(input("Passo: "))
contador(num1,num2,num3)