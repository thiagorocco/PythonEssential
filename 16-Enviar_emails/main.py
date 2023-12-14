import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import config

data = datetime.datetime.now()

dataAtual = f'{data.day}/{data.month}/{data.year} às {data.hour}:{data.minute}:{data.second}'

try:
    senha = config.senha
    servidor_email = smtplib.SMTP(config.servidor, config.porta)
    servidor_email.starttls()


    remetente = config.remetente
    destinatarios = config.destinatarios
    assunto = 'Teste'
    corpo_email = f'Olá, este é um email de teste enviado em {dataAtual}'

    mensagem = MIMEMultipart()
    mensagem['From'] = remetente
    mensagem['To'] = ', '.join(destinatarios)
    mensagem['Subject'] = assunto
    mensagem.attach(MIMEText(corpo_email, 'plain', 'utf-8'))

    servidor_email.login(remetente, senha)
    servidor_email.sendmail(remetente, destinatarios, mensagem.as_string())

except Exception as e:
    print(f'Erro ao enviar e-mail: {e}')

finally:
    servidor_email.quit()
