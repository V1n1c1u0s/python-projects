import string, random

letras = string.ascii_letters
numeros = string.digits
pontuacao = string.punctuation
opcoes = letras+numeros+pontuacao
print(opcoes)

def gerarSenha(tamanho):
    senha = ''
    for x in range(0, tamanho):
        digito = random.choice(opcoes)
        senha += digito
    return senha

tamanho = int(input('Digite o número de dígitos que você deseja para sua senha: [Mínimo - 8] '))
senha = gerarSenha(tamanho)

print(f"Senha gerada: {senha}")