def aumentar(valor = 0, taxa = 0, format = False):
    aux = valor*(taxa/100)
    return valor+aux if format is False else moeda(valor+aux)

def diminuir(valor = 0, taxa = 0, format = False):
    aux = valor*(taxa/100)
    return valor-aux if format is False else moeda(valor-aux)

def dobro(valor = 0, format = False):
    return valor*2 if format is False else moeda(valor*2)

def metade(valor = 0, format = False):
    return valor/2 if format is False else moeda(valor/2)

def moeda(valor = 0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')