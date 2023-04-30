import calculadoraModulo

while True:
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    op=int(input("Que operação deseja realizar: "))
    x=float(input("Primeiro numero: "))
    y=float(input("Segundo  numero: "))

    if op==1:
        print("Soma:", calculadoraModulo.soma(x,y))
    elif op==2:
        print("Subtração:", calculadoraModulo.subtracao(x,y))
    elif op==3:
        print("Multiplicação:", calculadoraModulo.multiplicacao(x,y))
    elif op==4:
        print("Divisão:", calculadoraModulo.divisao(x,y))
    else:
        print("Opção inválida,tente novamente")
