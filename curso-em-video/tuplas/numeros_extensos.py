numerosExtensos = (
    'zero',
    'um',
    'dois',
    'três',
    'quatro',
    'cinco',
    'seis',
    'sete',
    'oito',
    'nove',
    'dez',
    'onze',
    'doze',
    'treze',
    'catorze',
    'quinze',
    'dezesseis',
    'dezessete',
    'dezoito',
    'dezenove',
    'vinte'
)

while 1:
    numero = int(input('Digite um número inteiro entre 0 e 20: '))
    if 0 <= numero <= 20:
        break
    print('Tente Novamente!',end='\n')
print(f'Você digitou o número {numerosExtensos[numero]}')