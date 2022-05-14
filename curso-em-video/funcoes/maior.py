def maior(*num):
    print('-='*30)
    print('Analisando os valores passados...')
    maior_valor = 0
    if len(num) > 0: 
        for x in num:
            print(x, end=' ')
            if x > maior_valor:
                maior_valor = x
    print(f'Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {maior_valor}!')

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()