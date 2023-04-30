senha='2112'
tentativa=input("Digite a senha:")
tentativas = 1

while (senha != tentativa and tentativas<3):
    print("Senha errada! Tente novamente!")
    tentativa=input("Digite a senha:")
    tentativas += 1

if tentativa == senha:
    print("Senha correta. Entrando no sistema...")
else:
    print("Este programa será encerrado após 3 tentativas incorretas da senha...")