from datetime import date
data = date.today()
ano = data.year
cadastro = {}
cadastro['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
cadastro['idade'] = ano - nasc
cadastro['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if cadastro['ctps'] == 0:
    for x,y in cadastro.items():
        print(f'- {x} tem o valor {y}')
    exit()
cadastro['contratação'] = int(input('Ano de contratação: '))
cadastro['salário'] = float(input('Salário: R$'))
cadastro['aposentadoria'] = (cadastro['contratação']-nasc)+35
for x,y in cadastro.items():
        print(f'- {x} tem o valor {y}')