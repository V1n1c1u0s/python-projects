def interative_help(funcao):
    manual = f"Acessando o manual do comando '{funcao}'"
    if funcao != 'fim':
        print('\033[1;37;44m',end=f"{'~'*(len(manual)+4)}\n")
        print(f'  {manual}  ')
        print('~'*(len(manual)+4), end='\033[m')
        print('\033[1;37;42m');help(funcao);print('\033[m',end='')
    else:
        return 'fim'
    

info_funcao = ''

while info_funcao != 'fim':
    print('\033[1;37;41m',end=f"{'~'*27}\n")
    print('  SISTEMA DE AJUDA PyHELP  ')
    print('~'*27,end='\033[m\n')
    funcao = str(input('Função ou Biblioteca > '))
    info_funcao = interative_help(funcao)