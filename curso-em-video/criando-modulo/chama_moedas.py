from moedas import *

preco = float(input('Digite o preço: R$'))
print(f'O dobro de {moeda(preco)} é {dobro(preco, True)}')
print(f'A metade de {moeda(preco)} é {metade(preco, True)}')
print(f'Aumentando 10%, temos {aumentar(preco, 10, True)}')
print(f'Diminuindo 13%, temos {diminuir(preco, 13, True)}')