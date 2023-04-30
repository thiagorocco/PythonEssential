desc = 10

def desconto(valor):
    #modificador "global" indica que estamos referenciando uma variável global
    global desc
    print('Preço original: R$ ',valor)
    print('Desconto      : R$ ',desc,'%')

    desc /= 100
    print('Valor desconto: ',valor*desc)
    print('Preço c/ desconto: ',valor*(1-desc))

val = float(input('Preço do produto: '))
desconto(val)
