from datetime import date

def voto(idade):
    if idade < 16:
        return 'NEGADO'
    elif idade >= 16 and idade < 18 or idade > 65:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'  

ano_atual = date.today().year

while True:
    try:
        ano_nascimento = int(input("Digite seu ano de nascimento: "))
        if (idade := ano_atual - ano_nascimento) <= 110 and idade >= 0:
            break
        else:
            print("Valor Inválido. Tente Novamente!")
    except ValueError:
        print("Valor Inválido. Tente Novamente!")

seu_voto = voto(idade)
print(f'Na sua idade, seu voto é {seu_voto}!')