lista = []
def ordenar(*lista):
    '''
    ->Ordena a lista do menor para o maior
    :param *lista: Lista contendo os números desordenados
    '''
    return sorted(lista)

lista = ordenar(100,58,102,93,5,2,9,1,0,77)
print(lista)

print(input.__doc__)
help(__doc__)
help(ordenar)

def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de 3 valores e mostra o resulta na tela
    :param a: 1° Valor
    :param b: 2° Valor
    :param c: 3° Valor
    """
    s = a+b+c
    print(s)

somar()
somar(1)
somar(1,2)
somar(1,2,3)
help(somar)