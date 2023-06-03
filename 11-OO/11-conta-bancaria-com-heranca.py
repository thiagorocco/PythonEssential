class Conta:
    def __init__(self):
        self.saldo = 0

    def getSaldo(self):
        return self.saldo
        
class PF(Conta):
    def __init__(self,):
        Conta.__init__(self)

    def setSaldo(self, valor):
        self.saldo += valor - 5

class PJ(Conta):
    def __init__(self):
        Conta.__init__(self)
    
    def setSaldo(self, valor):
        self.saldo += valor - 10

print('1.Criar conta Pessoa Física')
print('2.Criar conta Pessoa Jurídica')
op = int(input('Opção:'))

if op == 1:
    conta = PF()
elif op == 2:
    conta = PJ()

while True:
    print('1. ver saldo')
    print('2. Sacar / Depositar')
    op = int(input("Opção:"))
 
    if op == 1:
        print("R$", conta.getSaldo())
    elif op==2:
        val = float(input("Valor para movimentar:"))
        conta.setSaldo(val)
