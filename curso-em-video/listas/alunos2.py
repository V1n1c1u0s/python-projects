ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/2
    ficha.append([nome,[nota1,nota2],media])
    resp = str(input('Quer continuar cadastrando? '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for x,y in enumerate(ficha):
    print(f'{x:<4}{y[0]:<10}{y[2]:>8.1f}')
while True:
    print('-'*35)
    aluno = int(input('Mostrar notas de qual aluno? [999 interrompe] '))
    if aluno == 999:
        break
    if aluno <= len(ficha)-1:
        print(f'Notas de {ficha[aluno][0]} são {ficha[aluno][1]}')