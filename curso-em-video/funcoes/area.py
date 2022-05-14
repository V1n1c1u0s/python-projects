def calculaArea(x, y):
    area = x*y
    #print(f"A área de um terreno {x}x{y} é de {area}m²")
    return area

print("Controle de Terrenos")
print("-"*20)
largura = float(input("LARGURA (m): "))
comprimento = float(input("COMPRIMENTO (m): "))
area = calculaArea(largura, comprimento)
print(f"A área de um terreno {largura}x{comprimento} é de {area}m²")