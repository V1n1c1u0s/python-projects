from random import choice

def jogar():
    usuario = input('Sua jogada: ([P] Papel  [T] Tesoura  [Pe] Pedra): ').lower()
    computador = choice(['p','t','pe'])

    if usuario == computador:
        return 'Empate!'

    if verificarVencedor(usuario,computador):
        return 'Você venceu!'

    return 'Você perdeu!'

def verificarVencedor(jogador, oponente):
    if((jogador == 'p' and oponente == 'pe') or (jogador == 'pe' and oponente == 't') or (jogador == 't' and oponente == 'p')):
        return True

print(jogar())