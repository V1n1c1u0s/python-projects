import requests

def verificaCep(cep):
    if len(cep) != 8:
        print('\nCEP Inválido!')
        return
    request = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    info_cep = request.json()
    if 'erro' not in info_cep:
        print(f'''\nCEP ENCONTRADO:\n
        CEP: {cep}
        Endereço: {info_cep['logradouro']}
        Bairro: {info_cep['bairro']}
        Cidade: {info_cep['localidade']}
        Estado: {info_cep['uf']}''')
    else:
        print('\nCEP Inválido!')
    return

if __name__ == '__main__':
    while True:
        cep = input("\nDigite o CEP para consulta: ")
        verificaCep(cep)
        continuar = input("\nDeseja continuar consulta: S/N ")
        if continuar in 'Nn':
            break