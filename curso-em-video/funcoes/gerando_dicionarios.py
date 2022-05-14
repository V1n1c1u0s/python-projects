def notas(*notas, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param *notas: uma ou mais notas dos alunos(aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação das notas
    """
    info_notas = {
        'total': len(notas),
        'maior': max(notas),
        'menor': min(notas),
        'média': sum(notas)/len(notas) 
    }
    if sit:
        if info_notas['média'] >= 7:
            info_notas['situação'] =  'BOA'
        elif info_notas['média'] >= 5:
            info_notas['média'] = 'REGULAR'
        else:
            info_notas['média'] =  'PÉSSIMA'
    return info_notas

info_notas = notas(10, 4, 7, sit=False)
print(info_notas)