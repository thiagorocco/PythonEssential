'''
    datetime

    datetime.now() - Retorna a data atual
    datetime.datetime(ano,mes,dia) - Retorna uma data conforme informado ano/mes/dia

    strftime(caractere): Imprime uma informação específica da data conforme abaixo:
        %a texto dia da semana abreviado
        %A texto dia da semana
        %w número dia da semana - 0 Sunday to 6 Saturday
        %W número da semana do ano
        %d número dia do mês - Retorna o número do mês.EX: nov = 11, jan = 1
        %b texto mês abreviado
        %B texto mês
        %m número do mês
        %M minutos
        %S segundos
        %f microsegundos
        %j Dia do ano 001 - 365 ou 366
'''
import datetime
import math

data_atual = datetime.datetime.now()

#Imprimindo a data_atual de 3 formas diferentes:
print(f'{data_atual.day}/{data_atual.month}/{data_atual.year}')
print(str(data_atual.day)+'/'+str(data_atual.month)+'/'+str(data_atual.year))
print(data_atual.day,'/',data_atual.month,'/',data_atual.year)

#Trabalhando com data de nascimento
day = 7
month = 11
year = 1989
data_nasc = datetime.datetime(year,month,day)

anos = math.floor((data_atual - data_nasc).days/365)
meses = math.floor(((data_atual - data_nasc).days/365 - anos)*12)
dias = math.floor(((data_atual - data_nasc).days/365 - anos)*12 - meses)

print(f'Você tem {anos} anos, {meses} meses e {dias} de vida')
