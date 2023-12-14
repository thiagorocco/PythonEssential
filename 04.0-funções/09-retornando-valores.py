def par(x):
    if (x%2)==0:
        return True
    else:
        return False

controle = True

while controle:
    num = int(input("Insira um número: "))
    if par(num):
        print("É par")
    else:
        print("É ímpar")
        controle = par(num)

