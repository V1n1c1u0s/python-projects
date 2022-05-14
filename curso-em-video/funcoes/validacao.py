def leiaInt(txt):
    while True:
        num = input(txt)
        if num.isnumeric():
            return num
        else:
            print('\033[36mERRO! Digite um número inteiro válido!\033[m') 

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')