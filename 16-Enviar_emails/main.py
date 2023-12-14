import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

try:
    senha = 'SuaSenha'
    servidor_email = smtplib.SMTP('smtp.dominio.com.br', 587)
    servidor_email.starttls()


    remetente = 'email@dominio.com.br'
    destinatarios = ['email@dominio.com.br']
    assunto = 'Teste'
    corpo_email = 'Olá, este é um email de teste.'

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
