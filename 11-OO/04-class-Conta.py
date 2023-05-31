class Conta:
    saldo = 0.0
    def __init__(self):
        print("Conta do cliente criada")
 
    def depositar(self, num):
        if(num>0):
            self.saldo += num
        else:
            print("Nao é possível depositar 0 ou menos")
    def sacar(self, valor):
        if(valor<=self.saldo):
            self.saldo -= valor
        else:
            print("Valor insuficiente. Você tem:", self.saldo)

    def exibeSaldo(self):
        return self.saldo
 
pessoa = Conta()
op = True

while op:
    print("0. Sair")
    print("1. Exibir saldo")
    print("2. Depositar")
    print("3. Sacar")
    op=int(input())

    if(op==1):
        print("Saldo:", pessoa.exibeSaldo() )
    elif(op==2):
        num=float(input("Valor para depositar:"))
        pessoa.depositar(num)
    elif(op==3):
        num=float(input("Valor para sacar:"))
        pessoa.sacar(num)
    else:
        print("Saindo do sistema...")
        break