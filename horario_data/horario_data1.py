from datetime import datetime, timedelta, timezone
from datetime import date

dataAtual = datetime.now()
print(dataAtual)
data = dataAtual.date()
print(data)
print(data.year)
#data.year e data.strftime(%Y) é a msm merda
ano = data.strftime('%Y')
print(ano)

data = date.today()
print(data)
print(data.year)

data_atual = date.today()
data_em_texto = data_atual.strftime('%d/%m/%Y')
print(data_em_texto)

data_e_hora_em_texto = '09/10/2021 12:30'
data_e_hora = datetime.strptime(data_e_hora_em_texto, '%d/%m/%Y %H:%M')
print(data_e_hora)

outro = datetime.now()
prova = outro.year #Não necessita do outro.date() pra poder fazer outro.year, pode-se fazer outro.year direto
print(prova)

data_e_horas_atuais = datetime.now()
data_e_horas_atuais_em_texto = data_e_horas_atuais.strftime('%d/%m/%Y %H:%M')
print(data_e_horas_atuais_em_texto)
diferenca = timedelta(hours=-3)
print(diferenca)
fuso_horario = timezone(diferenca)
print(fuso_horario)

date_e_hora_sp = data_e_horas_atuais.astimezone(fuso_horario)
data_e_hora_sp_em_texto = date_e_hora_sp.strftime('%d/%m/%Y %H:%M')
print(data_e_hora_sp_em_texto)

'''
timedelta recebe vários outros argumentos além da hora, nessa ordem:

days (dias)
seconds (segundos)
microseconds (microsegundos)
milliseconds (milisegundos)
minutes (minutos)
hours (horas)
weeks (semanas)
'''