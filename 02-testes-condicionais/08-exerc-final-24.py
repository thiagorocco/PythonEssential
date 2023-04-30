'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                    Até 5 Kg               Acima de 5 Kg
    Alcatra         R$ 5,90 por Kg         $ 6,80 por Kg
    File Duplo      R$ 4,90 por Kg         $ 5,80 por Kg
    Picanha         $ 6,90 por Kg          R$ 7,80 por Kg

    Para atender a todos os clientes, cada cliente poderá levar 
    apenas um dos tipos de carne da promoção, porém não há limites para a quantidade
    de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá
    ainda um desconto de 5% sobre o total a compra. 
    
    Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário 
    e gere um cupom fiscal contendo as informações da compra: tipo e quantidade de carne, preço total, 
    tipo de pagamento, valor do desconto e valor a pagar.

'''
tipoCarne = input('Informe o tipo de carne que deseja comprar? A->Alcatra, F-> Filé Duplo, P->Picanha: ')
descCarne = ''

if tipoCarne == 'A' or tipoCarne == 'a':
    descCarne = 'ALCATRA'
elif tipoCarne == 'F' or tipoCarne == 'f':
    descCarne = 'FILÉ DUPLO'
elif tipoCarne == 'P' or tipoCarne == 'p':
    descCarne = 'PICANHA'

qtde = float(input('Informe a quantidade em kg que deseja comprar: '))
tipoPgto = input('A compra será no cartão Tabajara?S-Sim, N-Não: ')
subtotal = 0
desconto = 0

if descCarne == 'ALCATRA' or descCarne == 'FILÉ DUPLO' or descCarne == 'PICANHA':
    if descCarne == 'ALCATRA':
        if qtde <= 5.00:
            subtotal = qtde * 5.90
        else:
            subtotal = qtde * 6.80
    elif descCarne == 'FILÉ DUPLO':
        if qtde <= 5.00:
            subtotal = qtde * 4.90
        else:
            subtotal = qtde * 5.80
    elif descCarne == 'PICANHA':
        if qtde <= 5.00:
            subtotal = qtde * 6.90
        else:
            subtotal = qtde * 7.80

    if tipoPgto =='S' or tipoPgto=='s':
        tipoPgto ='SIM'
        desconto = subtotal * 0.05
    else: 
        tipoPgto ='NÃO'

    totalPagar = subtotal - desconto
    print('Tipo de Carne\t\t:',descCarne,
    '\nQuantidade de Carne\t:', qtde,'KG'
    '\nPreço total\t\t: R$ %.2f' %subtotal, 
    '\nCartão Tabajara\t\t:',tipoPgto,
    '\nValor do desconto\t: R$ %.2f' %desconto,
    '\nValor a pagar\t\t: R$ %.2f' %totalPagar)
else:
    print('Informou um tipo de carne que não existe!! Tente novamente!')