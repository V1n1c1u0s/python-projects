from datetime import datetime
from pytz import timezone

data_hora_atual = datetime.now()
fuso_horario = timezone('America/Sao_Paulo')
data_hora_sao_paulo = data_hora_atual.astimezone(fuso_horario)
data_hora_sao_paulo_texto = data_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')
print(data_hora_sao_paulo_texto)